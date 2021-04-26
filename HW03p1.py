# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:22:29 2020

@author: turne
"""
import numpy as np
from matplotlib import pyplot as plt
#Define the test function and its derivative using python syntax
def func(x):
    return (x**5) - (3*x**3) + (15*x**2) + (27*x) + 9

def dfunc(x):
    return (5*x**4) - (9*x**2) + (30*x) + 27

#Plot the functionn to visually estimate roots and starting values for NR root finder
xrange = np.arange(-4,4,.001)
plt.plot(xrange,func(xrange))
plt.ylim(-8,8)
plt.grid(True)
plt.show()
#----------------------------------------------------------------------------
#Newt Function
#intent: To performm newton-raphson fixed point iteration and converge on roots of a test function
#in: xstart is the starting xvalue approximated visually from the plot. tol is the allowed tolerance
#while: this loop runs as long as the tolerance has not been met. It updates the value of xn1 and xn according
#       to the NR method.
#out: xn1 after the loop is completed is the approximate value of the root
#----------------------------------------------------------------------------
def Newt(xstart,tol):
    xn1 = 0
    xn = 0
    t = 20 # must be greater than 0 so that the while loop functions correctly.
    while tol <= t:
        xn1 = xstart - (func(xstart)/dfunc(xstart))
        xn = xstart
        xstart = xn1
        t = np.abs(xn1 - xn)
    
    return(xn1)

#Print the results
print('The first root is found at: ', Newt(-.46,10**(-14)))
print('The second root is found at: ',Newt(-1.1,10**(-14)))
print('The third root is found at: ',Newt(-2.25,10**(-14)))
        