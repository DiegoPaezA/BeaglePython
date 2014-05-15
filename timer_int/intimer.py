#Programa para testar las interrupciones por timer


import threading
from time import sleep

# Funcion Interrupcion
def setInterval(interval):
    def decorator(function):
        def wrapper(*args, **kwargs):
            stopped = threading.Event()

            def loop(): # executed in another thread
                while not stopped.wait(interval): # until stopped
                    function(*args, **kwargs)

            t = threading.Thread(target=loop)
#            t.daemon = True  # stop if the program exits
            t.start()
            return stopped
        return wrapper
    return decorator

@setInterval(.25)
def funcion():
    global flag,xx
    flag = 1
    lista.append(n)
    #print "Hello World"
    xx = xx + 1
    print xx
    return xx

@setInterval(1)
def funcion2():
    print "funcion 2"


stop = funcion()  # start timer, the first call is in .5 seconds

lista=[]  # lista para almacenar lecturas

n = 0
xx = 0
flag = 0

while n<10:
 #   print "do something else"
    n = n + 1
    if flag == 1:
        #print xx
        flag = 0
    if n == 5:
        print "----------Activada funcion 2"
        stop1 = funcion2()
    sleep(1)

stop.set() # stop interrupt
stop1.set()

print "---------------------"
print lista
print "finish"
