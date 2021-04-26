# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:22:52 2020

@author: turne
"""
# Template File for Homework 3, Problem 4
# PHYS 331
# Amy Oldenburg

## module newtonRaphson

# has been modified to strip bisection aspects of the code
# is generally UNSAFE, but can be used for specific case of Problem 4

import numpy as np
def newtonRaphsonMOD(f,df,a,b): # YES YOU MAY MODIFY!
    from numpy import sign
    temp = []   #initialized list for error value appending
    fa = f(a)
    if fa == 0.0: return a
    fb = f(b)
    if fb == 0.0: return b
    if sign(fa) == sign(fb): 
        print('Root is not bracketed')
        return []
    x = 0.5*(a + b)                    
    for i in range(30):
        fx = f(x)
      # Try a Newton-Raphson step    
        dfx = df(x)
        
      # If division by zero, push x out of bounds
        try: dx = -fx/dfx
        except ZeroDivisionError: dx = b - a
        
        xtemp = x
        x = x + dx
        
        temp.append(np.abs(x-xtemp))
        
    return np.array(temp)   #modification here to be sure and return an array of the error instead of a list
#----------------------------------------------------------------

#b
from matplotlib import pyplot as plt
    
#define the specified function and derivative as functions
def f1(x):
    return (x+10)*(x-25)*(x**2 + 45)

def df1(x):
    return 4*x**3 - 45*x**2 - 410*x - 675


elist = (newtonRaphsonMOD(f1,df1,-50,0))
print(elist[:9])

#c
#------------------------------------------------------------------
#error
#intent: to create separate plots for each error line and compare linearity between each one
#in: m this is the value of m (convergence) that the data is fit to
#for: this loops over the list of error values and takes the difference between the n+1 and n terms
#out: ret is the plot of error and temp is the list of error differences
#------------------------------------------------------------------
def error(m):
    elist = (newtonRaphsonMOD(f1,df1,-50,0))[:8]
    temp = [] #initialize a list for the calculated error values
    for i in range(len(elist)-1):
        c = (elist[i+1])/((elist[i]**m))
        temp.append(c)
    ret = plt.plot(range(1,(len(temp)+1)),temp)
    plt.ylim(-3,3)
    plt.title('Order of Convergence Plot with m = ' + str(m))
    plt.figure((m/0.5))
    plt.show()
    return ret, temp

error(1)
error(1.5)
error(2)


        
    