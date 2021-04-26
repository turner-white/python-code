# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:42:46 2020

@author: turne
"""
import numpy as np
from matplotlib import pyplot as plt

m = 15
g = 2.2
k = 32

def PartA(f):
    A = 1
    w0 = np.sqrt(k/m)
    w1 = 2*np.pi*f
    return (A/m)/np.sqrt((w0**2-w1**2)**2+((w1**2 * g**2)/m**2))

f0 = (np.sqrt(k/m))/(2*np.pi)
frange = np.arange(0,2.5*f0,0.001)

plt.plot(frange, PartA(frange))
plt.title('Part A cos driving force')
plt.show()  

def PartB(tau):
    trange = np.arange(-1000,1000,0.01)
    N = len(trange)
    dt = 0.01
    df = 1/(N*dt)
    dw = 2*np.pi*df
    wrange = np.arange(0,N*dw,dw)
    
    def F(t):
        return np.exp(-(t**2)/(tau**2))
    
    FT = F(trange)
    
    FW = np.fft.fft(FT)
    
    X = FW/(-m*(wrange)**2 + (-1)**0.5 *g*wrange + k)
    
    xt = (np.fft.ifft(X))

    frange = np.arange(0,N*df,df)
    return FT, np.abs(FW), np.abs(X), np.real(xt), trange, frange

tau1 = PartB(1)
tau3 = PartB(3)
tau10 = PartB(10)

plt.plot(tau1[4],tau1[0])
plt.plot(tau3[4],tau3[0])
plt.plot(tau10[4],tau10[0])
plt.xlim(-50,50)
plt.title('FT')
plt.legend(('tau1', 'tau3','tau10'))
plt.show()

plt.plot(tau1[5], tau1[1])
plt.plot(tau3[5], tau3[1])
plt.plot(tau10[5], tau10[1])
plt.xlim(0,1)
plt.title('FW')
plt.legend(('tau1', 'tau3','tau10'))
plt.show()

plt.plot(tau1[5], tau1[2])
plt.plot(tau3[5], tau3[2])
plt.plot(tau10[5], tau10[2])
plt.xlim(0,1)
plt.title('Xw')
plt.legend(('tau1', 'tau3','tau10'))
plt.show()

plt.plot(tau1[4], tau1[3])
plt.plot(tau3[4], tau3[3])
plt.plot(tau10[4], tau10[3])
plt.xlim(-50,50)
plt.title('xt')
plt.legend(('tau1', 'tau3','tau10'))
plt.show()
    
    
    
    
    
    