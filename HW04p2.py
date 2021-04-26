# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:33:52 2020

@author: turne
"""

# Homework 4, Problem 2 Template
# Amy Oldenburg

import numpy as np
import math
import sys

## module error
''' err(string).
    Prints 'string' and terminates program.
'''    
def err(string):
    print(string)
    input('Press return to exit')
    sys.exit(0)

## module swap
''' swapRows(v,i,j).
    Swaps rows i and j of a vector or matrix [v].

    swapCols(v,i,j).
    Swaps columns of matrix [v].
'''
def swapRows(v,i,j):
    if len(v.shape) == 1:
        v[i],v[j] = v[j],v[i]
    else:
        v[[i,j],:] = v[[j,i],:]
        
def swapCols(v,i,j):
    v[:,[i,j]] = v[:,[j,i]]
    
## module gaussPivot
''' x = gaussPivot(a,b,tol=1.0e-12).
    Solves [a]{x} = {b} by Gauss elimination with
    scaled row pivoting
'''    
def gaussPivot(a,b,tol=1.0e-12):
    n = len(b)
    
  # Set up scale factors
    s = np.zeros(n)
    for i in range(n):
        s[i] = max(np.abs(a[i,:]))
            
    for k in range(0,n-1):
        
      # Row interchange, if needed
        p = np.argmax(np.abs(a[k:n,k])/s[k:n]) + k
        if abs(a[p,k]) < tol: err('Matrix is singular')
        if p != k:
            swapRows(b,k,p)
            swapRows(s,k,p)
            swapRows(a,k,p)
            
      # Elimination
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
    if abs(a[n-1,n-1]) < tol: err('Matrix is singular')
                   
  # Back substitution
    b[n-1] = b[n-1]/a[n-1,n-1]
    for k in range(n-2,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b

## module newtonRaphson2
''' soln = newtonRaphson2(f,x,tol=1.0e-9).
    Solves the simultaneous equations f(x) = 0 by
    the Newton-Raphson method using {x} as the initial
    guess. Note that {f} and {x} are vectors.
'''
def newtonRaphson2(f,x,tol=1.0e-9):
    
    def jacobian(f,x):
        h = 1.0e-4
        n = len(x)
        jac = np.zeros((n,n))
        f0 = f(x)
        for i in range(n):
            temp = x[i]
            x[i] = temp + h
            f1 = f(x)
            x[i] = temp
            jac[:,i] = (f1 - f0)/h
        return jac,f0
    
    for i in range(30):
        jac,f0 = jacobian(f,x)
        if math.sqrt(np.dot(f0,f0)/len(x)) < tol:
            return x
        dx = gaussPivot(jac,-f0)
        x = x + dx
        if math.sqrt(np.dot(dx,dx)) < tol*max(max(abs(x)),1.0): return x
    print('Too many iterations')

# EDIT BELOW HERE

#define each function, using separate values of R and theta for each
def f1(x):
    return x[0]*(1+x[1]*np.sin(-(np.pi/6)+x[2]))**-1 - 6870
                 
def f2(x):
    return x[0]*(1+x[1]*np.sin(x[2]))**-1 - 6728

def f3(x):
    return x[0]*(1+x[1]*np.sin((np.pi/6)+x[2]))**-1 - 6615     
#define a big fucntion that combines the others and stacks them like they are a matrix
def F(x):
    return np.array([f1(x),f2(x),f3(x)])        
#initial guess               
xtemp = np.array([6870,1,(np.pi/4)])

#print(F(xtemp))
print(newtonRaphson2(F,xtemp))
y = newtonRaphson2(F,xtemp)

#sin is maximized at pi/2

theta = np.pi/2 - y[2]
theta_deg = (theta - 2*np.pi)*(180/np.pi)

R = y[0]/(1+y[1]*np.sin(theta + y[2]))
print(R)
print(theta_deg)
