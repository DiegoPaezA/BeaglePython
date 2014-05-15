# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtCore, QtGui
import sys, time


import numpy as np
import Adafruit_BBIO.UART as UART
import serial as sc

from Ui_home import Ui_MainWindow



UART.setup("UART1")



class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.setWindowTitle("Interface de Control")
        self.center() # Centra la ventana en la pantalla
        
        #self.buttongo.clicked.connect(self.enablebuttons)
        self.ButtonStart.clicked.connect(self.start)
        self.ButtonStop.clicked.connect(self.stop)
                
        # crear timer
        #Creo mi Timer y lo conecto a una funcion
        self.imustimer = QtCore.QTimer()
        QtCore.QObject.connect(self.imustimer, QtCore.SIGNAL("timeout()"), self.imusRead)
        self.imustimer.setInterval(250)
        
        
        #----------------------
        # Configurar Serial
        self.arduino = sc.Serial(port = "/dev/ttyO1", baudrate=9600,timeout = .5)
        self.arduino.close()
        self.arduino.open()
        
        # Inicializar conexion con arduino
        self.initSerial() # verifica la conexion con arduino

        

        
        #variables para leer sensores imus
        self.data1 = [] # lista para verificar la conexion de los sensores
        self.data2 = [] # lista para leer los angulos de los sensores
        
        self.numSensores = 7
        self.numAngulos = 4 # w,x,y,z 
        self.totalAngulos = self.numAngulos * self.numSensores # total angulos leidos
        self.sensoresOk = np.array(['$S1O', '$S2O', '$S3O', '$S4O', '$S5O', '$S6O', '$S7O'])
        self.sensoresBad = np.array(['$S1B', '$S2B', '$S3B', '$S4B', '$S5B', '$S6B', '$S7B'])
        
        self.posicionZero = np.zeros((self.numSensores, self.numAngulos))
        self.splitAngulos = np.zeros(self.totalAngulos)
        self.splitSensores = [] # Verificar la conexion de los sensores
       
        
        
        
    # metodo para centrar la ventana en la pantalla
    def initSerial(self):        
        tmp = 1
        loopOn = 1
        off_time = 0
        start_time = time.time()
        while loopOn == 1:
            print "Waiting For Arduino..."
            line = self.arduino.readline()
            # print line
            #----------------------------------
            #Calcula intervalo
            loop_time = time.time()
            off_time = loop_time - start_time
            #----------------------------------
            # print off_time
            if line == "$$\n":
                self.arduino.write("$")
                tmp = 0
                
            #Espera 3 seg y si no recibe nada del arduino ingresa al loop    
            elif off_time >= 3:
                print "Arduino is Runing!"
                tmp = 0
                off_time = 0
                print "Go into it!"
                loopOn = 0
            time.sleep(.5)
            
        
    # metodo Verificar la conexion con el arduino
    def center(self):        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    
    def start(self):
        print "start ok"
        self.imustimer.start() 
            
    def stop(self):
        self.imustimer.stop() 

        print "stop ok"
        

    def imusRead(self):
    #Show Current Time in "hh:mm:ss" format
        self.arduino.flushInput()
        self.arduino.write("$PRI")
            
        self.data2.append(self.arduino.readline())
        time.sleep(0.1)
            
        self.splitString = (self.data2[0].split(",")) #angulos separados por string

        for i in range(0,len(self.splitString)-1):    
            self.splitAngulos[i]=(float(self.splitString[i]))
            
        print "---------------------------------------------------------------"    
        print self.splitAngulos[0], self.splitAngulos[1],self.splitAngulos[2],self.splitAngulos[3]
        print "---------------------------------------------------------------"
        
        self.data2 = []