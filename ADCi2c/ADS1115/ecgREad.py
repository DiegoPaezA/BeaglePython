#!/usr/bin/python

import time, signal, sys
from Adafruit_ADS1x15 import ADS1x15
import pyqtgraph as pg
import numpy as np

def signal_handler(signal, frame):
       
        print 'You pressed Ctrl+C!'
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
#print 'Press Ctrl+C to exit'

ADS1115 = 0x01	# 16-bit ADC

# Select the gain
# gain = 6144  # +/- 6.144V
gain = 4096  # +/- 4.096V
#gain = 2048  # +/- 2.048V
#gain = 1024  # +/- 1.024V
# gain = 512   # +/- 0.512V
# gain = 256   # +/- 0.256V


#sps = 250  # 250 samples per second
#sps = 475  # 475 samples per second
sps = 860  # 860 samples per second

# Initialise the ADC using the default mode (use default I2C address)
# Set this to ADS1015 or ADS1115 depending on the ADC you are using!
adc = ADS1x15(ic=ADS1115)

ecgRead = []
stop_time = int(raw_input("Ingresar Tiempo de la Prueba en Segundos : "))
print "El tiempo es : ", stop_time , "Segundos "
start_time = time.time()
loop_time=0

while (loop_time<=stop_time):
            # Read channel 0 in single-ended mode using the settings above
        volts = adc.readADCSingleEnded(0, gain, sps) / 1000
        ecgRead.append(volts)
        
        temp_time = time.time()
        loop_time = temp_time - start_time

print len(ecgRead)
np.savetxt('ecg.txt', ecgRead, fmt='%10.2f')
pg.plot(ecgRead)

print "Duracion de la prueba : ", loop_time , "Segundos "
    
print "Prueba Finalizada"    
