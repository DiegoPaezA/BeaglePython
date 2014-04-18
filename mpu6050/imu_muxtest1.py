#!/usr/bin/python

from PCA9548lib import PCA9548
from MPU6050 import MPU6050

# Initialise the PCA9548 and use Channel 1 (default value)
# bmp = PCA9548(0x70)

print('Start')

# define clase 

PCA9548(0x70,1) #selecciona canal 1 mux
IMU1=MPU6050()
PCA9548(0x70,2) #selecciona canal 2 mux
IMU2=MPU6050()

print "Loop"

count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1
   PCA9548(0x70,1)
   print(IMU1.readSensors())
   print('\n')
   PCA9548(0x70,2)
   print(IMU2.readSensors())
   print('\n')

print "Good bye!"

#print(IMU1.readSensorsRaw())
#print(IMU1.readTemp())
#IMU.updateOffsets('IMU_offset.txt')
#IMU.readOffsets('IMU_offset.txt')
#print("IMU ready 1!")
#print('\n')

#PCA9548(0x70,2)
#print(IMU2.readSensorsRaw())

#IMU2.updateOffsets('IMU_offset2.txt')
#IMU2.readOffsets('IMU_offset2.txt')
#print("IMU ready 2!")
#print('\n')

#apaga los canales
PCA9548(0x70,0)

  
