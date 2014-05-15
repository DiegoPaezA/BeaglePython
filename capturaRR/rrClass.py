# Clase para calcular los datos de VFC
import numpy as np


class hrv:
    dado=None

    def __init__(self,dado):
        self.dado=dado
        self.dados=np.loadtxt(self.dado,delimiter='\n')
        self.n=self.dados.size

    def mediahrv(self):
        self.media=(1/float(self.n))*np.sum(self.dados)
        return self.media

    def SDNN(self):
        p=0
        for i in range(0,self.n):
            a = (self.dados[i] - self.media)**2
            p = p+a
        return np.sqrt(1/(float(self.n) -1)*(p))

    def RMSSD(self):
        p=0
        for i in range(0,(self.n - 1)):
            a = (self.dados[i] - self.dados[i+1])**2
            p = p+a
        return np.sqrt(1/(float(self.n) -1)*(p))

    def pNN50(self):
        p=0
        for i in range(0,(self.n - 1)):
            if (abs(self.dados[i] - self.dados[i+1]) > .05):
                p += 1
        return ((p)/(float(self.n)-1)) * 100

