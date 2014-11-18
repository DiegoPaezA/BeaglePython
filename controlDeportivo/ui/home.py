# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtCore, QtGui

from Ui_home import Ui_MainWindow


import Adafruit_BBIO.GPIO as GPIO
import time, math, os
import numpy as np
import datetime
 


Vrr_inicial=np.zeros(50)
Vrr_update = np.zeros(5)

# Inicializar Variables
n = 0 ; i = 0 ; j = 0 ; k = 0;  count = 0;
rr_end=0; rr_value=0; rr_mseg=0; rr_med=0; bpm=0; rr_medt=0 ; bpmt = 0

# Configurar Pines de entrada y salida
GPIO.setup("P9_12", GPIO.IN)

  
#GPIO.add_event_detect("P9_12", GPIO.RISING,callback=getRR, bouncetime=50)

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
        
        self.buttongo.clicked.connect(self.enablebuttons)
        
        
        self.totalrr=[]         # dynamic array
        self.rrshot=[]          # dynamic array
        self.shootresult=[]          # dynamic array
        self.trigerflag = 0    
    
    def getRR(self,rrint):  
        global n,i,j,k,rr_start, rr_value, rr_end, rr_mseg, rr_med,rr_medt, bpm , bpmt

        if (n==0): 
            rr_start = time.time()
            n=1
            print("interrup")
            
        elif (n==1):
            j += 1
            i += 1
            
            rr_end = time.time()
            rr_value = rr_end - rr_start 
            rr_start=rr_end
            rr_mseg = int(rr_value*1000) # ajuste para presentar en segundos
            
            
            rr_med += rr_mseg
            bpmt += rr_value
            
            if i==3:
               bpm = int(60/(bpmt / 3))
               i = 0
               bpmt = 0
               
            print ("rr_value Time: ", rr_mseg)
            
            # -----------------------
            # Filtro ajuste Media Local
            #if j==3:
            #    rr_medt = rr_med/3
            #    j = 0
            #    rr_med = 0
            #-------------------------    
            #if rr_mseg > rr_medt + 200:
            #    n = 0
            #    rr_mseg = rr_medt
            #-------------------------    
            
            
            self.totalrr.append(rr_mseg) # crear vector con intervalos rr
            
            if self.trigerflag == 1:            
                self.rrshot.append(rr_mseg) # crear vector con intervalos rr del tiro

            

            self.labelintervaloRR.setText('')
            self.labelbpsout.setText('')
            time.sleep(0.01)
            self.labelbpsout.setText(str(bpm))
            self.labelintervaloRR.setText(str(rr_mseg))
        return  
    
    @pyqtSignature("")
    def on_ButtonStart_released(self):
        """
        Slot documentation goes here.
        """
        print "Start captura"
        GPIO.add_event_detect("P9_12", GPIO.RISING,callback=self.getRR, bouncetime=50)
        global n , j
        n = 0
        j = 0
        
    @pyqtSignature("")
    def on_ButtonStop_released(self):
        """
        Slot documentation goes here.
        """
        print "stop capture"
        GPIO.remove_event_detect("P9_12")
        
        # Guardar archivo con los datos adquiridos
        horaActual = str(datetime.datetime.now())
        np.savetxt('rr' + str(self.dataread) + horaActual + '.txt', self.totalrr, fmt='%i')
        
        np.savetxt('resultado' + str(self.dataread) + horaActual + '.txt', self.shootresult, fmt='%i')
        
        self.totalrr = [] # clear total rr
        self.shootresult = [] # clear resultado
        
        self.ButtonStart.setEnabled(False)
        self.ButtonStop.setEnabled(False)
        self.ButtonTrigeron.setEnabled(False)
        self.Readtext.clear()  
        self.Readtext.setEnabled(True)
        
        

    
    @pyqtSignature("")
    def on_ButtonTrigeron_clicked(self):
        """
        Slot documentation goes here.
        """
        
        
        if self.trigerflag == 0: # inicia la captura
                self.trigerflag = 1
                self.ButtonTrigeron.setText('Triger Shot Stop')
                self.ButtonStop.setEnabled(False)
                #self.readResultado.setEnabled(True)
                print "Triger Shot Start"
                
        elif self.trigerflag == 1: # salva el archivo con los datos capturados
                self.trigerflag = 0
                
                text, ok = QtGui.QInputDialog.getText(self, 'Resultado', 'Insira o Resultado:')
                if ok:
                    self.readResultado.setText(str(text))
                    self.shootresult.append(int(str(text)))
                
                horaActual = str(datetime.datetime.now())
                np.savetxt('rrshot' + str(self.dataread) + horaActual + '.txt', self.rrshot,fmt='%i')

                self.rrshot = [] # clear total rr
                

                self.ButtonTrigeron.setText('Triger Shot Start')
                self.ButtonStop.setEnabled(True)

                print "Triger Shot Stop"
                
               
        
    @pyqtSignature("")    
    def enablebuttons(self):
        
        self.dataread = self.Readtext.text()
        
        if self.dataread == "":
            print "Ingrese el nombre y numero de la prueba test1"
            msgBox = QtGui.QMessageBox()
            msgBox.setText('  Insira o Nome + Numero do Teste.  ')
            msgBox.setInformativeText("       Exemplo: teste1hiago ")
            msgBox.setWindowTitle ('Warning!')
            msgBox.addButton(QtGui.QPushButton('Ok'), QtGui.QMessageBox.AcceptRole)
            ret = msgBox.exec_();
        else:
            print "habilite los botones"
            self.ButtonStart.setEnabled(True)
            self.ButtonStop.setEnabled(True)
            self.ButtonTrigeron.setEnabled(True)
              
            self.Readtext.setEnabled(False)
            
            
      # metodo para centrar la ventana en la pantalla
    def center(self):        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())        
    
