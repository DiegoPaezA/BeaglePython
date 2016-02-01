from PyQt4 import QtGui,QtCore
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

class WorkerImu(QtCore.QThread):
    def __init__(self):
        QtCore.QObject.__init__(self)
        self.stopflag = 0
        self.exitflag = 0
        #Configuration of Accel Sensor
        self.Imu=ReadAccel()
        self.accelfile = open("accel.txt", "w")
        self.accelfile.write("Ax;Ay;Az;")
        self.accelfile.write("\n")
        self.accelfile.close() #close accel file    
        self.data = [0,';',0,';',0,';',"\n"]

        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.readImu)
        
        GPIO.add_event_detect("P9_26", GPIO.RISING,callback=self.exitWorker, bouncetime=200)

        #self.timer.start(20)
    
    def startTimer(self):
        print "Start Timer"
        self.timer.start(500)
        
    def readImu(self):
        fax, fay, faz= self.Imu.readAccel()
        ax = "%.4f" % round(fax,4)
        ay = "%.4f" % round(fay,4)
        az = "%.4f" % round(faz,4)
        print "acel x: ", ax, " acel y: ", ay, " acel z: ", az
        self.data[0] = ax
        self.data[2] = ay
        self.data[4] = az
        x = 0
        for i in self.data:
            #x += 1
            #print x
            if (self.stopflag == 0):
                with open("accel.txt", "a") as self.accelfile:
                    self.accelfile.write(str(i))
                    self.accelfile.flush()
            elif (self.stopflag == 1):
                print "Stop Reading Imu"
                self.exitflag = 1
                self.accelfile.close() #close accel file
                break
                
                #self._exit = True            
    def stopFlag(self):
        self.stopflag = 1
    def exitWorker(self,isr):
        print "-------ExitWorker"
        self.timer.stop()
        self._exit = True
        QtCore.QCoreApplication.exit(0) # exit app  
        #return self.exitflag
    def run(self):
        #self.exec_()
        pass


    def afunc(self,isr):
        print "Test"
        self.emit(SIGNAL("asignal"))


app = QtCore.QCoreApplication(sys.argv)
t = WorkerImu()
t.start()
QtCore.QObject.connect(t,SIGNAL("asignal"),t.startTimer,Qt.QueuedConnection)
GPIO.add_event_detect("P9_24", GPIO.RISING,callback=t.afunc, bouncetime=200)

sys.exit(app.exec_())