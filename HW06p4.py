# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:27:11 2020

@author: turne
"""

import numpy as np

# this function inputs an nxn matrix "Ainput" and an nx1 column matrix "binput"
# inputs should be floating-point type
# it performs Gaussian elimination and outputs the eliminated new matrices A and b
# where "A" is nxn upper triangular, and "b" is an nx1 column matrix
def LUdecomp(mat):
    n=len(mat)
    Au = mat.copy() # make copies so as not to write over originals
    Al = np.zeros((n,n)) # initialize zero matrix for lower form

    for i in range(n): #
        Al[i][i] = 1 # set the diagonal equal to 1
    
    # loop over pivot rows from row 1 to row n-1 (i to n-2)
    for i in range(0,n-1):
        # loop over row to be zero'ed from row j+1 to n (j+1 to n-1)
        for j in range(i+1,n):
            c = Au[j,i]/Au[i,i] # multiplicative factor to zero point
            Al[j,i] = c
            #print(c)
            Au[j,i] = 0.0 # we know this element goes to zero
            Au[j,i+1:n]=Au[j,i+1:n]-c*Au[i,i+1:n] # do subtraction of two rows
             # set the elements of the lower array equal to the multiplicative factor
            # do substraction of b's as well
            
    return (Au,Al)  # return modified A and b

A = np.array([[4.,-2.,1.],[-3.,-1.,4.],[1.,-1.,3.]])
A2 = np.array([[6.,1.,-6.,-5.],[0.,2.,0.,1.],[2.,2.,3.,2.],[4.,-3.,0.,1.]])#matrices, and permute each one
a, b = LUdecomp(A)
a2, b2 = LUdecomp(A)
print('-----Test the outputs from A, the 3x3 matrix in problem 2-----')
print(a)
print()
print(b)
print()
print(np.dot(b,a), 'Is the dot product LU, which is equal to A')
print()
print('-----Test the outputs from A2, the 4x4 matrix in problem 2-----')
print(a2)
print()
print(b2)
print()
print(np.dot(b2,a2), 'Is the dot product LU, which is equal to A')