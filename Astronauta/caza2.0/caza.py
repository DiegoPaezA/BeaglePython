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
        
        # Thread Accel + Temp
        self.threadImu = QtCore.QThread() 
        self.workerImu = WorkerImu()      
        self.workerImu.moveToThread(self.threadImu) 
        self.threadImu.started.connect(self.workerImu.setup)
        QtCore.QObject.connect(self.workerImu,SIGNAL("asignal"),self.workerImu.startTimer)
        
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
            self.crearDir() ## crear directorio
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
        rootDir = "/home/BeaglePython/Astronauta/caza2.0/"
        stackFolders = []
        
        for dirName, subdirList, fileList in os.walk(rootDir):
            stackFolders.append(dirName)
        numFolder = len(stackFolders)
        folderName = "data_" + str(numFolder)
        folder = "/home/BeaglePython/Astronauta/caza2.0/" + str(folderName) 
        directory = os.path.join(os.pardir, folder)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        os.chdir(directory)
    def afunc(self,isr):
        print "Test"
        self.emit(SIGNAL("asignal"))    


class WorkerImu(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
        self.stopflag = 0
        self.exitflag = 0
        self.counter = 0
        
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
                with open("accel.txt", "a") as self.accelfile:
                    self.accelfile.write(str(i))
                    self.accelfile.flush()
            elif (self.stopflag == 1):
                print "Stop Reading Imu"
                self.exitflag = 1
                self.accelfile.close() #close accel file
                self.timer.stop()
                break
        self.counter += 1

        if self.counter == 50:
            #1Hz -> cada 1seg almacena temperatura
            self.counter = 0
            self.bmpData[0] = "%.2f" % round(self.sensorTemp.read_temperature(),2)
            self.bmpData[2] = "%.2f" % round(self.sensorTemp.read_pressure(),2)
            self.bmpData[4] = "%.2f" % round(self.sensorTemp.read_altitude(),2)
            self.bmpData[6] = "%.2f" % round(self.sensorTemp.read_sealevel_pressure(),2) 
            #print "Running... Accel + Temp"
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
                    break   
    def stopFlag(self):
        self.stopflag = 1
    def startTimer(self):
        print "Start Timer"
        self.timer.start(20)
        self.stopflag = 0
        self.exitflag = 0
    def setup(self):
        #Configuration of Accel Sensor
        self.Imu=ReadAccel(address=0x68,i2c_bus = 1, Arange =4)
        self.accelfile = open("accel.txt", "w")
        self.accelfile.write("Ax;Ay;Az;")
        self.accelfile.write("\n")
        self.accelfile.close() #close accel file    
        self.data = [0,';',0,';',0,';',"\n"]
        
        self.sensorTemp = BMP085.BMP085()
        self.bmpdatafile = open("bmpdata.txt", "w")
        self.bmpdatafile.write("Temp;Pressure;Altitude;seaLevelP;")
        self.bmpdatafile.write("\n")
        self.bmpdatafile.close() #close accel file    
        self.bmpData = [0,';',0,';',0,';',0,';',"\n"]

        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.readImu)
        self.timer.start(20)


        
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
