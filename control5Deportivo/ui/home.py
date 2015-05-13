# -*- coding: utf-8 -*-
# controlDeportivo_V4_1
# Software para captura fisiologica, no incluye el procesamiento
# Origem: 1,mayo,2015
# Diego R. Paez Ardila
# Ubicacion: IEB-UFSC - Brasil
# Estatus : Gestion de sesiones por carpetas, update interface lenguage
# Update: 13, mayo, 2015
"""
Module implementing MainWindow.
"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtCore, QtGui

from Ui_home import Ui_MainWindow

import Adafruit_BBIO.GPIO as GPIO
from bbio import *
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.UART as UART
import serial as sc

import time,os
import numpy as np


# Inicializar Variables
n = 0; i = 0; j = 0; k = 0; count = 0;
rr_end=0; rr_value=0; rr_mseg=0;rr_med_temp=0; rr_med_actual=0; bpm=0; rr_med_ant=0 ; bpmt = 0

# Configurar Pines de entrada y salida
GPIO.setup("P9_12", GPIO.IN)
RST = GPIO0_4
pinMode(RST, OUTPUT)

# Configurar ADC y serial
ADC.setup()
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

        self.buttongo.clicked.connect(self.enablebuttons)
        self.plotButton.clicked.connect(self.plotGraph) #
        self.plotButton.setEnabled(False)

        self.resetButton.clicked.connect(self.resetAll) #


        self.pauseEmgButton.clicked.connect(self.pauseEmg) #
        self.savePositionButton.clicked.connect(self.savePosition) #


        self.totalrr=[]         # dynamic array
        self.rrtriger = []
        #self.shootresult = []     # dynamic array
        self.trigerflag = 0
        self.tflag = 0
        self.temporizador = 180 # segundos
        self.tempoProva = [0]
        self.emgRead = []
        self.posicioncounter = 0

        self.tiempo = QtCore.QTime() # lector del tiempo actual del sistema Y vector de tiempo
        self.timeVectorOn = [] #
        self.timeVectorOff = [] #

        # crear timer Read ADC
        #Creo mi Timer y lo conecto a una funcion
        self.adctimer = QtCore.QTimer()
        QtCore.QObject.connect(self.adctimer, QtCore.SIGNAL("timeout()"), self.readADC)
        self.adctimer.setInterval(4) # Fs= 100Hz = 10ms Fs = 250 Hz = 4ms # Fs = 580 Hz = 1.7ms

        # crear timer show Tiempo
        #Creo mi Timer y lo conecto a una funcion
        self.showtimer = QtCore.QTimer()
        QtCore.QObject.connect(self.showtimer, QtCore.SIGNAL("timeout()"), self.showTime)
        self.showtimer.setInterval(1000)

        #check buttons Activar o desactivar vfc o emg
        self.activarVFC.setChecked(False)
        self.activarEMG.setChecked(False)
        self.activarIMUS.setChecked(False)

        #construir grafica
        self.p =self.plot
        self.curve1 = self.p.plot()
        self.curve2 = self.p.plot()

        #-------------------------------------------------------------------------
        #datos iniciales comunicacion Serial
        # crear timer
        #Creo mi Timer y lo conecto a una funcion
        self.imustimer = QtCore.QTimer()
        QtCore.QObject.connect(self.imustimer, QtCore.SIGNAL("timeout()"), self.imusRead)
        self.imustimer.setInterval(20) #40ms -> 25Hz; 20ms -> 50Hz

        #-------------------------------------------------------------------------
        #reset arduino
        self.resetArduino()
        #------------------------------------------------------------------------------
        # Configurar Serial
        self.arduino = sc.Serial(port = "/dev/ttyO1", baudrate=115200,timeout = .5)
        self.arduino.close()
        self.arduino.open()

        #variables para leer sensores imus
        self.data1 = [] # lista para verificar la conexion de los sensores
        self.data2 = [] # lista para leer los angulos de los sensores
        self.datoplotpith = []
        self.datoplotroll = []

        self.posicion1 = False #bandera posiciones
        self.posicion2 = False

        self.swith = 0 # swith referencias
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

        # Inicializar conexion con arduino
        self.initSerial() # verifica la conexion con arduino
# Fin inicializacion del Constructor-------------------------------------------------------------

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
                self.tiempo.restart()  # Reinicia el vector de tiempo cuando se activa la VFC
            #-------------------------
        elif n == 2:

            j += 1
            i += 1
            rr_end = time.time()
            rr_value = rr_end - rr_start
            rr_start = rr_end
            rr_mseg = int(rr_value*1000)  # ajuste para presentar en msegundos
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
                if i==20:
                    bpm = int(60/(bpmt / 20))
                    i = 0
                    bpmt = 0
                # -----------------------
                print "rr_mseg ---> ", rr_mseg

                self.totalrr.append(rr_mseg) # crear vector con intervalos rr

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

        self.tiempo.start() # inicia vector de tiempo para guardar interrupcion de tiro

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

        if self.activarIMUS.isChecked() == True:   # True Activo, False no activo
            self.imustimer.start() # Activar lectura de sensores
            self.savePositionButton.setEnabled(True) #activar boton tomar posicion
            self.imuStatus() # Verificar status de los sensores
        else:
            print "IMUS inactivos"

        if (self.activarVFC.isChecked() == False) and (self.activarEMG.isChecked() == False
                                                       and self.activarIMUS.isChecked() == False):
                print 'activar vfc por defecto'
                self.activarVFC.setChecked(False) # ------------------Revisar
                self.activarEMG.setChecked(False)
                self.activarIMUS.setChecked(False)
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

        #----------------------------VFC-------------------------------------------------------------------------------
        if self.activarVFC.isChecked() == True:  # True Activo, False no activo
            #inicializar thread de interrupcion
            GPIO.remove_event_detect("P9_12")
            np.savetxt('rr' + str(self.dataread) + '.txt', self.totalrr, fmt='%i') # salvar archivo rr total
        else:
            print "VFC inactivo"
        #----------------------------EMG--------------------------------------------------------------------------------
        if self.activarEMG.isChecked() == True:
            self.adctimer.stop() # parar timer
            np.savetxt('Emg' + str(self.dataread) +  '.txt', self.emgRead, fmt='%10.4f') # salvar archivo emg
            self.pauseEmgButton.setEnabled(False) # desactivar boton pause
            self.pauseEmgButton.setText('Pausar Emg')
        else:
            print "EMG Inactivo"
         #----------------------------IMUS--------------------------------------------------------------------------------
        if self.activarIMUS.isChecked() == True:
            self.imustimer.stop() #Desactivar lectura sensores
        else:
            print "EMG Inactivo"
        #---------------------------------------------------------------------------------------------------------------

        if self.timeVectorOn != [] and self.timeVectorOff != []:
            np.savetxt('vectorTOn' + str(self.dataread)+ '.txt', self.timeVectorOn, fmt='%i') # salvar resultado
            np.savetxt('vectorTOff' + str(self.dataread)+ '.txt', self.timeVectorOff, fmt='%i') # salvar resultado

        #self.shootresult = []   # clear resultado

        self.timeVectorOn = []
        self.timeVectorOff = []
        self.posicioncounter = 0 # reiniciar contador de tiros

        self.ButtonStart.setEnabled(False)
        self.ButtonStop.setEnabled(False)
        self.ButtonTrigeron.setEnabled(False)
        self.savePositionButton.setEnabled(False)
        self.Readtext.clear()
        self.Readtext.setEnabled(True)

        self.plotButton.setEnabled(True) # Activa el boton de plot
        self.resetButton.setEnabled(True)
        self.showtimer.stop() # parar Timer
        os.chdir(self.directorioOriginal) # vuelve al directorio inicial

    @pyqtSignature("")
    def on_ButtonTrigeron_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.trigerflag == 0: # inicia la captura del tiro
                self.trigerflag = 1
                self.ButtonTrigeron.setText('Triger Shot Stop')
                self.ButtonStop.setEnabled(False)
                self.timeVectorOn.append(self.tiempo.elapsed()) # Agrega tiempo de elapse al vector de triggers
                print "Triger Shot Start"

        elif self.trigerflag == 1: # salva el archivo con los datos capturados
                self.trigerflag = 0
                self.timeVectorOff.append(self.tiempo.elapsed())
                print "Triger Shot Stop"
                """
                # Desactivar funcion que pide el resultado
                text, ok = QtGui.QInputDialog.getText(self, 'Resultado', 'Insira o Resultado:')
                if ok:
                    if text != "":
                        self.shootresult.append(int(str(text)))
                """
                self.ButtonTrigeron.setText('Triger Shot Start')
                self.ButtonStop.setEnabled(True)


    @pyqtSignature("")
    def enablebuttons(self):

        self.dataread = self.Readtext.text()
        self.crearDir() ## crear directorio
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
        #b = self.tiempo.currentTime().toString(str("hh:mm:ss"))
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
        value = ADC.read("P9_33") * 1.8 # convierte la lectura a tension
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
        n = 0 ; i = 0 ; j = 0 ; k = 0;
        rr_end=0; rr_value=0; rr_mseg=0;rr_med_temp=0;
        rr_med_actual=0; bpm=0; rr_med_ant=0 ; bpmt = 0
        self.temporizador = 180 # segundos
       # Inicializar la comunicacion con el arduino
    def initSerial(self):
        loopOn = 1
        off_time = 0
        start_time = time.time()
        while loopOn == 1:
            print "Waiting For Arduino..."
            line = self.arduino.readline()
            #print line
            #----------------------------------
            #Calcula intervalo
            loop_time = time.time()
            off_time = loop_time - start_time
            #----------------------------------
            # print off_time
            if line == "$$\n":
                self.arduino.write("$")
                self.arduinoLabel.setText("Arduino rst Ok!")
                print "rst OK!!"
                print "Go into it!"
                loopOn = 0

            #Espera 2 seg y si no recibe nada del arduino ingresa al loop
            elif off_time >= 2:
                print "Arduino is Runing!"
                print "Go into it!"
                self.arduinoLabel.setText("Arduino Ok!")
                loopOn = 0
            time.sleep(.5)

    def imusRead(self):
        # realiza lectura de los sensores
        self.arduino.flushInput()
        self.arduino.write("$PRI")

        self.data2.append(self.arduino.readline())
        self.splitString = (self.data2[0].split(",")) #angulos separados por string
        for i in range(0,len(self.splitString)-1):
            # convertir string to float y despues float to int
            self.splitAngulos[i]=int((float(self.splitString[i])))
        self.data2 = []

    def imuStatus(self):
        self.arduino.flushInput() # Limpia el puerto serial
        self.arduino.write("$$$$") # imprime el comando verificacion de status
        time.sleep(.1)
        self.data1.append(self.arduino.readline()) # lee la linea de datos
        self.splitSensores = (self.data1[0].split(","))     #sensores
        # Verificar conexion de los sensores
        for i in range(0,len(self.splitSensores)-1):
            if (self.splitSensores[i] == self.sensoresOk[i]):
                print "Sensor ", i+1, " Conexion Ok!"
            elif (self.splitSensores[i] == self.sensoresBad[i]):
                print "Verificar Conexion del sensor ", i+1
        self.data1 = [] # resetear data 1

    def savePosition(self):
        print "save position"
        self.posicioncounter += 1
        np.savetxt('position' + str(self.dataread) + "_" +str(self.posicioncounter)+ '.txt', self.splitAngulos, fmt='%i') # salvar archivo rr total


    def resetArduino(self):
        #---Reset Arduino
        digitalWrite(RST, HIGH)
        time.sleep(1)
        digitalWrite(RST, LOW)
        time.sleep(1)
        print "Wait 8 Seg Until Reset"
        print ""
        time.sleep(8) #wait until reset

    def crearDir(self):
        self.directorioOriginal = os.getcwd()
        carpeta = "control4Deportivo/" +  str(self.dataread)

        directorio = os.path.join(os.pardir, carpeta)
        if not os.path.isdir(directorio):
            os.mkdir(directorio)
        os.chdir(directorio)

