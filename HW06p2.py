# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:27:10 2020

@author: turne
"""

# HW6 Problem 2 template file -- Turner White

#--Do not modify below this line--#
import numpy as np

# this function inputs an nxn matrix "Ainput" and an nx1 column matrix "binput"
# inputs should be floating-point type
# it performs Gaussian elimination and outputs the eliminated new matrices A and b
# where "A" is nxn upper triangular, and "b" is an nx1 column matrix
def GaussElimin(Ainput,binput):
    n=len(binput)
    A = Ainput.copy() # make copies so as not to write over originals
    b = binput.copy()
    # loop over pivot rows from row 1 to row n-1 (i to n-2)
    for i in range(0,n-1):
        # loop over row to be zero'ed from row j+1 to n (j+1 to n-1)
        for j in range(i+1,n):
            c = A[j,i]/A[i,i] # multiplicative factor to zero point
            A[j,i] = 0.0 # we know this element goes to zero
            A[j,i+1:n]=A[j,i+1:n]-c*A[i,i+1:n] # do subtraction of two rows
            b[j] = b[j]-c*b[i] # do substraction of b's as well
    return (A,b)  # return modified A and b

#---Do not modify above this line--#

#Part b
A1 = np.array([[4.,-2.,1.],[-3.,-1.,4.],[1.,-1.,3.]]) #Initialize given A1 matrix
b1 = np.array([[15.],[8.],[13.]]) #Initialize given b1 matrix
x = np.array([[2.],[-2.],[3.]]) #Initialize given solution matrix

newA1, newb1 = GaussElimin(A1,b1) #Use Gaussian Elimination to convert to upper form
print("-----Let's initialize and construct the matrices-----") #Just a bunch of print statements for things
print(A1, 'Input matrix A')                                    #to look nice :)
print()
print(newA1, 'Output matrix following Gaussian Elimination')

print()

print(b1, 'Input measurment matrix')
print()
print(newb1, 'Output measurement matrix following Gaussian Elimination')
print()
print('-----Now to test and make sure that they work-----')

res1 = np.dot(A1,x) - b1 #Compute residual as in HW05
res2 = np.dot(newA1,x) - newb1 #Do it again

print(res1, 'Are the residuals using the input matrices')
print()
print(res2, 'Are the residuals using the output matrices')
print()
print('Because both residuals are very close to 0, we know that both forms are solutions.')

#Part c
A2 = np.array([[0.,2.,0.,1.],[2.,2.,3.,2.],[4.,-3.,0.,1.],[6.,1.,-6.,-5.]]) #Initialize the second set of 
pA2 = np.array([[6.,1.,-6.,-5.],[0.,2.,0.,1.],[2.,2.,3.,2.],[4.,-3.,0.,1.]])#matrices, and permute each one
b2 = np.array([[0.],[-2.],[-7.],[6.]])
pb2 = np.array([[6.],[0.],[-2.],[-7.]])
x2 = np.array([[-0.5],[1.],[1/3],[-2.]]) #Initialize the second solution matrix, no permutation

newA2, newb2 = GaussElimin(pA2,pb2) #Use Gaussian Elimination again for A2
print('-----Part d testing with permuted 4x4 array-----') #More print statements to look nice :)
print(pA2, 'Input matrix A after permutation')
print()
print(pb2, 'Input measurement matrix after permutation')
print()
print(newA2, 'Output matrix following Gaussian Elimination')
print()
print(newb2, 'Output measuerment matrix following Gaussian Elimination')
print()
print('-----Now to test the residuals again-----')

res3 = np.dot(A2,x2) - b2 #Compute residuals again
res4 = np.dot(newA2,x2) - newb2 #And again

print(res3, "Are the residuals using the input matrices")
print()
print(res4, ' Are the residuals using the output matrices')
print()
print('Because both residuals are very close to 0, we know that both forms are solutions.')



