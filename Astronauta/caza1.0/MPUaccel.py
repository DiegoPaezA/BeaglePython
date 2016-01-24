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
    MPU6050_RA_TEMP_OUT_H= 		    0x41
    MPU6050_RA_ACCEL_CONFIG= 		0x1C
    
    def __init__(self, address=0x68,i2c_bus = 1, Arange =2):
        print "start--config MPU6050" 
        self.bus = smbus.SMBus(i2c_bus)    # or bus = smbus.SMBus(1) for Revision 2 boards
        self.address = address       # This is the address value read via the i2cdetect command
        self.bus.write_byte_data(self.address, self.power_mgmt_1, 0) # Now wake the 6050 up as it starts in sleep mode
        self.setRange(Arange)
        
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
    
    def setRange(self,Arange = 2):
        #0x00=+/-2 0x08=+/- 4    0x10=+/-8 0x18=+/-16
        if Arange ==2:
            data = 0x00
            self.scale = 16384.0
        elif Arange == 4:
            data = 0x08
            self.scale = 8192.0
        elif Arange == 8:
            data = 0x10
            self.scale = 4096.0
        elif Arange == 16:
            data = 0x18
            self.scale = 2048.0
        self.bus.write_byte_data(self.address,self.MPU6050_RA_ACCEL_CONFIG, data)
        
    def readAccel(self):
        accel_xout = self.read_word_2c(self.MPU6050_RA_ACCEL_XOUT_H)
        accel_yout = self.read_word_2c(self.MPU6050_RA_ACCEL_YOUT_H)
        accel_zout = self.read_word_2c(self.MPU6050_RA_ACCEL_ZOUT_H)
        
        accel_xout_scaled = accel_xout / self.scale
        accel_yout_scaled = accel_yout / self.scale
        accel_zout_scaled = accel_zout / self.scale
        
        return accel_xout_scaled ,accel_yout_scaled ,accel_zout_scaled
    
    def readTemp(self):
        temp = self.read_word_2c(self.MPU6050_RA_TEMP_OUT_H)
        temp = (float(temp) / 340) + 36.53
        ##logger.debug('temp = %s oC', temp)
        return temp