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
        self.imustatusButton.clicked.connect(self.imuStatus)
        self.imustatusButton.setText('Take Position 1')    

        
        self.plotButton.clicked.connect(self.plotGraph)
        self.p =self.plot 
        self.curve1 = self.p.plot()
        self.curve2 = self.p.plot()



                
        # crear timer
        #Creo mi Timer y lo conecto a una funcion
        self.imustimer = QtCore.QTimer()
        QtCore.QObject.connect(self.imustimer, QtCore.SIGNAL("timeout()"), self.imusRead)
        self.imustimer.setInterval(100)
        
        
        #----------------------
        # Configurar Serial
        self.arduino = sc.Serial(port = "/dev/ttyO1", baudrate=115200,timeout = .5)
        self.arduino.close()
        self.arduino.open()
        
        # Inicializar conexion con arduino
        self.initSerial() # verifica la conexion con arduino

        

        
        #variables para leer sensores imus
        self.data1 = [] # lista para verificar la conexion de los sensores
        self.data2 = [] # lista para leer los angulos de los sensores
        self.datoplotpith = []
        self.datoplotroll = []
        
        self.swith = 0 # swith valor actual vs anterior

        self.numSensores = 7
        self.numAngulos = 2 # pith,roll 
        self.totalAngulos = self.numAngulos * self.numSensores # total angulos leidos
        self.sensoresOk = np.array(['$S1O', '$S2O', '$S3O', '$S4O', '$S5O', '$S6O', '$S7O'])
        self.sensoresBad = np.array(['$S1B', '$S2B', '$S3B', '$S4B', '$S5B', '$S6B', '$S7B'])
        
        self.posicionZero = np.zeros((self.numSensores, self.numAngulos))
        self.splitAngulos = np.zeros(self.totalAngulos)
        self.splitAngulosRef1 = np.zeros(self.totalAngulos)
        self.splitAngulosRef2 = np.zeros(self.totalAngulos)
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
                
            #Espera 2 seg y si no recibe nada del arduino ingresa al loop    
            elif off_time >= 2:
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
            # convertir string to float y despues float to int
            self.splitAngulos[i]=int((float(self.splitString[i]))) 
            
        
        # Comparar valores de las referencias
        if self.swith == 2:
            #hacer diferencia de la posicion de referencia vs la actual
            print " "
            print " "
            ref = 7 # +- 7 grados de aceptacion
            kref1 = 0
            kref2 = 0
            for i in range(0,len(self.splitAngulos)):    
                difRef1 = self.splitAngulos[i]-self.splitAngulosRef1[i]
                difRef2 = self.splitAngulos[i]-self.splitAngulosRef2[i]
                #print "Diferencia Ref1: ", difRef1
                
                if (difRef1 > -ref and difRef1 < ref):
                    kref1 += 1
                if (difRef2 > -ref and difRef2 < ref):
                    kref2 += 1        
            
            if kref1 == 14:
                print "Posicion 1 On"
            elif kref2 == 14 :
                print "Posicion 2 On"
                
        #print "Out"
            
            
        
        self.datoplotpith.append(self.splitAngulos[0])
        self.datoplotroll.append((self.splitAngulos[1]))   
           
        
        self.data2 = []
        
    def imuStatus(self):
        # Verificando status de conexion de los sensores
        print "-----in"
        
        if self.swith == 0 :
            for i in range(0,len(self.splitAngulos)):    
                self.splitAngulosRef1[i]=self.splitAngulos[i]
            self.swith = 1
            self.imustatusButton.setText('Take Position 2')

        elif self.swith == 1:
            for i in range(0,len(self.splitAngulos)):    
                self.splitAngulosRef2[i]=self.splitAngulos[i]
            self.swith = 2
            self.imustatusButton.setText('Reset Position')
        elif self.swith == 2:
            self.swith = 0
            self.imustatusButton.setText('Take Position 1')    

            
        
        
        '''
        self.arduino.flushInput()
        self.arduino.write("$$$$")
        time.sleep(.1)
        self.data1.append(self.arduino.readline())
        
        
        self.splitSensores = (self.data1[0].split(","))     #sensores
        # Verificar conexion de los sensores
        for i in range(0,len(self.splitSensores)-1):
            if (self.splitSensores[i] == self.sensoresOk[i]):
                print "Sensor ", i+1, " Conexion Ok!"
            elif (self.splitSensores[i] == self.sensoresBad[i]):
                print "Verificar Conexion del sensor ", i+1             
        self.data1 = [] # resetear data 1
        '''
        
    def plotGraph(self):
        
        print "Plot Graph"
    
        self.curve1.setData(self.datoplotpith,pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w', symbolSize = 2)
        self.curve2.setData(self.datoplotroll,pen=(0,200,200), symbolBrush=(255,0,0), symbolPen='w', symbolSize = 2)

        self.datoplotpith = []
        self.datoplotroll = []
        
        
        