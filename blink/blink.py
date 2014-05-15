import Adafruit_BBIO.GPIO as GPIO
import time
from bbio import *

LED = GPIO0_4
pinMode(LED, OUTPUT)

#GPIO.setup("P8_10", GPIO.OUT)
#GPIO.setup("P8_12", GPIO.OUT)
GPIO.setup("P9_16", GPIO.OUT)

#GPIO.output("P9_18", GPIO.LOW)
#time.sleep(5)

while True:
    GPIO.output("P9_16", GPIO.HIGH)
    digitalWrite(LED, HIGH)
  
    #GPIO.output("P8_12", GPIO.LOW)
    time.sleep(0.5)
    digitalWrite(LED, LOW)
    GPIO.output("P9_16", GPIO.LOW)
    #GPIO.output("P8_12", GPIO.HIGH)
    time.sleep(0.5)
