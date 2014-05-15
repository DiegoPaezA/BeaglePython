#!/usr/bin/python
from rrClass import hrv

r = hrv('totalrr.csv')
print r.mediahrv()
print r.SDNN()
print r.RMSSD()
print r.pNN50()
