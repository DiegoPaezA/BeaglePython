import Adafruit_BBIO.GPIO as GPIO
import time
from bbio import *

#LED1 = GPIO2_12
#pinMode(LED1, OUTPUT)

LED1 = "P8_7"
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup("P8_10", GPIO.OUT)
GPIO.setup("P8_12", GPIO.OUT)
GPIO.setup("P8_14", GPIO.OUT)

GPIO.setup("P9_30", GPIO.IN)
#GPIO.output("P9_18", GPIO.LOW)
#time.sleep(5)
print "Start Blink"
while True:
    GPIO.output(LED1, GPIO.HIGH)
    GPIO.output("P8_10", GPIO.HIGH)
    GPIO.output("P8_12", GPIO.HIGH)
    GPIO.output("P8_14", GPIO.HIGH)
    #print "High"
    #digitalWrite(LED1, HIGH)
  
    time.sleep(0.5)
    GPIO.output(LED1, GPIO.LOW)
    GPIO.output("P8_10", GPIO.LOW)
    GPIO.output("P8_12", GPIO.LOW)
    GPIO.output("P8_14", GPIO.LOW)
    
    #digitalWrite(LED1, LOW)
    #print "Low"
    time.sleep(0.5)
    
    if GPIO.input("P9_30"):
        print("HIGH")
    else:
        print("LOW")
