import Adafruit_BBIO.UART as UART
import serial
import time 
import numpy as np 
UART.setup("UART1")
 
ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser.close()
ser.open()
i = 0 
#if ser.isOpen():
print "Serial is open!"
#ser.write("hola")


line = ''
while i < 10:
	
	line = ser.read()
	
	
	print line

	if line == "A":
		ser.write("A")
	#	i = 51
		ser.write("diego$")
	i += 1
	#print i
	time.sleep(0.1)
		
ser.close()
 
# Eventually, you'll want to clean up, but leave this commented for now, 
# as it doesn't work yet
#UART.cleanup()
