# coding=utf-8
# coding=utf-8

__author__ = 'diegopaez'

import Adafruit_BBIO.UART as UART
from bbio import *
import serial as sc
import time 
import numpy as np


RST = GPIO0_4
pinMode(RST, OUTPUT)
#---Reset Arduino
digitalWrite(RST, HIGH)
time.sleep(1)
digitalWrite(RST, LOW)
time.sleep(1)
print "Wait 8 Seg Until Reset"
time.sleep(8) #wait until reset


UART.setup("UART1")
arduino = sc.Serial(port = "/dev/ttyO1", baudrate=115200,timeout = .5)
arduino.close()
arduino.open()

    
#-----
data1 = []
data2 = []
data3 = []
data4 = []

numSensores = 7
numAngulos = 4 # w,x,y,z 
totalAngulos = numAngulos * numSensores # total angulos leidos
sensoresOk = np.array(['$S1O', '$S2O', '$S3O', '$S4O', '$S5O', '$S6O', '$S7O'])
sensoresBad = np.array(['$S1B', '$S2B', '$S3B', '$S4B', '$S5B', '$S6B', '$S7B'])

posicionZero = np.zeros((numSensores, numAngulos))
splitAngulos = np.zeros(totalAngulos)
splitSensores = [] # Verificar la conexion de los sensores


tmp = 1
loopOn = 1
off_time = 0
start_time = time.time()
while loopOn == 1:
    
    #print "Waiting For Arduino..."
    line = arduino.readline()
    print line
    #----------------------------------
    #Calcula intervalo
    loop_time = time.time()
    off_time = loop_time - start_time
    #----------------------------------
    # print off_time
    if line == "$$\n":
        arduino.write("$")
        print "Arduino Reset Ok!!"
        tmp = 0
        
    #Espera 3 seg y si no recibe nada del arduino ingresa al loop    
    elif off_time >= 3:
        print "Arduino is Runing!"
        tmp = 0
        off_time = 0
        print "Go into it!"


    while tmp == 0:
        
        user = int(raw_input("Ingrese 1 para Validar Conexion o 2 Leer Angulos : "))
        if user == 1:
            arduino.flushInput()
            arduino.write("$$$$")
            time.sleep(.1)
            data1.append(arduino.readline())
            splitSensores = (data1[0].split(","))     #sensores
            # Verificar conexion de los sensores
            for i in range(0,len(splitSensores)-1):
                if (splitSensores[i] == sensoresOk[i]):
                    print "Sensor ", i+1, " Conexion Ok!"
                elif (splitSensores[i] == sensoresBad[i]):
                    print "Verificar Conexion del sensor ", i+1             
            data1 = [] # resetear data 1 

        elif user == 2:
            
            arduino.flushInput()
            arduino.write("$PRI")
            
            data2.append(arduino.readline())
            
            splitString = (data2[0].split(",")) #angulos separados por string

            for i in range(0,len(splitString)-1):    
                splitAngulos[i]=(float(splitString[i]))
            print "Lectura Ok!"
            
            
        elif user == 3:
            tmp = 1
            loopOn = 0
    time.sleep(.5)

# print data1, "\n", data2, "\n", data3
print "Fin"

#print splitAngulos
#np.savetxt('angulos.txt', splitAngulos, fmt= '%10.4f')
arduino.close()
