#Test Imu + BMP180
print "Test Imu + BMP180"
from MPUaccel import ReadAccel
import Adafruit_BMP.BMP085 as BMP085

Imu=ReadAccel()
fax, fay, faz= Imu.readAccel()
temp = Imu.readTemp()

sensor = BMP085.BMP085()

print "-----------------------------------------------------------"
print "acel x: ", fax, " acel y: ", fay, " acel z: ", faz
print "Temperatura : " , temp

print "-----------------------------------------------------------"
print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature())
print 'Pressure = {0:0.2f} Pa'.format(sensor.read_pressure())
print 'Altitude = {0:0.2f} m'.format(sensor.read_altitude())
print 'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure())
print "-----------------------------------------------------------"