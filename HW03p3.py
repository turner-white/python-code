# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:22:51 2020

@author: turne
"""
# Template File for Homework 3, Problem 3
# PHYS 331
# Amy Oldenburg
#----------------------------------------------   
# DO NOT MODIFY BETWEEN THIS LINE AND ONE BELOW
## module newtonRaphson
''' root = newtonRaphson(f,df,a,b,tol,maxiter).
    Finds a root of f(x) = 0 by combining the Newton-Raphson
    method with bisection. The root must be bracketed in (a,b).
    Calls user-supplied functions f(x) and its derivative df(x).   
    tol is the tolerance, and maxiter is the maximum number of iterations..
''' 
def newtonRaphson(f,df,a,b,tol,maxiter): 
    from numpy import sign
    
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if sign(fa) == sign(fb): 
        print('Root is not bracketed')
        return []
    x = 0.5*(a + b)                    
    for i in range(maxiter):
        fx = f(x)
        if fx == 0.0: return x
      # Tighten the brackets on the root 
        if sign(fa) != sign(fx): b = x  
        else: a = x
      # Try a Newton-Raphson step    
        dfx = df(x)
      # If division by zero, push x out of bounds
        try: dx = -fx/dfx
        except ZeroDivisionError: dx = b - a
        x = x + dx
      # If the result is outside the brackets, use bisection  
        if (b - x)*(x - a) < 0.0:  
            dx = 0.5*(b - a)                      
            x = a + dx
      # Check for convergence     
        if abs(dx) < tol*max(abs(b),1.0): return x
    print('Too many iterations in Newton-Raphson')
## ADD your code below this line
#----------------------------------------------
import numpy as np
from matplotlib import pyplot as plt
#defining the given function and functionn derivative calculated by using the product rule
def f1(x):
    return np.cosh(x)*np.cos(x) + 1

def df1(x):
    return np.sinh(x)*np.cos(x)-np.cosh(x)*np.sin(x)

#plotting the graph to visually evaluate roots and derivative values
xrange = np.arange(-10,10,0.001)
plt.plot(xrange,f1(xrange),xrange,np.abs(df1(xrange)))
plt.ylim(-10,10)
plt.grid()

#print(newtonRaphson(f1,df1,4,5,10**-15,30))
#-----------------------------------------------
#freq
#in: n is the nth natural frequency, up to 2, and determines the output of the function
#if: This is the condition that sets ranges for the 1st and 2nd natural frequency
#out: outputs the solved value of fi from the equation given in the book
#-----------------------------------------------
def freq(n):
    if n == 1:
        a = 1
        b = 3
    if n == 2:
        a = 4
        b = 5
    #set the hard-coded variables for the equation that are supplied by the textbook
    m = (0.9)*(.025)*(.0025)* 7850
    b= (newtonRaphson(f1,df1,a,b,10**-15,30))
    E = 200*10**9
    I = (1/12)*(.025)*(.0025**3)
    L = 0.9
    return (1/(2*np.pi))*((b**4 * E*I)/(m * L**3))**(1/2)

print(freq(1), 'Hz is the first natural frequency found using NR')
print(freq(2), 'Hz is the second natural frequency found using NR')

    