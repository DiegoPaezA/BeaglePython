from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
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
        
        print "Qthread Number: " + str(QtCore.QThread.idealThreadCount()) 
        # Thread Accel
        '''
        self.threadImu = QtCore.QThread() 
        self.workerImu = WorkerImu()      
        self.workerImu.moveToThread(self.threadImu) 
        self.threadImu.started.connect(self.workerImu.setup)
        QtCore.QObject.connect(self.workerImu,SIGNAL("asignal"),self.workerImu.startTimer)
        '''
        self.threadAdc = QtCore.QThread() 
        self.workerAdc = WorkerADC()      
        self.workerAdc.moveToThread(self.threadAdc) 
        self.threadAdc.started.connect(self.workerAdc.setup)
        QtCore.QObject.connect(self.workerAdc,SIGNAL("asignal"),self.workerAdc.startTimer)

        
        self.crearDir() ## crear directorio
        print "Push Start Button"
        
        
        GPIO.add_event_detect("P9_26", GPIO.RISING,callback=self.stop, bouncetime=200)
        GPIO.add_event_detect("P9_30", GPIO.RISING,callback=self.exitapp, bouncetime=200)
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.Demo)
        #self.timer.start(1000)
        
        self.start_stop_flag = 0
        self.xx = 0
    def Demo(self):
        print "Timer Workig"
    def startTimer(self):
        if self.xx == 0:
          self.timer.start(500)
          self.threadAdc.start() # Worker Thread setup start
          self.xx=1
        elif self.xx == 1:
            self.timer.start(500)
            self.workerAdc.afunc()
        if self.start_stop_flag == 1:
            GPIO.add_event_detect("P9_26", GPIO.RISING,callback=self.stop, bouncetime=200)    
        self.start_stop_flag = 0
        GPIO.output(Led2,GPIO.HIGH) #Led2 on Indicates start capture

    def stop(self,isr):
        GPIO.remove_event_detect("P9_26")
        if self.timer.isActive() == True:
            self.timer.stop()
        if self.threadAdc.isRunning() == True:
            self.workerAdc.stopFlag()
            print "isFinished---->" + str(self.threadAdc.isFinished())
            #print "stop imuThread"
        #------------------
 
        print "stop capture"
        self.start_stop_flag = 1    
        GPIO.output(Led2,GPIO.LOW) #Led2 off Indicates stops capture
       
    def exitapp(self,isr):
        print "Exit App"
        GPIO.cleanup()
        GPIO.output(Led1,GPIO.LOW) #Led1 off Indicates thats software it's not running
        if self.threadAdc.isRunning() == True:    
            self.threadAdc.quit()
            print "isFinished---->" + str(self.threadAdc.isFinished())
        QtCore.QCoreApplication.exit(0) # exit app    

    def crearDir(self):
        self.directorioOriginal = os.getcwd()
        carpeta = "Astro/data" 

        directorio = os.path.join(os.pardir, carpeta)
        if not os.path.isdir(directorio):
            os.mkdir(directorio)
        os.chdir(directorio)
    def afunc(self,isr):
        print "Test"
        self.emit(SIGNAL("asignal"))    
        
class WorkerADC(QtCore.QObject):
    def readEcg(self):
        #read Adc
        ecgValue = ADC.read("AIN5") * 1.8 # convierte la lectura a tension
        self.ecgData[0] = "%.3f" % round(ecgValue,3)
        
    def stopFlag(self):
        self.stopflag = 1
        self.timer.stop()
    def exitWorker(self):
        print "-------ExitWorker"
        self.timer.stop()
        self._exit = True   
        return self.exitflag
    def startTimer(self):
        print "Start Timer"
        self.timer.start(2)
        self.stopflag = 0
        self.exitflag = 0
    def setup(self):
        self.stopflag = 0
        self.exitflag = 0
        
        self.ecgdatafile = open("ecgdata.txt", "w")
        self.ecgdatafile.write("Ecg")
        self.ecgdatafile.write("\n")
        self.ecgdatafile.close() #close accel file    
        self.ecgData = []
        
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.readEcg)
        self.timer.start(2) #2 ms -> 500Hz ; 4ms -> 250Hz
    def afunc(self):
        print "Test"
        self.emit(SIGNAL("asignal"))       

if __name__ == "__main__":
    app = QtCore.QCoreApplication(sys.argv)
    micro = MicroGravedadControl()
    QtCore.QObject.connect(micro,SIGNAL("asignal"),micro.startTimer)
    GPIO.add_event_detect("P9_24", GPIO.RISING,callback=micro.afunc, bouncetime=200)
    GPIO.output(Led1,GPIO.HIGH) #Led1 on Indicates thats software it's running
    sys.exit(app.exec_())
