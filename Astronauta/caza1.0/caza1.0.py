from PyQt4 import QtGui, QtCore
import sys
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


class Worker(QtCore.QObject):
    def do_stuff_timer(self):
        print "Read Accel"
        fax, fay, faz= self.Imu.readAccel()
        print "acel x: ", fax, " acel y: ", fay, " acel z: ", faz 
    def stop(self):
        self._exit = True
        self.timer.stop()

    def loop(self):
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.do_stuff_timer)
        self.timer.start(200)
        
        #Clase leer aceleracion
        self.Imu=ReadAccel()



if __name__ == "__main__":
    
    app = QtCore.QCoreApplication(sys.argv)
    micro = MicroGravedad()
    sys.exit(app.exec_())
