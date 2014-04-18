#!/usr/bin/python

import time
from Adafruit_I2C import Adafruit_I2C # First Install Adafruit_I2C library for BBB
# https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black

# ===========================================================================
# PCA9548 Class
# ===========================================================================

class PCA9548 :
  i2c = None


  # PCA9548 CHANNELS
  __PCA9548_CH0           = 0x00  # W   CHANNELS OFF  
  __PCA9548_CH1           = 0x01  # W   ACTIVATION OF CHANNEL 1
  __PCA9548_CH2           = 0x02  # W   ACTIVATION OF CHANNEL 2
  __PCA9548_CH3           = 0x04  # W   ACTIVATION OF CHANNEL 3
  __PCA9548_CH4           = 0x08  # W   ACTIVATION OF CHANNEL 4
  __PCA9548_CH5           = 0x10  # W   ACTIVATION OF CHANNEL 5
  __PCA9548_CH6           = 0x20  # W   ACTIVATION OF CHANNEL 6
  __PCA9548_CH7           = 0x40  # W   ACTIVATION OF CHANNEL 7
  __PCA9548_CH8           = 0x88  # W   ACTIVATION OF CHANNEL 8
 
  # Constructor
  def __init__(self, address=0x70, channel=1,debug=False):
    self.i2c = Adafruit_I2C(address)

    self.address = address
    self.debug = debug
    # Activate Channel
    if (channel == 0):
        self.i2c.write8(self.address,self.__PCA9548_CH0)
    	time.sleep(0.005)  # Wait 5ms    
    	print("Channels Off")
    elif (channel == 1):
	self.i2c.write8(self.address,self.__PCA9548_CH1)
    	time.sleep(0.005)  # Wait 5ms
        print("Channel 1 selected")    
    elif (channel == 2):
        self.i2c.write8(self.address,self.__PCA9548_CH2)
    	time.sleep(0.005)  # Wait 5ms
        print("Channel 2 selected")    
    elif (channel == 3):
        self.i2c.write8(self.address,self.__PCA9548_CH3)
    	time.sleep(0.005)  # Wait 5ms 
        print("Channel 3 selected")   
    elif (channel == 4):
        self.i2c.write8(self.address,self.__PCA9548_CH4)
    	time.sleep(0.005)  # Wait 5ms
        print("Channel 4 selected")    	
    elif (channel == 5):
        self.i2c.write8(self.address,self.__PCA9548_CH5)
    	time.sleep(0.005)  # Wait 5ms
        print("Channel 5 selected")    
    elif (channel == 6):
        self.i2c.write8(self.address,self.__PCA9548_CH6)
    	time.sleep(0.005)  # Wait 5ms    
        print("Channel 6 selected")
    elif (channel == 7):
        self.i2c.write8(self.address,self.__PCA9548_CH7)    
    	time.sleep(0.005)  # Wait 5ms
        print("Channel 7 selected")    	
    elif (channel == 8):
        self.i2c.write8(self.address,self.__PCA9548_CH8)
    	time.sleep(0.005)  # Wait 5ms
        print("Channel 8 selected")    
    else: 
    	print("Error!, select a channel  between  1-8")		

#------------------------------------------------------

