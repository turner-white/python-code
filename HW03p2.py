# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:22:51 2020

@author: turne
"""

import numpy as np
from matplotlib import pyplot as plt

#Defining each g1, g2, and g3 function along with their derivatives and simple linear functions
def y0(x):
    return x*0

def y(x):
    return x

def g1(x):
    return (-1/27)*(x**5 - 3*x**3 + 15*x**2 + 9)

def g2(x):
    return x**5 - 3*x**3 + 15*x**2 + 28*x + 9

def g3(x):
    return -9*(x**4 - 3*x**2 + 15*x + 27)**-1

def dg1(x):
    return (-1/27)*(5*x**4 - 9*x**2 + 30*x)

def dg2(x):
    return 5*x**4-9*x**2+30*x+28

def dg3(x):
    return 9*(x**4-3*x**2+15*x+27)**-2 * (4*x**3-6*x+15)
#print(dg1(1.117))

#Creating a range of x-values to plot the functions over. After testing, -5,5 was determined to be effective
#at displaying the relevant roots and values of functions in one window
xrange = np.arange(-5,5,0.001)

#Individually plot each function, its derivative, the line y-0, and the line y=x. Ylim of 5 was introduced
#to make the graphs proportional and to show the line y=x with its true slope
plt.figure(0)
plt.plot(xrange,g1(xrange),xrange,np.abs(dg1(xrange)),xrange, y0(xrange), xrange, y(xrange))
plt.ylim(-5,5)
plt.grid(True)
plt.legend(('g1(x)','dg1(x)','y=0','y=x'))
plt.show()

plt.figure(1)
plt.plot(xrange,g2(xrange),xrange,np.abs(dg2(xrange)),xrange, y0(xrange), xrange, y(xrange))
plt.ylim(-5,5)
plt.grid(True)
plt.legend(('g2(x)','dg2(x)','y=0','y=x'))
plt.show()

plt.figure(2)
plt.plot(xrange,g3(xrange),xrange,np.abs(dg3(xrange)),xrange, y0(xrange), xrange, y(xrange))
plt.ylim(-5,5)
plt.grid(True)
plt.legend(('g3(x)','dg3(x)','y=0','y=x'))
plt.show()
#-----------------------------------------------------
#fixed_pt
#intent: To iterate on g(x) and update the previous x value with the next function value
#in: g, xstart, tol, n max
#while: designed to stop when either the tolerance is met or the max iterations are run
#out: a floating point value of the closest converging root.
#-----------------------------------------------------
def fixed_pt(g,xstart,tol,nmax):
    xn1 = 0
    xn = 0
    i = 0
    t = 1
    while tol <= t and i < nmax:
        xn1 = g(xstart)
        xn = xstart
        xstart = xn1
        t = np.abs(xn1-xn)
        
        i += 1
        
        #print(t)
    
    return xstart

print(fixed_pt(g1,0,10**-15,30),'Is the first root found by fixed iteration of g1')
#print(fixed_pt(g1,-1.1171,10**-15,50))
print(fixed_pt(g1,-2.22,10**-15,30), 'Is the second root found by fixed iteration of g1')
#print(fixed_pt(g2,-.46,10**-15,30))
#print(fixed_pt(g2,-1.11,10**-15,30))
#print(fixed_pt(g2,-2.22,10**-15,30))
print(fixed_pt(g3,0,10**-15,30),'Is the first root found by fixed iteration of g3')
#print(fixed_pt(g3,-1.11,10**-15,30))
#print(fixed_pt(g3,-2.22,10**-15,30))