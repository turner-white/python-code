# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:33:52 2020

@author: turne
"""

import numpy as np
from matplotlib import pyplot as plt
import scipy.optimize
#use loadtext with stupid backwards parentheses to access data
path = 'C:/Users/turne/Documents/Fall 2020 UNC/Code/HW04p3data.csv'
data = np.loadtxt(path, delimiter=',')
print(data)
print(len(data[:]))
print(len(data[0][:]))

v = []
Sv = []
#make the data into arrays
for e in data:
    v.append(e[0])
    Sv.append(e[1])
    
v = np.array(v)
Sv = np.array(Sv)
plt.figure(0)
plt.scatter(v,Sv, c='r')
#since there are two functions, I created a function within a function to handle the substitution
def ModelSpectrum(c1,c2,v01,v02,gamma1,gamma2,v):
    def L(v0,ga,v):
        return 1/np.pi*1/2*ga/((v-v0)**2+(1/2*ga)**2)
    return c1*L(v01,gamma1,v) + c2*L(v02,gamma2,v)

plt.plot(v, ModelSpectrum(56,20,20237,20700,50,50,v))

#56,20,20237,20700,50,50

#d      #c1#c2#
x0 = np.array([56,20,20237,20700,50,50])
#define the second function that takes an array input where constants are indexed inputs
def ModelSpectrum2(x,v):
    def L(v0,ga,v):
        return 1/np.pi*1/2*ga/((v-v0)**2+(1/2*ga)**2)
    return x[0]*L(x[2],x[4],v) + x[1]*L(x[3],x[5],v)

plt.plot(v,ModelSpectrum2(x0,v),c='b')
#take the difference and return it as an array
def Residuals(x1,v,Sv):
    #for e in 
    return np.array(Sv - ModelSpectrum2(x1,v))

plt.plot(v,Residuals(x0,v,Sv))

#time for scipy! We struggled for a bit with the arguments and exact return values but eveuntally got it in
#the end
res = (scipy.optimize.leastsq(Residuals,x0, args= (v,Sv)))
x1 = res[0]
print(x1)
plt.plot(v, Residuals(x1,v,Sv))
plt.figure(1)
vmesh = np.arange(20000,21000,.001)
plt.plot(vmesh, ModelSpectrum2(x1,vmesh))
plt.scatter(v,Sv)
#the best fit values
#20237
#20696
    

