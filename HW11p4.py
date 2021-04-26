# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:42:47 2020

@author: turne
"""

import numpy as np
from scipy import interpolate as intp
from matplotlib import pyplot as plt

def f(x):
    return np.abs(np.sin(x))

xrange = np.arange(-10,10,0.1)
y = f(xrange)
print('-------------------Part B-------------------')
plt.plot(xrange,y)
plt.plot(xrange,0*xrange)
plt.title('True Function sampled over 0.1 step size')
plt.show()
print()
Sn = intp.interp1d(xrange, y, kind=('nearest'))
Sl = intp.interp1d(xrange, y, kind=('linear'))
Sq = intp.interp1d(xrange, y, kind=('quadratic'))
Sc = intp.interp1d(xrange, y, kind=('cubic'))

prange = np.arange(-0.5,0.5,0.001)
print('-------------------Part C-------------------')
plt.plot(prange,Sn(prange))
plt.scatter(xrange,y)
plt.plot(prange,f(prange))
plt.xlim(-0.5,0.5)
plt.ylim(0,0.6)
plt.legend(('Interp', 'f(x)'))
plt.title('Nearest Interpolation')
plt.show()

plt.plot(prange,Sl(prange))
plt.scatter(xrange,y)
plt.plot(prange,f(prange))
plt.xlim(-0.5,0.5)
plt.ylim(0,0.6)
plt.legend(('Interp', 'f(x)'))
plt.title('Linear Interpolation')
plt.show()

plt.plot(prange,Sq(prange))
plt.scatter(xrange,y)
plt.plot(prange,f(prange))
plt.xlim(-0.5,0.5)
plt.ylim(0,0.6)
plt.legend(('Interp', 'f(x)'))
plt.title('Quad. Interpolation')
plt.show()

plt.plot(prange,Sc(prange))
plt.scatter(xrange,y)
plt.plot(prange,f(prange))
plt.xlim(-0.5,0.5)
plt.ylim(0,0.6)
plt.legend(('Interp', 'f(x)'))
plt.title('Cubic Interpolation')
plt.show()
print()
print('-------------------Part D-------------------')
drange = np.arange(1,2,0.001)

plt.plot(drange,Sl(drange))
plt.scatter(xrange,y)
plt.plot(drange,f(drange))
plt.xlim(1.38,1.75)
plt.ylim(0.96,1.04)
plt.legend(('Interp', 'f(x)'))
plt.title('Linear Interpolation at peak')
plt.show()

plt.plot(drange,Sc(drange))
plt.scatter(xrange,y)
plt.plot(drange,f(drange))
plt.xlim(1.38,1.75)
plt.ylim(0.96,1.04)
plt.legend(('Interp', 'f(x)'))
plt.title('Cubic Interpolation at peak')
plt.show()

