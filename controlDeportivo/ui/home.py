# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtCore, QtGui

from Ui_home import Ui_MainWindow


import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC

import time, math, os, sys
import numpy as np
import datetime
 


Vrr_inicial=np.zeros(50)
Vrr_update = np.zeros(5)

# Inicializar Variables
n = 0 ; i = 0 ; j = 0 ; k = 0;  count = 0;
rr_end=0; rr_value=0; rr_mseg=0;rr_med_temp=0; rr_med_actual=0; bpm=0; rr_med_ant=0 ; bpmt = 0

# Configurar Pines de entrada y salida
GPIO.setup("P9_12", GPIO.IN)

# Configurar ADC 
ADC.setup()
  

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
        self.plotButton.clicked.connect(self.plotGraph) # 
        
        self.totalrr=[]         # dynamic array
        self.rrshot=[]          # dynamic array
        self.shootresult = []     # dynamic array
        self.trigerflag = 0
        self.temporizador = 180 # segundos
        self.tempoProva = [0] 
        self.emgRead = []
        
        self.tiempo = QtCore.QTime() # lector del tiempo actual del sistema
        
        # crear timer Read ADC
        #Creo mi Timer y lo conecto a una funcion
        self.adctimer = QtCore.QTimer()
        QtCore.QObject.connect(self.adctimer, QtCore.SIGNAL("timeout()"), self.readADC)
        self.adctimer.setInterval(4) # Fs= 100Hz = 10ms Fs = 240 Hz = 4.7ms # Fs = 580 Hz = 1.7ms
        
        # crear timer show Tiempo
        #Creo mi Timer y lo conecto a una funcion
        self.showtimer = QtCore.QTimer()
        QtCore.QObject.connect(self.showtimer, QtCore.SIGNAL("timeout()"), self.showTime)
        self.showtimer.setInterval(1000)
        
        #check buttons Activar o desactivar vfc o emg
        self.activarVFC.setChecked(True)
        self.activarEMG.setChecked(False)
        
        
        #construir grafica
        self.p =self.plot 
        self.curve1 = self.p.plot()
        
    @pyqtSignature("")
    def getRR(self,rrint):  
        global n,i,j,k,rr_start, rr_value, rr_end, rr_mseg, rr_med_actual,rr_med_ant,rr_med_temp, bpm , bpmt

        if (n==0): 
            rr_start = time.time()
            n=1
            print("interrup")
            
        elif (n==1):
            j += 1
            i += 1
            print "Calibrando"
            
            rr_end = time.time()
            rr_value = rr_end - rr_start 
            rr_start = rr_end
            rr_mseg = int(rr_value*1000) # ajuste para presentar en segundos
            
            
            rr_med_temp += rr_mseg
            rr_med_actual = rr_med_temp//j # media
            
            # Filtro ajuste Media Local
            if j==3:
                rr_med_ant = rr_med_actual
                j = 0
                i = 0
                rr_med_actual = 0
                rr_med_temp = 0
                n = 2 # sale de etapa de calibracion
            #-------------------------
            
        elif n == 2:
        
            j += 1
            i += 1
            
            
            rr_end = time.time()
            rr_value = rr_end - rr_start 
            rr_start = rr_end
            
            rr_mseg = int(rr_value*1000) # ajuste para presentar en segundos
            
            
            # print "RR Leido ---> ",rr_mseg 
            
            if rr_mseg > (rr_med_ant + 100):
                #  print "--------- rr Descartado"
                rr_med_actual = 0
                rr_med_temp = 0
                j = 0
                i = 0
            elif rr_mseg < (rr_med_ant - 100):
                #  print "--------- rr Descartado"
                rr_med_actual = 0
                rr_med_temp = 0
                j = 0
                i = 0
            else:    
                
                #  print rr_med_ant
                rr_med_temp += rr_mseg
                rr_med_actual = rr_med_temp//j # media
                
                
                # Filtro ajuste Media Local
                if j==3:
                  rr_med_ant = rr_med_actual
                  j = 0
                  rr_med_actual = 0
                  rr_med_temp = 0
                 #-------------------------
            
                bpmt += rr_value
                # --------------------------
                # Calculo bpm
                if i==5:
                    bpm = int(60/(bpmt / 5))
                    i = 0         
                    bpmt = 0
                # -----------------------
                #print "rr_mseg ---> ", rr_mseg
                
                self.totalrr.append(rr_mseg) # crear vector con intervalos rr
            
                if self.trigerflag == 1:            
                    self.rrshot.append(rr_mseg) # crear vector con intervalos rr del tiro
                
                self.labelintervaloRR.setText('')
                self.labelbpsout.setText('')
                time.sleep(0.01)
                self.labelbpsout.setText(str(bpm))
                self.labelintervaloRR.setText(str(rr_mseg))
                
                
        return  
    
    @pyqtSignature("") # Funcion boton start captura
    def on_ButtonStart_released(self):
        """
        Slot documentation goes here.
        """
        global n, j, i
        n = 0; j = 0; i = 0
        
        print "Start captura"
        #inicializar thread de interrupcion
        GPIO.add_event_detect("P9_12", GPIO.RISING,callback=self.getRR, bouncetime=100)
        self.adctimer.start() # Start timer Read adc    
        self.showtimer.start() # Start timer mostrar tiempo
        self.curve1.clear() # clear grafico
        self.tempoProva[0] = 0
        
        
        
        
    @pyqtSignature("") # Funcion boton stop captura
    def on_ButtonStop_released(self):
        """
        Slot documentation goes here.
        """
        print "stop capture"
        
        GPIO.remove_event_detect("P9_12")
        
        # Guardar archivo con los datos adquiridos
        horaActual = str(datetime.datetime.now())
        
        np.savetxt('rr' + str(self.dataread) + horaActual + '.txt', self.totalrr, fmt='%i') # salvar archivo rr total
        np.savetxt('Emg' + str(self.dataread) + horaActual + '.txt', self.emgRead, fmt='%10.4f') # salvar archivo emg
        
        
        if self.shootresult != []:
            np.savetxt('resultado' + str(self.dataread) + horaActual + '.txt', self.shootresult, fmt='%i') # salvar resultado
        
        self.totalrr = []       # clear total rr
        self.shootresult = []   # clear resultado
        
        
        self.ButtonStart.setEnabled(False)
        self.ButtonStop.setEnabled(False)
        self.ButtonTrigeron.setEnabled(False)
        self.Readtext.clear()  
        self.Readtext.setEnabled(True)
        
        self.adctimer.stop() # parar timer
        self.showtimer.stop() # parar Timer
        self.curve1.setData(self.emgRead) # graficar curva emg
        self.emgRead = []
        
        np.savetxt('tempoProvaSeg' + str(self.dataread) + horaActual + '.txt', self.tempoProva, fmt='%i') # salvar tiempo de prueba
        

    
    @pyqtSignature("")
    def on_ButtonTrigeron_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.trigerflag == 0: # inicia la captura del tiro
                self.trigerflag = 1
                self.ButtonTrigeron.setText('Triger Shot Stop')
                self.ButtonStop.setEnabled(False)
                print "Triger Shot Start"
                
        elif self.trigerflag == 1: # salva el archivo con los datos capturados
                self.trigerflag = 0
                
                text, ok = QtGui.QInputDialog.getText(self, 'Resultado', 'Insira o Resultado:')
                if ok:
                    self.readResultado.setText(str(text))
                    self.shootresult.append(int(str(text)))
                
                horaActual = str(datetime.datetime.now())
                np.savetxt('shot' + str(self.dataread) + horaActual + '.txt', self.rrshot,fmt='%i')
                self.rrshot = [] # clear rrshot para el proximo shoot
                
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
    
    def showTime(self):
    #Show Current Time in "hh:mm:ss" format
        b = self.tiempo.currentTime().toString(str("hh:mm:ss"))
 
        # print('%02d:%02d' % (minutes, seconds))
        
        # tiempo prueba
        
        minutesP = int(self.tempoProva[0]/60)
        secondsP = int(self.tempoProva[0]%60)
          
        #print('%02d:%02d' % (minutesP, secondsP))
        
        
        self.tempoProva[0] += 1
        
        if self.temporizador != 0 :
            #temporizador 
            minutes = int(self.temporizador/60)
            seconds = int(self.temporizador%60)
            self.temporizador -= 1
            self.relojout.setText('%02d:%02d' % (minutes, seconds))
            
        elif self.temporizador == 0 :
            self.relojout.setText('Start T')
            
        self.tempoProvaout.setText('%02d:%02d' % (minutesP, secondsP))

    
    def readADC(self):
        #read Adc
        value = ADC.read("P9_33")
        self.emgRead.append(value)
        
    def plotGraph(self):

        if self.plotEMG.isChecked() : 
            print "plot emg"
        elif self.plotVFC.isChecked() :
            print "plot VFC"    

        

