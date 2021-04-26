# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 18:41:20 2020

@author: turne
"""
import numpy as np
from matplotlib import pyplot as plt

#part c
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

#Hardcode the 9x9 temperature matrix because idk how to generate it procedurally
Aa = np.array([[-4,1,0,1,0,0,0,0,0],[1,-4,1,0,1,0,0,0,0],[0,1,-4,0,0,1,0,0,0],
               [1,0,0,-4,1,0,1,0,0],[0,1,0,1,-4,1,0,1,0],[0,0,1,0,1,-4,0,0,1],
               [0,0,0,1,0,0,-4,1,0],[0,0,0,0,1,0,1,-4,1],[0,0,0,0,0,1,0,1,-4]])

b1 = np.array([0,0,-100,0,0,-100,-200,-200,-300]) #Initialize the corrected b matrix


Temp = myJacobi(Aa,b1,1,10**(-4))[1] #Store the return values of myJacobi for heatmap plotting

Tempbruh = Temp.reshape(3,3) #Reorganize the values into a 3x3 matrix for imshow

print('-Temperature values organized according to the mesh points in the textbook-')
print(Tempbruh) #Display the temperature matrix

plt.imshow(Tempbruh, cmap='hot') #Make a cool heatmap of the temperatures
plt.title('Heatmap of the temperature mesh')