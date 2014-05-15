# -*- coding: utf-8 -*-
# controlDeportivo_V2_
# Software para captura fisiologica, no incluye el procesamiento
# update 16,marzo,2015
# Diego R. Paez Ardila
# Ubicacion: IEB-UFSC - Brasil
# Estatus : evolucion a version 3, donde se incluira el modulo
#           de movimiento y procesamento de las señales adquiridas
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
        self.plotButton.setEnabled(False)
        
        self.resetButton.clicked.connect(self.resetAll) #
        
        
        self.pauseEmgButton.clicked.connect(self.pauseEmg) #
        
        
        self.totalrr=[]         # dynamic array
        self.rrtriger = []
        self.shootresult = []     # dynamic array
        self.trigerflag = 0
        self.tflag = 0
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
        self.curve2 = self.p.plot()

        
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
            
            if rr_mseg > (rr_med_ant + 200):
                rr_med_actual = 0
                rr_med_temp = 0
                j = 0
                i = 0
            elif rr_mseg < (rr_med_ant - 200):
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
                if i==3:
                    bpm = int(60/(bpmt / 3))
                    i = 0         
                    bpmt = 0
                # -----------------------
                print "rr_mseg ---> ", rr_mseg
                
                self.totalrr.append(rr_mseg) # crear vector con intervalos rr
                self.rrtriger.append(rr_mseg) # crear vector con intervalos + triger 1
                
                #if self.trigerflag == 1:            
                #    self.rrshot.append(rr_mseg) # crear vector con intervalos rr del tiro
                
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
        #global n, j, i
        self.resetAll()
        self.resetButton.setEnabled(False)
        
        if self.activarVFC.isChecked() == True:  # True Activo, False no activo
            #inicializar thread de interrupcion
            GPIO.add_event_detect("P9_12", GPIO.RISING,callback=self.getRR, bouncetime=100)
        else:
            print "VFC inactivo"
                
        if self.activarEMG.isChecked() == True:   # True Activo, False no activo
            self.adctimer.start() # Start timer Read adc
            self.pauseEmgButton.setEnabled(True) # activa boton de pause emg
        else:
            print "EMG inactivo"    
        
        if (self.activarVFC.isChecked() == False) and (self.activarEMG.isChecked() == False):
                print 'activar vfc por defecto'
                self.activarVFC.setChecked(True)
                self.activarEMG.setChecked(False)
                
                GPIO.add_event_detect("P9_12", GPIO.RISING,callback=self.getRR, bouncetime=100)
            
        print "Start captura"
        
        self.showtimer.start() # Start timer mostrar tiempo
        self.curve1.clear() # clear grafico
        self.curve2.clear() # clear grafico
        self.tempoProva[0] = 0
        
        # clear emg & vfc
        self.totalrr = []       # clear total 
        self.rrtriger = []
        self.emgRead = []       # clear total
        
        self.plotButton.setEnabled(False) # desactiva el boton de plot
        self.ButtonStart.setEnabled(False) # desactiva boton start
        
        
        
        
    @pyqtSignature("") # Funcion boton stop captura
    def on_ButtonStop_released(self):
        """
        Slot documentation goes here.
        """
        print "stop capture"
        
        
        horaActual = str(datetime.datetime.now())
        
        #----------------------------VFC-------------------------------------------------------------------------------
        if self.activarVFC.isChecked() == True:  # True Activo, False no activo
            #inicializar thread de interrupcion
            GPIO.remove_event_detect("P9_12")
            np.savetxt('rr' + str(self.dataread) + horaActual + '.txt', self.totalrr, fmt='%i') # salvar archivo rr total
            if self.tflag == 1:
                np.savetxt('rrtriger' + str(self.dataread) + horaActual + '.txt', self.rrtriger, fmt='%i') # salvar archivo rr total
                        
        else:
            print "VFC inactivo"
            
        #----------------------------EMG--------------------------------------------------------------------------------
        if self.activarEMG.isChecked() == True: 
            self.adctimer.stop() # parar timer 
            np.savetxt('Emg' + str(self.dataread) + horaActual + '.txt', self.emgRead, fmt='%10.4f') # salvar archivo emg
            self.pauseEmgButton.setEnabled(False) # desactivar boton pause
            self.pauseEmgButton.setText('Pausar Emg')
        else:
            print "EMG Inactivo"
        #---------------------------------------------------------------------------------------------------------------
        
        if self.shootresult != []:
            np.savetxt('resultado' + str(self.dataread) + horaActual + '.txt', self.shootresult, fmt='%i') # salvar resultado
        
        self.shootresult = []   # clear resultado
        
        
        self.ButtonStart.setEnabled(False)
        self.ButtonStop.setEnabled(False)
        self.ButtonTrigeron.setEnabled(False)
        self.Readtext.clear()  
        self.Readtext.setEnabled(True)
        
        self.plotButton.setEnabled(True) # Activa el boton de plot
        self.resetButton.setEnabled(True)
        self.showtimer.stop() # parar Timer
        np.savetxt('tempoProvaSeg' + str(self.dataread) + horaActual + '.txt', self.tempoProva, fmt='%i') # salvar tiempo de prueba
        

    
    @pyqtSignature("")
    def on_ButtonTrigeron_clicked(self):
        """
        Slot documentation goes here.
        """
        self.tflag = 1 # triger fue ejecutado, salvar archivos
        
        if self.trigerflag == 0: # inicia la captura del tiro
                self.trigerflag = 1
                self.ButtonTrigeron.setText('Triger Shot Stop')
                self.ButtonStop.setEnabled(False)
                self.emgRead.append(1) # agrego marcador al vector de emg
                self.rrtriger.append(1) # agrego marcador al vector de emg
                print "Triger Shot Start"
                
        elif self.trigerflag == 1: # salva el archivo con los datos capturados
                self.trigerflag = 0
                
                self.emgRead.append(1) # agrego marcador al vector de emg
                self.rrtriger.append(1) # agrego marcador al vector de vfc triger
                print "Triger Shot Stop"
                
                self.ButtonTrigeron.setText('Triger Shot Start')
                
                text, ok = QtGui.QInputDialog.getText(self, 'Resultado', 'Insira o Resultado:')
                if ok:
                    self.shootresult.append(int(str(text)))
                
                self.emgRead.append(1) # agrego marcador al vector de emg
                self.rrtriger.append(1) # agrego marcador al vector de vfc triger
                
                self.ButtonTrigeron.setText('Triger Shot Start')
                self.ButtonStop.setEnabled(True)
                

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
        value = ADC.read("P9_33") * 1.8
        self.emgRead.append(value)
        
    def plotGraph(self):

        if self.plotEMG.isChecked() : 
            print "plot emg"
            self.curve2.clear()
            if self.emgRead != []: # si hay nada almacenado en emgRead no graficar
                self.p.setXRange(0, len(self.emgRead) + 1)
                self.p.setYRange(np.amin(self.emgRead), np.amax(self.emgRead))
                self.curve2.setData(self.emgRead) # graficar curva emg
            
        elif self.plotVFC.isChecked() :
            print "plot VFC"
            self.curve1.clear()
            if self.totalrr != []: # si hay nada almacenado en emgRead no graficar
                self.p.setXRange(0, len(self.totalrr) + 1)
                self.p.setYRange(np.amin(self.totalrr) - 50, np.amax(self.totalrr) + 50)
                self.curve1.setData(self.totalrr,pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w', symbolSize = 4) # graficar curva emg
            
            
    def pauseEmg(self):
        #Pausar captura EMG
        if self.adctimer.isActive() == True:
            self.adctimer.stop()
            self.pauseEmgButton.setText('Ativar Emg')
            
        elif self.adctimer.isActive() == False:
            self.adctimer.start()
            self.pauseEmgButton.setText('Pausar Emg')
        
    def resetAll(self):
        global n,i,j,k,rr_start, rr_value, rr_end, rr_mseg, rr_med_actual,rr_med_ant,rr_med_temp, bpm , bpmt

        
        # reset all Variables
        n = 0 ; i = 0 ; j = 0 ; k = 0;  count = 0;
        rr_end=0; rr_value=0; rr_mseg=0;rr_med_temp=0;
        rr_med_actual=0; bpm=0; rr_med_ant=0 ; bpmt = 0
        self.temporizador = 180 # segundos



