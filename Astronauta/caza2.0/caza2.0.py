from PyQt4 import QtGui, QtCore
import sys,os,time

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import Adafruit_BMP.BMP085 as BMP085


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
        self.threadImu = QtCore.QThread() 
        self.workerImu = WorkerImu()      
        self.workerImu.moveToThread(self.threadImu) 
        self.threadImu.started.connect(self.workerImu.setup) 
        
        # adding by emitting signal in different thread
        self.threadAdc = QtCore.QThread()
        self.workerAdc = WorkerADC()
        self.workerAdc.moveToThread(self.threadAdc)
        self.threadAdc.started.connect(self.workerAdc.setup)
        
        # adding by emitting signal in different thread
        self.threadTemp = QtCore.QThread()
        self.workerTemp = WorkerTemp()
        self.workerTemp.moveToThread(self.threadTemp)
        self.threadTemp.started.connect(self.workerTemp.setup)
        
        self.crearDir() ## crear directorio
        print "Push Start Button"
        
        GPIO.add_event_detect("P9_24", GPIO.RISING,callback=self.start, bouncetime=200)
        GPIO.add_event_detect("P9_26", GPIO.RISING,callback=self.stop, bouncetime=200)
        GPIO.add_event_detect("P9_30", GPIO.RISING,callback=self.exitapp, bouncetime=200)
        

    def start(self,isr): 
        #-----------------------------------
        print "Start Capture"
        #self.threadAdc.start() # Worker Thread setup start
        self.threadImu.start() # Worker Thread setup start
        self.threadTemp.start() # Worker Thread setup start
        GPIO.remove_event_detect("P9_24")
        GPIO.output(Led2,GPIO.HIGH) #Led1 on Indicates thats software it's running
        #-----------------------------------
    
    def stop(self,isr): 
        #------------------
        if self.threadAdc.isRunning() == True:
            self.workerAdc.stop()
            self.threadAdc.quit()
            self.threadAdc.terminate()
            print "stop adcThread"
        #------------------
        if self.threadImu.isRunning() == True:
            self.workerImu.stopFlag()
            exitWorkerFlag = self.workerImu.exitWorker
            while  exitWorkerFlag != 1:
                time.sleep(0.05)
                exitWorkerFlag = self.workerImu.exitflag
            self.threadImu.quit()
            #self.threadImu.terminate()
            print "stop imuThread"
        #------------------
        if self.threadTemp.isRunning() == True:
            self.workerTemp.stopFlag()
            exitWorkerFlag = self.workerTemp.exitWorker
            while  exitWorkerFlag != 1:
                time.sleep(0.05)
                exitWorkerFlag = self.workerTemp.exitflag
            self.threadTemp.quit()
            print "stop tempThread"
            
        print "stop capture"
        GPIO.output(Led2,GPIO.LOW) #Led2 off Indicates stops capture
       
    def exitapp(self,isr):
        print "Exit App"
        GPIO.cleanup()
        GPIO.output(Led1,GPIO.LOW) #Led1 off Indicates thats software it's not running
        QtCore.QCoreApplication.exit(0) # exit app    

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
        print "acel x: ", ax, " acel y: ", ay, " acel z: ", az
        self.data[0] = ax
        self.data[2] = ay
        self.data[4] = az
        
        for i in self.data:
            if (self.stopflag == 0):
                with open("accel.txt", "a") as self.accel:
                    self.accel.write(str(i))
                    self.accel.flush()
            elif (self.stopflag == 1):
                #print "Stop Reading Imu"
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

class WorkerTemp(QtCore.QObject):
    def readTemp(self):
        #read temperature
        self.bmpData[0] = "%.2f" % round(self.sensorTemp.read_temperature(),2)
        self.bmpData[2] = "%.2f" % round(self.sensorTemp.read_pressure(),2)
        self.bmpData[4] = "%.2f" % round(self.sensorTemp.read_altitude(),2)
        self.bmpData[6] = "%.2f" % round(self.sensorTemp.read_sealevel_pressure(),2) 
        print self.bmpData
        for i in self.bmpData:
            if (self.stopflag == 0):
                with open("bmpdata.txt", "a") as self.bmpdatafile:
                    self.bmpdatafile.write(str(i))
                    self.bmpdatafile.flush()
            elif (self.stopflag == 1):
                #print "Stop Reading bmp180"
                self.exitflag = 1
                self.bmpdatafile.close() #close  file
                self.timer.stop()
                self._exit = True            
    def stopFlag(self):
        self.stopflag = 1
    def exitWorker(self):
        return self.exitflag
    def setup(self):
        self.stopflag = 0
        self.exitflag = 0
        self.sensorTemp = BMP085.BMP085()
        self.bmpdatafile = open("bmpdata.txt", "w")
        self.bmpdatafile.write("Temp;Pressure;Altitude;seaLevelP;")
        self.bmpdatafile.write("\n")
        self.bmpdatafile.close() #close accel file    
        self.bmpData = [0,';',0,';',0,';',0,';',"\n"]
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.readTemp)
        self.timer.start(1000)
    
if __name__ == "__main__":
    app = QtCore.QCoreApplication(sys.argv)
    micro = MicroGravedadControl()
    GPIO.output(Led1,GPIO.HIGH) #Led1 on Indicates thats software it's running
    sys.exit(app.exec_())
