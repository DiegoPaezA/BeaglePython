from PyQt4 import QtGui, QtCore
import sys,os

import Adafruit_BBIO.GPIO as GPIO
from MPUaccel import ReadAccel

GPIO.setup("P9_12", GPIO.IN)
GPIO.setup("P9_14", GPIO.IN)

class MicroGravedad(QtCore.QObject):

    def __init__(self):
        super(MicroGravedad, self).__init__()
        
        # Crear Timer read Imu
        self.timerimu = QtCore.QTimer(self)
        self.timerimu.timeout.connect(self.readImu)
        self.timerimu.setInterval(20) #50Hz -> 20ms
        
        #
        # adding by emitting signal in different thread
        self.thread = QtCore.QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.loop)
        
        GPIO.add_event_detect("P9_12", GPIO.RISING,callback=self.start, bouncetime=100)
        GPIO.add_event_detect("P9_14", GPIO.RISING,callback=self.stop, bouncetime=100)
        
        self.dataread = raw_input("Enter Session Name: ")
        self.crearDir() ## crear directorio
        print "Push Start button"
        
        #Clase leer aceleracion
        self.Imu=ReadAccel()
        self.accel = open("accel.txt", "w")
        self.accel.write("Ax;Ay;Az;")
        self.accel.write("\n")
        self.ite = 0
        
        #self.timerimu.start()

    def start(self,isr): 
        #-----------------------------------
        print "Start Capture"
        self.thread.start() # Worker Thread
        GPIO.remove_event_detect("P9_12")
        #-----------------------------------
        return
    def stop(self,isr): 
        #------------------
        if self.thread.isRunning() == True:
            self.worker.stop()
            self.thread.quit()
            self.thread.wait()
            print "stop Thread"
            #------------------
        print "stop program"
        #---------------------------------------
        if self.timerimu.isActive() == True:
            self.timerimu.stop()
        self.accel.close() #close accel file
        #---------------------------------------
        GPIO.remove_event_detect("P9_14")
        QtCore.QCoreApplication.exit(0) # exit app
        return
    
 
    def readImu(self):
        print "--> ok"
        fax, fay, faz= self.Imu.readAccel()
        ax = "%.4f" % round(fax,4)
        ay = "%.4f" % round(fay,4)
        az = "%.4f" % round(faz,4)
        print "acel x: ", ax, " acel y: ", ay, " acel z: ", az
        self.accel.write(str(ax))
        self.accel.write(";")
        self.accel.write(str(ay))
        self.accel.write(";")
        self.accel.write(str(az))
        self.accel.write(";")
        self.accel.write("\n")
        
        self.ite += 1
        if self.ite == 50:
            print "Read Temperatura"
            self.ite = 0

    def crearDir(self):
        self.directorioOriginal = os.getcwd()
        carpeta = "caza1.0/" +  str(self.dataread)

        directorio = os.path.join(os.pardir, carpeta)
        if not os.path.isdir(directorio):
            os.mkdir(directorio)
        os.chdir(directorio)
        
class Worker(QtCore.QObject):
    def do_stuff_timer(self):
        print "Read Adc"

    def stop(self):
        self._exit = True
        self.timer.stop()

    def loop(self):
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.do_stuff_timer)
        self.timer.start(200)
if __name__ == "__main__":
    
    app = QtCore.QCoreApplication(sys.argv)
    micro = MicroGravedad()
    sys.exit(app.exec_())
