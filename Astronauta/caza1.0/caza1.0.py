from PyQt4 import QtGui, QtCore
import sys,os

import Adafruit_BBIO.GPIO as GPIO
from MPUaccel import ReadAccel

GPIO.setup("P9_12", GPIO.IN)
GPIO.setup("P9_14", GPIO.IN)

class MicroGravedad(QtCore.QObject):

    def __init__(self):
        super(MicroGravedad, self).__init__()
        
        # Crear Timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.ReadImu)
        #self.timer.start(200)
        self.i = 0
        
        #
        # adding by emitting signal in different thread
        self.thread = QtCore.QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.loop)
        
        GPIO.add_event_detect("P9_12", GPIO.RISING,callback=self.start, bouncetime=50)
        GPIO.add_event_detect("P9_14", GPIO.RISING,callback=self.stop, bouncetime=50)
        
        self.dataread = raw_input("Enter Session Name: ")
        self.crearDir() ## crear directorio
        print "Push Start button"


    def start(self,isr): 
        #-----------------------------------
        print "Start Thread"
        self.thread.start() # Worker Thread
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
        QtCore.QCoreApplication.exit(0)
        return
    
    
    def ReadImu(self):
        #print "Leer Imu"
        if self.i == 0:
            #-----------------------------------
            print "Start Thread"
            self.thread.start() # Worker Thread
            #-----------------------------------
        elif self.i == 50:
            #QtCore.QCoreApplication.instance().quit()
            #------------------
            print "stop Thread"
            self.worker.stop()
            self.thread.quit()
            self.thread.wait()
            #------------------
        elif self.i >60:
            print "stop program"
            QtCore.QCoreApplication.exit(0)
            
        self.i += 1

    def crearDir(self):
        self.directorioOriginal = os.getcwd()
        carpeta = "caza1.0/" +  str(self.dataread)

        directorio = os.path.join(os.pardir, carpeta)
        if not os.path.isdir(directorio):
            os.mkdir(directorio)
        os.chdir(directorio)
        
class Worker(QtCore.QObject):
    def do_stuff_timer(self):
        print "Read Accel"
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
    def stop(self):
        self._exit = True
        self.timer.stop()
        self.accel.close()
        

    def loop(self):
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.do_stuff_timer)
        self.timer.start(200)
        
        #Clase leer aceleracion
        self.Imu=ReadAccel()
        self.accel = open("accel.txt", "w")
        self.accel.write("ax;ay;az;")
        self.accel.write("\n")



if __name__ == "__main__":
    
    app = QtCore.QCoreApplication(sys.argv)
    micro = MicroGravedad()
    sys.exit(app.exec_())
