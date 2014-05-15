# coding=utf-8
# coding=utf-8

__author__ = 'diegopaez'

import Adafruit_BBIO.UART as UART
import serial as sc
import time 
import numpy as np 
UART.setup("UART1")


arduino = sc.Serial(port = "/dev/ttyO1", baudrate=9600,timeout = .5)
arduino.close()
arduino.open()


#-----
data1 = []
data2 = []
data3 = []
data4 = []


tmp = 1
loopOn = 1
off_time = 0
start_time = time.time()
while loopOn == 1:
    
    print "Waiting For Arduino..."
    line = arduino.readline()
    # print line
    #----------------------------------
    #Calcula intervalo
    loop_time = time.time()
    off_time = loop_time - start_time
    #----------------------------------
    # print off_time
    if line == "$$\n":
        arduino.write("$")
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
            print "$$$$"
            arduino.write("$$$$")
            time.sleep(.1)
            print arduino.readline()
            # data1.append(arduino.readline())

    #    elif user == 2:
    #        print "$CAL"
    #        arduino.flushInput()
    #        arduino.write("$CAL")
    #        time.sleep(.1)
    #        print arduino.readline()
            #data2.append(arduino.readline())

        elif user == 2:
            
            arduino.flushInput()
            arduino.write("$PRI")
            
            data1.append(arduino.readline())
            print "Lectura Ok!"
            
        elif user == 3:
            tmp = 1
            loopOn = 0
    time.sleep(.5)

# print data1, "\n", data2, "\n", data3
print "Fin"

'''
for i in range(0,(len(data3)-1)):
    ((re.split(',', data3[i])))
'''
print data1
np.savetxt('angulos.txt', data1, fmt= '%s')
arduino.close()
