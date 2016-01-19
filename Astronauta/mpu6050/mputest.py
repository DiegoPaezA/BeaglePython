from PyQt4 import QtGui, QtCore
import sys,os

import Adafruit_BBIO.GPIO as GPIO
from MPU6050 import MPU6050

GPIO.setup("P9_24", GPIO.IN)
GPIO.setup("P9_26", GPIO.IN)

class MicroGravedad(QtCore.QObject):

    def __init__(self):
        super(MicroGravedad, self).__init__()
        
        # Thread Imus Temperatura
        self.threadimu = QtCore.QThread()
        self.workerimu = WorkerImu()
        self.workerimu.moveToThread(self.threadimu)
        self.threadimu.started.connect(self.workerimu.loop)
        
        # adding by emitting signal in different thread
        self.threadadc = QtCore.QThread()
        self.workeradc = WorkerADC()
        self.workeradc.moveToThread(self.threadadc)
        self.threadadc.started.connect(self.workeradc.loop)

        self.dataread = raw_input("Enter Session Name: ")
        self.crearDir() ## crear directorio
        print "Push Start button"
        
        GPIO.add_event_detect("P9_24", GPIO.RISING,callback=self.start, bouncetime=100)
        GPIO.add_event_detect("P9_26", GPIO.RISING,callback=self.stop, bouncetime=100)
        

    def start(self,isr): 
        #-----------------------------------
        print "Start Capture"
        #self.threadadc.start() # Worker Thread
        self.threadimu.start() # Worker Thread
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
            self.workerimu.stop()
            self.threadimu.quit()
            self.threadimu.terminate()
            print "stop Thread"
            #------------------    
        print "stop program"
        QtCore.QCoreApplication.exit(0) # exit app
        return
    def test(self):
        print "its working"
    def crearDir(self):
        self.directorioOriginal = os.getcwd()
        carpeta = "mpu6050/" +  str(self.dataread)

        directorio = os.path.join(os.pardir, carpeta)
        if not os.path.isdir(directorio):
            os.mkdir(directorio)
        os.chdir(directorio)

class WorkerImu(QtCore.QObject):
    def readImu(self):
        fax, fay, faz, fgx, fgy, fgz= self.Imu.readSensors()
        ax = "%.4f" % round(fax,4)
        ay = "%.4f" % round(fay,4)
        az = "%.4f" % round(faz,4)
        #print "acel x: ", ax, " acel y: ", ay, " acel z: ", az
        self.data[0] = ax
        self.data[2] = ay
        self.data[4] = az
        
        for i in self.data:
            if self.off == 1:
                self.accel.write(str(i))
            elif self.off == 0:
                print "off Cambio"
                self.accel.close() #close accel file       
        self.ite += 1
        if self.ite == 50:
            print "Read Temperatura"
            self.ite = 0
            
    def stop(self):
        self.off = 0
        self.timer.stop()
        self._exit = True
    def loop(self):
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.readImu)
        self.timer.start(20)
        #Clase leer aceleracion
        self.Imu=MPU6050()
        self.accel = open("accel.txt", "w")
        self.accel.write("Ax;Ay;Az;")
        self.accel.write("\n")
        self.data = [0,';',0,';',0,';',"\n"]
        self.ite = 0
        self.off = 1
        
class WorkerADC(QtCore.QObject):
    def readEcg(self):
        print "Read Adc"
    def stop(self):
        self.timer.stop()
        self._exit = True
    def loop(self):
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.readEcg)
        self.timer.start(200)
        
        
        
if __name__ == "__main__":
    
    app = QtCore.QCoreApplication(sys.argv)
    micro = MicroGravedad()
    sys.exit(app.exec_())
