#test imu
print "Test Imu 1"
from MPU6050 import MPU6050
IMU=MPU6050()
fax, fay, faz, fgx, fgy, fgz= IMU.readSensors()
print "acel x: ", fax, " acel y: ", fay, " acel z: ", faz 