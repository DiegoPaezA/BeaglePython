#
#solenero.tech@gmail.com
#solenerotech.wordpress.com

#solenerotech 2013.07.31

#2013.10.1 ImU Test 2
#2013.10.10 ImU Test 3

from time import sleep,time
import numpy
from kalmanfilter import KalmanFilterLinear
from lowpassfilter import lowpassfilter
import math

def getAngleGyro(r,p,y,fgx,fgy,fgz,dt):
    new_r=r+fgx*dt
    new_p=p+fgy*dt
    new_y=y+fgz*dt
    return new_r,new_p,new_y


def getAngleAcc(fax, fay, faz):
    #TODO it seems that right now the acc data are not correctly
    #scaled so that's why I'm using gravity=0.98
    g=0.980665
    pi=3.141592
    #ATTENTION atan2(y,x) while in excel is atan2(x,y)
    r=math.atan2(fay,faz+g)*180/pi
    p=math.atan2(fax,faz+g)*180/pi
    #ATTENTION the following calculation does not return
    #a consistent value.
    #by the way it is not used
    y=math.atan2(fax,fay)*180/pi

    return r,p,y


def getAngleCompl(r,p,y,fay, faz, fgx, fgy, fgz,dt):
    tau=0.003
    #tau is the time constant in sec
    #for time periods <tau the  gyro takes precedence
    #for time periods > tau the acc takes precedence

    new_r,new_p,new_y=getAngleAcc(fax, fay, faz)
    a=tau/(tau+dt)
    new_r=a*(new_r+fgx*dt)+(1-a)*r
    new_p=a*(new_p+fgy*dt)+(1-a)*p
    #note the yaw angle can be calculated only using the
    # gyro that's why a=1
    a=1
    new_y=a*(new_y+fgz*dt)+(1-a)*y

    return new_r,new_p,new_y

#import pylab

try:
    from MPU6050 import MPU6050
    #print ('MPimport ok')
except ImportError:
    print ('import nok')


#logger = logging.getLogger(__name__)
IMU=MPU6050()
IMU.updateOffsets('IMU_offset.txt')
IMU.readOffsets('IMU_offset.txt')
print ('IMU ready!')



#Kalman filter parameters for a 1-dim case x 3
#dimension with error distribution = gaussian
#
A = numpy.eye(3)
H = numpy.eye(3)
B = numpy.eye(3)*0
Q = numpy.eye(3)*0.001
#play with Q to tune the smoothness
R = numpy.eye(3)*0.01
xhat = numpy.matrix([[0],[0],[0]])
P= numpy.eye(3)

kf = KalmanFilterLinear(A,B,H,xhat,P,Q,R)
lpf=lowpassfilter(0.025)

fax=0
fay=0
faz=0
fgx=0
fgy=0
fgz=0
faxk=0
fayk=0
fazk=0
faxf=0
fayf=0
fazf=0
rg=0
pg=0
yg=0
ra=0
pa=0
ya=0
rc=0
pc=0
yc=0

#measuredfax=[]
#kalmanfx=[]
lines=''
lines2=''
lines=lines+('n|t|dt|fax| fay| faz| fgx| fgy| fgz| faxf| fayf| fazf| faxk| fayk| fazk\n')
lines2=lines2+('n|t|dt|fax| fay| faz| fgx| fgy| fgz| ra| rg| rc| pa| pg| pc| ya| yg| yc\n')
lines=lines+('0| 0| 0|'+str(fax)+'|'+str(fay)+'|'+str(faz)+'|'+str(fgx)+'|'+str(fgy)+'|' + str(fgz)+ '|' +str(faxf)+'|' + str(fayf)+'|' + str(fazf)+'|' + str(faxk)+'|' + str(fayk)+'|' + str(fazk)+' \n')
inittime=time()
tottime=0
cycletime=0.03
for i in range (2000):
    tottime_old=tottime
    fax, fay, faz, fgx, fgy, fgz= IMU.readSensors()
    faxk,fayk,fazk = kf.filter(numpy.matrix([[0],[0],[0]]),numpy.matrix([[fax],[fay],[faz]]))
    tottime=time()-inittime
    steptime=tottime-tottime_old
    faxf,fayf,fazf=lpf.filter(fax,fay,faz,steptime)

    #Calculate angles
    ra,pa,ya=getAngleAcc(fax, fay, faz)
    rg,pg,yg=getAngleGyro(rg,pg,yg, fgx, fgy, fgz,steptime)


    #fusion of sensors using the complementary filter
    rc,pc,yc=getAngleCompl(rc,pc,yc,fay, faz, fgx, fgy, fgz,steptime)

    lines=lines +(str(i)+'|'+str(tottime)+'|'+str(steptime)+'|'+str(fax)+'|'+str(fay)+'|'+str(faz)+'|'+str(fgx)+'|'+str(fgy)+'|' + str(fgz)+ '|' +str(faxf)+'|' + str(fayf)+'|' + str(fazf)+'|' + str(faxk)+'|' + str(fayk)+'|' + str(fazk)+' \n')
    lines2=lines2+ (str(i)+'|'+str(tottime)+'|'+str(steptime)+'|'+str(fax)+'|'+str(fay)+'|'+str(faz)+'|'+str(fgx)+'|'+str(fgy)+'|' + str(fgz)+ '|' +str(ra)+'|' + str(rg)+'|' + str(rc)+'|' + str(pa)+'|' + str(pg)+'|' + str(pc)+'|'+str(ya)+'|' + str(yg)+'|' + str(yc)+' \n')

    #sleep(0.001)
    #print str(cycletime-steptime)
    #sleep(cycletime-steptime)
    #measuredfax.append(fax)
    #kalmanfx.append(faxk)
#print str(tottime)
with open('sensor_data.txt', 'w+') as data_file:
    data_file.write(lines)
    data_file.flush()

with open('sensor_data2.txt', 'w+') as data_file:
    data_file.write(lines2)
    data_file.flush()


#if False:
#    pylab.plot(range(1000),measuredfax,'b',range(1000),range(1000),kalmanfax,'g')
#    pylab.xlabel('Time')
#    pylab.ylabel('Voltage')
#    pylab.title('Voltage Measurement with Kalman Filter')
#    pylab.legend(('measured','true voltage','kalman'))
#    pylab.show()






