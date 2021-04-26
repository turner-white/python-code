# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:40:24 2020

@author: turne
"""

import numpy as np 
A = np.random.random((4,4)) #Generate the random 4x4 array
w, v = np.linalg.eig(A) #Compute the eigenvalues and eigenvectors of A and store in documentation variables
for i in range(len(w)): #Loop over every inndex of the eigenvalue list
    print('The ' + str(i) + " index eigenvalue is: ", w[i]) #Print the eigenvalue with some nice text
    
print()
bruh = np.dot(A,v[:,0]) #Compute the dot product of A and the eigendecomposition matrix A*w1
print(bruh) #Display to the console

bruh2 = v[:,0]*w[0] #Compute the dot product of the eigenvalue and the eigenvector (w1 and v1)
print(bruh2) #Display to the console
print('As we can see, these two outputs are equal.')

diag = np.dot(np.linalg.inv(v),np.dot(A,v)) #Compute the dot product of P-1 * A * P where P is the eigendecomp
#print() #vector v                -------Uncomment these to see the original diag-------
#print(diag) #Display to the console
for i in range(len(diag)): #Loop over all rows in diag
    for j in range(len(diag)): #Loop over all columns
        if np.abs(diag[i,j]) < 10**-10: #If the value is really close to 0
            diag[i,j] = float(0) #Just replace it with 0 for ease of viewing.
print()
print(diag)