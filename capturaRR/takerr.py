#!/usr/bin/python
#-----------------------------------------------------------------------------------------
#  Este Software captura las interrupciones obtenidas 
#  a partir de los picos RR, Calcula la variabilidad del ritmo cardiaco, 
#  haciendo la diferencia entre el tiempo entre interrupciones. 
#   
#   @Author : Diego R. Paez A. 
#   Date      : 13/05/2014
#   Update    : 14/05/2014
#   Place     : UFSC - Brasil
#   Version   : 0.1v
#   Stage     : Production
#   Funtion   : RRCaputre


# Librerias Necesarias 
# Adafruit_BBIO.GPIO as GPIO
# time
# numpy 
#
# Falta 
#-----------------------------------------------------------------------------------------
import Adafruit_BBIO.GPIO as GPIO
import time
import numpy as np
# import matplotlib.pyplot as plt
# from collections import deque

#-----------------------
# Iniciar variables

Vrr_inicial=np.zeros(50)
Vrr_update = np.zeros(5)
n = 0 ; i = 0 ; j = 0 ;  count = 0; rr_end=0; rr_value=0;
totalrr=[]         # dynamic array


#N = 50
#data = deque([0] * N, maxlen=N)  # deque con longitud maxima N

#Creamos la figura
# plt.ion()
# fig, ax = plt.subplots()
# ll, = ax.plot(data)
#-----------------------
# Configurar Pines de entrada y salida
GPIO.setup("P9_12", GPIO.IN)

#-----------------------
    
def getRR(int):  
    global n,i,j,rr_start, rr_value, rr_end;
    print("interrup")

    if (n==0): 
       rr_start = time.time()
       n=1
    elif (n==1):
       rr_end = time.time()
       rr_value = rr_end - rr_start
       
       if (i<=50):
           # print "Entro... i<=50 --- i = " , i
           Vrr_inicial[i] = rr_value
           i+=1
           if i==50 : 
               # print "Primeros 50 datos", Vrr_inicial
               i=51
       elif (i>50 & j< 5):  
           print "Entro i> 50 y j = " , j
           Vrr_update[j] = rr_value
           j+=1
           if j==5: 
              # print "5 datos para actualizar ", Vrr_update
              j=0
              
       rr_start=rr_end 
       totalrr.append(rr_value)
       
       np.savetxt('totalrr.txt', totalrr, fmt='%10.4f')
       print("rr_value Time: ", rr_value)

    return  

     



stop_time = int(raw_input("Ingresar Tiempo de la Prueba en Segundos : "))

print "El tiempo es : ", stop_time , "Segundos "


start_time = time.time()
loop_time=0

GPIO.add_event_detect("P9_12", GPIO.RISING,callback=getRR, bouncetime=100)

while (loop_time<=stop_time):

        temp_time = time.time()
        loop_time = temp_time - start_time
 


print "Duracion de la prueba : ", loop_time , "Segundos "
    
print "Prueba Finalizada"    
       
GPIO.cleanup()
