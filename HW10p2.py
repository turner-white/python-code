# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 18:41:19 2020

@author: turne
"""

import numpy as np
from matplotlib import pyplot as plt

def myJacobi(A,b,w,tol):
    n = len(A) #Find the size of the square matrix input
    L = np.zeros((n,n)) #Initialize the lower matrix
    D = np.zeros((n,n)) #Initialize the diagonal matrix
    U = np.zeros((n,n)) #Initialize the upper matrix
    
    for i in range(n): #Loop over every row index in A
        for j in range(n): #Loop over every column index in A
            if i > j: #If the row index is greater than the column index
                L[i][j] = A[i][j] #Set to the lower matrix
            if i == j: #If the indices are equal and on the diagonal
                D[i][j] = A[i][j] #Set to the diagonal matrix
            if i < j: #If the row index is less than the column index
                U[i][j] = A[i][j] #Set to the upper matrix
            
    Dinv = np.zeros((n,n)) #Initialize an array for the inverse of D
    for i in range(n): #Loop over all diagonal indices
        Dinv[i][i] = 1/(D[i][i]) #Compute the inverse by identity
    
    def iterate(xn): #Define a function that will compute the iteration operation g(x)
        a = np.dot((L+U),xn) #Take the inner dot product
        x = np.dot((-1*Dinv),a) #Compute the outer dot product following matrix operation order
        return x + np.dot(Dinv,b) #Return the dot product and sum with b
        
    def norm(a): #Define a function that will compute the euclidian norm
        summ = 0 #Initialize a sum counter
        a = np.atleast_2d(a) #Make sure that the passed array has 2 dimensions to ensure looping works
        for i in range(len(a)): #Loop over every row index
            for j in range(np.size(a,axis=1)): #Loop over every column index, if applicable
                summ += (a[i][j])**2 #Increment the sum according to the norm equation
                
        summ = np.sqrt(summ) #Take the square root of the final sum
        
        return summ #Return the sum value
    
    xstart = np.dot(Dinv,b) #Initialize an xstart
    xn = xstart #Iterate once to define xn
    xn1 = w*iterate(xn) + (1-w)*xn #Iterate once to define xn1
    
    n = 1 #Start the iteration counter at 1 because of the above steps
    
    while norm(xn-xn1) >= tol: #Iterate until the tolerance requirement is met
        xn = xn1 #Set xn equal to xn1
        xn1 = w*iterate(xn) + (1-w)*xn #Compute the iteration with the relaxation factor
        n += 1 #Increment the counter by 1
    
    return (n,xn1) #Return the requested values

def Agen(n): #Create a function to create an n by n derivative operator 
    A = np.zeros((n,n)) #Initialize an array of 0s
    A[0][0] = -2 #Set the first value
    for i in range(len(A)): #Loop over all diagonal indices
        A[i][i] = -2 #Set the diagonal to -2
        A[i][i-1] = 1 #Set the value to the left of the diagonal equal to 1
        A[i-1][i] = 1 #Set the value above the diagonal equal to 1
    
    return A #Return the matrix

xrange = np.linspace(0,2*np.pi-(2*np.pi/100),100) #Define a range of xvalues to compute and plot over

brange = -4*np.pi*np.sin(np.linspace(0,2*np.pi-(2*np.pi/100), 100)) #Create an array of b values


A1 = Agen(100) #Create a 100x100 Derivative operator array
#print(A1)
hne = xrange[3]-xrange[2] #Compute the step size in x values from two adjacent values

Ah = (1/(hne**2))*A1 #Multiply the A matrix by the normalization factor 1/h^2
b1 = brange #Create a copy of the brange for computation and plotting

#print(b1)
#print(len(brange))
#print(myJacobi(Ah,b1,1.0,10**(-4)))

def anal(x,c1,c2): #Create a function which computes the analytical solution
    return 4*np.pi*np.sin(x) + c1*x + c2 #Return the function

direct = np.dot(np.linalg.inv(Ah),b1) #Compute the directinv solution using linalg.inv

#Create cool plots
plt.plot(xrange,myJacobi(Ah,b1,1.0,10**(-4))[1])
plt.plot(xrange,direct) 
plt.plot(xrange,anal(xrange,0,0))
plt.legend(('myJacobi','directinv','anal'))
plt.grid(True)
plt.show()