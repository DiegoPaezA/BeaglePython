from bbio import *

LED = GPIO0_4

def setup():
  pinMode(LED, OUTPUT)

def loop():
  toggle(LED)
  delay(500)

run(setup, loop)