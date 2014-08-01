# Diego R. Paez Ardila
# Ejecutar software por intervalos de tiempo indicados por el usuario
#

import time





# Solicitar al usuario que ingrese el tiempo en segundos

Tempo = int(raw_input("Ingresar Segundos : "))

print "El tiempo es : ", Tempo , "Segundos "

off_time = 0

start_time = time.time()

while (off_time<=Tempo):
        loop_time = time.time()
        off_time = loop_time - start_time


print off_time
print "Out"        


