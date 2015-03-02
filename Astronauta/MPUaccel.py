#!/usr/bin/python

import smbus

class ReadAccel :

    i2c = None
    
    # Power management registers
    power_mgmt_1 = 0x6b
    power_mgmt_2 = 0x6c
    MPU6050_RA_ACCEL_XOUT_H= 		0x3b
    MPU6050_RA_ACCEL_YOUT_H= 		0x3d
    MPU6050_RA_ACCEL_ZOUT_H= 		0x3f
    MPU6050_RA_TEMP_OUT_H= 		0x41
    
    def __init__(self, address=0x68,i2c_bus = 2):
        print "start--config MPU6050" 
        self.bus = smbus.SMBus(i2c_bus)    # or bus = smbus.SMBus(1) for Revision 2 boards
        self.address = 0x68       # This is the address value read via the i2cdetect command
        self.bus.write_byte_data(self.address, self.power_mgmt_1, 0) # Now wake the 6050 up as it starts in sleep mode
        
    def read_byte(self,adr):
        return self.bus.read_byte_data(self.address, adr)
    
    def read_word(self,adr):
        high = self.bus.read_byte_data(self.address, adr)
        low = self.bus.read_byte_data(self.address, adr+1)
        val = (high << 8) + low
        return val
    
    def read_word_2c(self,adr):
        val = self.read_word(adr)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val
        
    def readAccel(self):
        accel_xout = self.read_word_2c(self.MPU6050_RA_ACCEL_XOUT_H)
        accel_yout = self.read_word_2c(self.MPU6050_RA_ACCEL_YOUT_H)
        accel_zout = self.read_word_2c(self.MPU6050_RA_ACCEL_ZOUT_H)
        
        accel_xout_scaled = accel_xout / 16384.0
        accel_yout_scaled = accel_yout / 16384.0
        accel_zout_scaled = accel_zout / 16384.0
        
        return accel_xout_scaled ,accel_yout_scaled ,accel_zout_scaled
    
    def readTemp(self):
        temp = self.read_word_2c(self.MPU6050_RA_TEMP_OUT_H)
        temp = (float(temp) / 340) + 36.53
        ##logger.debug('temp = %s oC', temp)
        return temp