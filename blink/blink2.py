from bbio import *
import Adafruit_BBIO.GPIO as GPIO

LED = GPIO0_4
off = 0
def setup():
  pinMode(LED, OUTPUT)
  GPIO.setup("P9_24", GPIO.IN)
  GPIO.add_event_detect("P9_24", GPIO.RISING,callback=start, bouncetime=100)
def start(isr):
  global off
  #-----------------------------------
  print "Start Capture"
  GPIO.remove_event_detect("P9_24")
  #-----------------------------------
  off =1
  return
def loop():
  global off
  toggle(LED)
  delay(500)
  if off == 1:
    exit()

run(setup, loop)