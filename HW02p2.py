# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:50:34 2020

@author: turne
"""
import numpy as np
from matplotlib import pyplot as plt

def rf_bisect(f,xlo,xhi,xtol,nmax):
#Computes the value of the root for function f bracketed in the domain [xlo, xhi]. 
# PARAMETERS:
#   f     --  (function) The one-dimensional function to evaluate a root of.
#   xlo   --  (float) The lower limit of the bracket.
#   xhi   --  (float) The upper limit of the bracket.
#   xtol  --  (float) The tolerance the calculated root should achieve.
#   nmax  --  (int) The maximum number of iterations allowed.

# RETURNS: (tuple(float, int)) A root of f that meets the tolerance tol the number 
# of iteratons required to converge.
    
#----> Implement your solution for rf_bisect here <-------
    iters = 1
    xtemp = []
    ftemp = []
    while (iters <= nmax) and (np.abs(xhi-xlo) >= xtol):
        root = (xlo+xhi)/2
        flo = f(xlo)
        fhi = f(xhi)
        fmid = f(root)
        #print(xlo,root,xhi)
        xtemp.append(root)
        ftemp.append(fmid)
        if flo*fmid < 0:
            xhi = root
            #print ('the sign change is below midpoint')
            
        if fhi*fmid < 0:
            xlo = root
            #print('the sign change is above midpoint')
            
        elif fmid == 0:
            #print('zero has been found')
            break
            
        iters += 1
        #print(root,iters)
        
    return (xtemp, ftemp)

# Functions f1, f2, f3, and f4 that may be used to test your implementation of rf_bisect.
def f1(x):
    return 3 * x + 2*np.sin(x) - np.exp(x)

def f2(x):
    return x**3 - 0.125

def f3(x):
    return np.sin(1. / (x + 0.01))

def y0(x):
    return 0*x
xrange = np.arange(-1,1,0.001)

xar1,far1 = rf_bisect(f1,-1,1,10**-10,30)
plt.figure(0)
plt.plot(xar1,far1,xrange,f1(xrange),xrange,y0(xrange))
plt.plot(xar1,far1,'.')
plt.title('F1 and midpoint error plot')
plt.grid(True)
plt.xlim(-0.05,0.7)
plt.ylim(-1,1)
plt.show()

xar2,far2 = rf_bisect(f2,-1,1,10**-10,30)
plt.figure(1)
plt.plot(xar2,far2,xrange,f2(xrange),xrange,y0(xrange))
plt.plot(xar2,far2,'.')
plt.title('F2 and midpoint error plot')
plt.xlim(-0.1,0.6)
plt.ylim(-.3,.3)
plt.grid(True)
plt.show()

xar3,far3 = rf_bisect(f3,-1,1,10**-10,30)
plt.plot(xar3,far3,xrange,f3(xrange),xrange,y0(xrange))
plt.plot(xar3,far3,'.')
plt.title('F3 and midpoint error plot')
plt.grid(True)
plt.figure(2)
plt.show()

#For each of the functions f1(x), f2(x) and f3(x) of problem 1, compute the error at each iteration by
#assuming the root at the final iteration is the “true” value. For the purpose of diagnostics, do not
#take the absolute value – just define error as the difference of the root at a given iteration from the
#“true” value. Display plots of this error versus the iteration number. 

def error(f):
    #-----------------------------------------
    #goal: to create a function that uses the output arrays from the modified rf_bisect to plot the error
    #in: f is the function that is being used for bisection, and is the only input for this function
    #for loop: this loop takes a look at the last value in the list (which is assumed to be the true zero from the
    #bisection code) and takes the difference between it and every value in the list. These differences are then 
    #appended to the return list.
    #out: a list of error and the plot of the error list
    #-----------------------------------------
    xer = []
    xtemp,ftemp = rf_bisect(f,-1,1,10**-10,50)
    for i in range(len(xtemp)):
        error = xtemp[-1]-xtemp[i]
        xer.append(error)
    p = plt.plot(range(len(xer)),xer)
    plt.title('Error for function ' + str(f)[10:12])
    plt.xlabel('Iteration number')
    plt.ylabel('Error')
    return xer, p

plt.figure(3)
error(f1)
plt.figure(4)
error(f2)
plt.figure(5)
error(f3)