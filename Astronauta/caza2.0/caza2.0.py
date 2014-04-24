from PyQt4 import QtGui, QtCore
import sys,os

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC

from MPUaccel import ReadAccel


#Inputs Buttons Configuration
Sw1 = "P9_30"; Sw2 = "P9_26" ; Sw3 = "P9_24" 
GPIO.setup(Sw1, GPIO.IN)
GPIO.setup(Sw2, GPIO.IN)
GPIO.setup(Sw3, GPIO.IN)

#Output Leds Configuration
Led1 = "P8_8"; Led2 = "P8_10"; Led3 = "P8_12"; Led4 = "P8_14"
GPIO.setup(Led1, GPIO.OUT)
GPIO.setup(Led2, GPIO.OUT)
GPIO.setup(Led3, GPIO.OUT)
GPIO.setup(Led4, GPIO.OUT)

#ADC Configuration P9_36 = AIN5
ADC.setup()


class MicroGravedadControl(QtCore.QObject):

    def __init__(self):
        super(MicroGravedadControl, self).__init__()
        # Thread Accel
        self.threadimu = QtCore.QThread() 
        self.workerimu = WorkerImu()      
        self.workerimu.moveToThread(self.threadimu) 
        self.threadimu.started.connect(self.workerimu.setup) 
        
        # adding by emitting signal in different thread
        self.threadadc = QtCore.QThread()
        self.workeradc = WorkerADC()
        self.workeradc.moveToThread(self.threadadc)
        self.threadadc.started.connect(self.workeradc.setup)

        self.crearDir() ## crear directorio
        print "Push Start Button"
        
        GPIO.add_event_detect("P9_24", GPIO.RISING,callback=self.start, bouncetime=100)
        GPIO.add_event_detect("P9_26", GPIO.RISING,callback=self.stop, bouncetime=100)
        

    def start(self,isr): 
        #-----------------------------------
        print "Start Capture"
        #self.threadadc.start() # Worker Thread setup start
        self.threadimu.start() # Worker Thread setup start
        GPIO.remove_event_detect("P9_24")
        #-----------------------------------
        return
    
    def stop(self,isr): 
        #------------------
        if self.threadadc.isRunning() == True:
            self.workeradc.stop()
            self.threadadc.quit()
            self.threadadc.terminate()
            print "stop Thread"
            #------------------
        if self.threadimu.isRunning() == True:
            self.workerimu.stopFlag()
            exitWorkerFlag = self.workerimu.exitWorker
            while  exitWorkerFlag != 1:
                exitWorkerFlag = self.workerimu.exitflag
                #print "waiting..."
            self.threadimu.quit()
            self.threadimu.terminate()
            print "stop Thread"
            #------------------    
        print "stop program"
        GPIO.output(Led1,GPIO.LOW) #Led1 off Indicates thats software it's not running
        GPIO.cleanup()
        QtCore.QCoreApplication.exit(0) # exit app
        return

    def crearDir(self):
        self.directorioOriginal = os.getcwd()
        carpeta = "caza2.0/data" 

        directorio = os.path.join(os.pardir, carpeta)
        if not os.path.isdir(directorio):
            os.mkdir(directorio)
        os.chdir(directorio)

class WorkerImu(QtCore.QObject):
    def readImu(self):
        fax, fay, faz= self.Imu.readAccel()
        ax = "%.4f" % round(fax,4)
        ay = "%.4f" % round(fay,4)
        az = "%.4f" % round(faz,4)
        #print "acel x: ", ax, " acel y: ", ay, " acel z: ", az
        self.data[0] = ax
        self.data[2] = ay
        self.data[4] = az
        
        for i in self.data:
            if (self.stopflag == 0):
                with open("accel.txt", "a") as self.accel:
                    self.accel.write(str(i))
                    self.accel.flush()
            elif (self.stopflag == 1):
                print "Stop Reading Imu"
                self.exitflag = 1
                self.accel.close() #close accel file
                self.timer.stop()
                self._exit = True
                
    def stopFlag(self):
        self.stopflag = 1
    def exitWorker(self):
        return self.exitflag
    def setup(self):
        self.stopflag = 0
        self.exitflag = 0
        #Configuration of Accel Sensor
        self.Imu=ReadAccel()
        self.accel = open("accel.txt", "w")
        self.accel.write("Ax;Ay;Az;")
        self.accel.write("\n")
        self.accel.close() #close accel file    
        self.data = [0,';',0,';',0,';',"\n"]

        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.readImu)
        self.timer.start(20)
        
class WorkerADC(QtCore.QObject):
    def readEcg(self):
        print "Read Adc"
        #read Adc
        #value = ADC.read("AIN5") * 1.8 # convierte la lectura a tension
    def stop(self):
        self.timer.stop()
        self._exit = True
    def setup(self):
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.readEcg)
        self.timer.start(200)
                
if __name__ == "__main__":
    app = QtCore.QCoreApplication(sys.argv)
    micro = MicroGravedadControl()
    GPIO.output(Led1,GPIO.HIGH) #Led1 on Indicates thats software it's running
    sys.exit(app.exec_())
