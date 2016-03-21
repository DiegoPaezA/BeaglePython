# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
import sys,os,time
import numpy as np

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

        #print "Qthread Number: " + str(QtCore.QThread.idealThreadCount())
        # Thread Accel
        self.threadImu = QtCore.QThread()
        self.workerImu = WorkerImu()
        self.workerImu.moveToThread(self.threadImu)
        self.threadImu.started.connect(self.workerImu.setup)
        QtCore.QObject.connect(self.workerImu,SIGNAL("asignal"),self.workerImu.startTimer)


        self.crearDir() ## crear directorio
        print "Push Start Button"


        GPIO.add_event_detect("P9_26", GPIO.RISING,callback=self.stop, bouncetime=200)
        GPIO.add_event_detect("P9_30", GPIO.RISING,callback=self.exitapp, bouncetime=200)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.readEcg)

        self.start_stop_flag = 0
        self.controlTimer = 0
        self.buffer30seg = 7500
        self.ecgDataBuffer = np.zeros(self.buffer30seg)
        self.counterEcg = 0
    def readEcg(self):
        #print "Timer Workig"
        ecgValue = "%.3f" % round((ADC.read("AIN5") * 1.8),3) # convierte la lectura a tension
        self.ecgDataBuffer[self.counterEcg] = ecgValue
        self.counterEcg += 1
        if self.counterEcg == self.buffer30seg:
            self.ecgData = self.ecgDataBuffer
            self.counterEcg =0
            self.saveDataEcg() #pass Data to a file

    def saveDataEcg(self):
        for i in self.ecgData:
            with open("ecgdata.txt", "a") as self.ecgdatafile:
                self.ecgdatafile.write(str(i)+"\n")
                self.ecgdatafile.flush()
        print "Saved ..."

    def startTimer(self):
        print "Running..."
        if self.controlTimer == 0:
            self.ecgdatafile = open("ecgdata.txt", "w")
            self.ecgdatafile.write("Ecg\n")
            self.timer.start(4) #500Hz
            self.threadImu.start() # Worker Thread setup start
            self.controlTimer=1
        elif self.controlTimer == 1:
            self.timer.start(4) #500Hz
            self.workerImu.afunc()
        if self.start_stop_flag == 1:
            GPIO.add_event_detect("P9_26", GPIO.RISING,callback=self.stop, bouncetime=200)
        self.start_stop_flag = 0
        GPIO.output(Led2,GPIO.HIGH) #Led2 on Indicates start capture


    def stop(self,isr):
        GPIO.remove_event_detect("P9_26")

        if self.timer.isActive() == True:
            self.timer.stop()

        if self.threadImu.isRunning() == True:
            self.workerImu.stopFlag()
            #self.threadImu.wait()
            print "isFinished---->" + str(self.threadImu.isFinished())
            #print "stop imuThread"
        #------------------
        print "stop capture"
        #if self.start_stop_flag == 0:
        #    GPIO.add_event_detect("P9_24", GPIO.RISING,callback=self.start, bouncetime=200)
        self.start_stop_flag = 1
        GPIO.output(Led2,GPIO.LOW) #Led2 off Indicates stops capture

    def exitapp(self,isr):
        print "Exit App"
        GPIO.cleanup()
        GPIO.output(Led1,GPIO.LOW) #Led1 off Indicates thats software it's not running
        if self.threadImu.isRunning() == True:
            self.threadImu.quit()
            print "isFinished---->" + str(self.threadImu.isFinished())
        QtCore.QCoreApplication.exit(0) # exit app

    def crearDir(self):
        self.directorioOriginal = os.getcwd()
        carpeta = "/home/BeaglePython/Astronauta/caza2.0/data"
        directorio = os.path.join(os.pardir, carpeta)
        if not os.path.isdir(directorio):
            os.mkdir(directorio)
        os.chdir(directorio)
    def afunc(self,isr):
        print "Test"
        self.emit(SIGNAL("asignal"))


class WorkerImu(QtCore.QObject):

if __name__ == "__main__":
    app = QtCore.QCoreApplication(sys.argv)
    micro = MicroGravedadControl()
    QtCore.QObject.connect(micro,SIGNAL("asignal"),micro.startTimer)
    GPIO.add_event_detect("P9_24", GPIO.RISING,callback=micro.afunc, bouncetime=200)
    GPIO.output(Led1,GPIO.HIGH) #Led1 on Indicates thats software it's running
    sys.exit(app.exec_())
