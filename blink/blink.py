import Adafruit_BBIO.GPIO as GPIO
import time
 
GPIO.setup("P8_10", GPIO.OUT)
GPIO.setup("P8_12", GPIO.OUT)

GPIO.setup("P9_18", GPIO.OUT)

GPIO.output("P9_18", GPIO.LOW)
time.sleep(5)

''' 
while True:
    GPIO.output("P8_10", GPIO.HIGH)
    GPIO.output("P8_12", GPIO.LOW)
    time.sleep(0.5)
    GPIO.output("P8_10", GPIO.LOW)
    GPIO.output("P8_12", GPIO.HIGH)
    time.sleep(0.5)
'''