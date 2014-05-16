__author__ = 'diegopaez'
import numpy as np
from array import array


n1 =[]         # dynamic array
x=array('i')   # dynamic array

for i in range(10):
    n1.append(i)
    x.append(i)


n1_array=np.array(n1)
n2_array=np.array(x)


# Escritura de archivos
np.savetxt('matriz_b1.txt', n1_array, fmt='%10.2f')
np.savetxt('matriz_b2.txt', n2_array, fmt='%.2e')

# lectura de archivos
Vread=np.loadtxt('matriz_b1.txt')

print Vread
print "Fin"
