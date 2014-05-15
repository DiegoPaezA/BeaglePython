
# serial_echo.py - Alexander Hiam - 4/15/12
#
# Prints all incoming data on Serial2 and echos it back.
#
# Serial1 TX = pin 24 on P9 header
# Serial1 RX = pin 26 on P9 header
#
# This example is in the public domain
from bbio import *
def setup():
    # Start Serial2 at 9600 baud:
    Serial1.begin(9600)
def loop():
    if (Serial1.available()):
        # There's incoming data
        data = ''
        while(Serial1.available()):
        # If multiple characters are being sent we want to catch
        # them all, so add received byte to our data string and
        # delay a little to give the next byte time to arrive:
            data += Serial1.read()
            delay(5)
        # Print what was sent:
        print "Data received:\n '%s'" % data
        # And write it back to the serial port:
        Serial1.write("A")
        # And a little delay to keep the Beaglebone happy:
    delay(200)

run(setup, loop)