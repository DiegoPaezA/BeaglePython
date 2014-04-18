import Adafruit_BBIO.GPIO as GPIO
import time
import numpy as np

a=np.zeros(50)
start_time = time.time()

GPIO.setup("P9_12", GPIO.IN)


def printFunction(int): 
     
    global n, start_time, elapsed_time, end_time;
    print ("------------------------")
    print("Interrupcion : ", n)
    print ("------------------------")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed Time: ", elapsed_time)
    start_time=end_time
    a[n]=elapsed_time
    n += 1
    if n==50:
       print a 
    return  

     
GPIO.add_event_detect("P9_12", GPIO.RISING,callback=printFunction, bouncetime=50)


count = 0
n = 0
while (n<50):

   print 'The count is:', count
   count = count + 1
   time.sleep(0.5)


# Clear event 
# GPIO.cleanup()

# Remove event
# GPIO.remove_event_detect("P9_12")




     

     