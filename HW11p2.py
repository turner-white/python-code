# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:42:46 2020

@author: turne
"""

import numpy as np
from matplotlib import pyplot as plt

def ExactSol(xvec):
    u = 2*np.exp(-1*xvec) - np.exp(-1000*xvec)
    v = -1*np.exp(-1*xvec) + np.exp(-1000*xvec)
    return (np.array(u),np.array(v))

xrange = np.arange(0,4,0.001)
bruh = ExactSol(xrange)
plt.plot(xrange,bruh[0],xrange,bruh[1])
plt.xscale('log')
plt.title('ExactSol')
plt.legend(('u', 'v'))
plt.show()

def ExplicitIntegrate(xstart, xstop, h, ystart):
    C = np.array([[-998.,-1998.],[999.,1999.]])
    I = np.array([[1.,0.],[0.,1.]])
    xrange = np.arange(xstart,xstop,h)
    N = len(xrange)
    vvec = np.zeros((N,2))
    vvec[0] = ystart
    for i in range(1,N):
        #print()
        vvec[i] = (I-h*C) @ vvec[i-1]
        
    return xrange, vvec

bruhx1, bruhy1 = ExplicitIntegrate(0,4,0.001,np.array([1,0]))
plt.plot(xrange,bruh[0],xrange,bruh[1])
plt.plot(bruhx1,bruhy1)
plt.legend(('ExactSol u','ExactSol v','Explicit u','Explicit v'))
plt.title('ExactSol & Explicit')
plt.xscale('log')
plt.show()

def ImplicitIntegrate(xstart, xstop, h, ystart):
    C = np.array([[-998.,-1998.],[999.,1999.]])
    I = np.array([[1.,0.],[0.,1.]])
    xrange = np.arange(xstart,xstop,h)
    N = len(xrange)
    vvec = np.zeros((N,2))
    vvec[0] = ystart
    for i in range(1,N):
        #print()
        vvec[i] = np.linalg.inv(I+h*C) @ vvec[i-1]
        
    return xrange, vvec

bruhx2, bruhy2 = ImplicitIntegrate(0,4,0.001,np.array([1,0]))
plt.plot(xrange,bruh[0],xrange,bruh[1])
plt.plot(bruhx2,bruhy2)
plt.legend(('ExactSol u','ExactSol v ', 'Implicit u', 'Implicit v'))
plt.title('ExactSol & Implicit')
plt.xscale('log')
plt.show()

he = 0.002
hi = 0.01

bruhhx1, bruhhy1 = ExplicitIntegrate(0,4,he,np.array([1,0]))
plt.plot(bruhhx1,bruhhy1)
plt.xscale('log')
plt.title('Messing around with h explicit')
plt.show()
bruhhx2, bruhhy2 = ImplicitIntegrate(0,4,hi,np.array([1,0]))
plt.plot(bruhhx2, bruhhy2)
plt.xscale('log')
plt.title('Messing around with h implicit')
plt.show()

