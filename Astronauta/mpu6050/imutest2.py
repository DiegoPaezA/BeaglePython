#test imu
print "Test Imu 1"
from MPUaccel import ReadAccel
Imu=ReadAccel()
fax, fay, faz= Imu.readAccel()
temp = Imu.readTemp()
print "acel x: ", fax, " acel y: ", fay, " acel z: ", faz
print "Temperatura : " , temp
