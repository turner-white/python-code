# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:18:59 2020

@author: turne
"""
import numpy as np
from matplotlib import pyplot as plt
def function(n): #define a function that does the specified things so that I can easily call it 1000 times later
    A = np.random.random((n,n)) #create an n by n matrix of random values
    b = np.random.random(n) #create a 1 by n measurement matrix of random values
    Ainv = np.linalg.inv(A) #compute the inverse of A
    x = np.dot(Ainv,b) #compute x by solving the equation Ax = b. We know x = A^-1*b
    res = np.dot(A,x) - b #compute the residuals

    RA = (np.linalg.det(A)/np.linalg.norm(A)) #compute the ratio RA as in equation 5
    CA = np.linalg.norm(A)*np.linalg.norm(Ainv) #compute the condition number
    res = np.linalg.norm(res) #compute the norm of the residual matrix
    
    return RA,CA,res #return the 3 requested values for insertion into matrices

Rlist = np.zeros(1000) #initialize a 1x1000 matrix for the RA values
clist = np.zeros(1000) #initialize a 1x1000 matrix for the condition values
reslist = np.zeros(1000) #initialize a 1x1000 matrix for the residual norms

for i in range(1000): #loop 1000 times
    R, C, r = function(10) #call the function to make a random 10x10 matrix
    Rlist[i] = R #store the RA value
    clist[i] = C #store the condition number
    reslist[i] = r #store the residual norm value
    
logr = np.log(Rlist) #compute the log of the RA array
logc = np.log(clist) #compute the log of the condition number array
logres = np.log(reslist) #compute the log of the reslist array
plt.figure(0) #create the first plot
plt.scatter(logc,logr) #plot the log log RA vs condition number
plt.title('Log of RA vs Log of Condition Number')
plt.figure(1) #establish a second plot
plt.scatter(logc, logres) #plot the log log residual norm vs condition number
plt.title('Log of Residual Norm vs Log of Condition Number')