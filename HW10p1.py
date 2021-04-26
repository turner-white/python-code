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

#Initialize test arrays
A1 = np.array([[1.01,0.99],[0.99,1.01]])
b1 = np.array([[2.0],[2.0]])
A2 = np.array([[1.5,0.5],[0.5,1.5]])
b2 = np.array([[2.],[2.]])

#Make nice looking print statements
print('The number of iterations and solution matrix for A1')
print(myJacobi(A1,b1,1.0,10**(-4)))
print()

print('The number of iterations and solution matrix for A2')
print(myJacobi(A2,b2,1.0,10**(-4)))

#Initialize part b test arrays
A3 = np.array([[9.,10.,2.],[1.,6.,3.],[10.,-1.,2.]])
b3 = np.array([[7.],[8.],[1.]])

true = np.dot(np.linalg.inv(A3),b3) #Compute the true solution matrix
wrange = np.arange(0.01,0.35,0.01) #Initialize a wrange for plotting
temp = [] #Initialize a list for the iteration count
bruh = [] #Initialize a list for the true error estimation
for w in wrange: #Loop over every value in wrange
    temp.append(myJacobi(A3,b3,w,10**(-4))[0]) #Evaluate the number of iterations and add to the list
    bruh.append(np.linalg.norm(true-myJacobi(A3,b3,w,10**(-4))[1])) #Do the same for true error

plt.plot(wrange,temp)
plt.grid(True)
plt.title('Number of iterations n vs. relaxation w')
plt.show()
#Make some more nice print statements
print()
print(max(temp), 'Is the max iters for a w of ' + str(wrange[np.argmax(temp)]))
print(min(temp), 'Is the min iters for a w of ' + str(wrange[np.argmin(temp)]))

plt.plot(wrange,bruh)
plt.grid(True)
plt.title('Norm of true error vs. relaxation w')
plt.show()

                
    
    