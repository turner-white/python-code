# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:14:18 2020

@author: turne
"""

import numpy as np

def triSolve(A,b,upperOrLower):
    n = len(A) #Find the dimensions of our nxn matrix by counting the number of rows
    ret = np.zeros(n) #Initialize our answer array with n rows for n solution variables
    #print(n)
    #lower
    if upperOrLower == 0: #Determine whether the input matrix is upper or lower
        i = 0 #Initialize the i index at 0 to access the rows in order
        while i < n: #Stop indexing when i = n-1 or hits the last element of the array
            sums = 0 #Initialize a temporary sums variable
            j = 0 #Initialize the j index at 0 to access the columns in order
            while j < i: #Stop indexing when j = i-1 and ignore the parts of the array that are 0
                sums += A[i][j]*ret[j] #Update the sums variable with the known products of A and x in forward sub
                j += 1 #Increment j and move to the next column
            ret[i] = (1/A[i][i])*(b[i]- sums) #Set the ith solution element to its calculated value
            i += 1 #Increment i and move to the next row
        return ret
    
    #upper
    elif upperOrLower == 1: #Determine whether the input matrix is upper or lower
        i = n-1 #set i to start at the last index of the array
        while i >= 0: #Stop indexing when i has moved backwards to the first element in the array
            #print(i, ' is i')
            sums = 0 #Initialize a temporary sums variable
            j = n-1 #set j to n-1 and start at the last column of the array
            while j >= i: #Stop indexing when j reaches i and produce 22, 12, 11, 02, 01, 00 pattern
                #print(j, 'is j')
                sums += A[i][j]*ret[j] #Update the sums variable with the known products of A and x in back sub
                #print(sums)
                j -= 1 #Increment j by -1 and move one column backwards
            ret[i] = (1/A[i][i])*(b[i]-sums) #Set the ith solutionn element to its calculated value
            i -= 1 #Increment i by -1 and move one row backwards
        return ret
    
    else:
        return('Please enter a valid upperOrLower value')
#Part b
def checkSolve(A, x, b): #Define a function with 3 inputs A, x, and b that computes the residuals
    dot = np.dot((A),x) #Use np.dot to calculate A*x
    res = dot - b #Subtract b so that res = 0
    return res

#Part c
A1 = np.array([[2,4,5],[0,2,-4],[0,0,5]]) #Initialize the first test array given in part c
b1 =np.array([-4,9,4]) #Initialize the first test measurement array given in part c

A2 = np.array([[9,0,0],[-4,2,0],[1,0,5]]) #Initialize the second test array
b2 = np.array([8,1,4]) #And its corresponding test measurement array

x1 = (triSolve(A1,b1,1)) #Compute the solutions for the first array, which we know is upper
x2 = (triSolve(A2,b2,0)) #Compute the solutions for the second array, which we know is lower

print(x1, ' is the solution column for A1')
print(checkSolve(A1,x1,b1), ' are the residuals for this solution')
print()

print(x2, 'is the solution column for A2')
print(checkSolve(A2,x2,b2), 'are the residuals for this solution')
print()
#Part d
def matmaker(n, upperOrLower): #Create a function that creates an nxn random matrix in upper or lower form
    a = np.random.random((n,n)) #Create a random nxn matrix
    b = np.random.random((n)) #Create a random n measuremtne matrix
    
    if upperOrLower == 1: #If the matrix requested is upper, then this statement conditions it
        for i in range(1,len(a)): #Loop over all rows except for the first one
            for j in range(i): #Loop over all columns starting at i to create the triangle
                a[i][j] = 0 #Update the target value with 0 
    
    if upperOrLower == 0: #If the matrix requested is lower, then this statement conditions is
        for i in range(len(a)): #Loop over all rows
            for j in range(i+1,len(a)): #Loop over all columns from i+1 to the last column and miss the diagonal
                a[i][j] = 0 #Update the target value with 0
                  
    return a, b


sizelist = [3,10,30,100] #Initialize list of test sizes given in homework file
for e in sizelist: #Use a for loop to print for me and randomize
    uplow = np.random.randint(0,1) #Create a random number between 1 and 0
    if uplow > 0.5: #If the number is above 0.5, then make an upper matrix
        uplow = 1 #This process adds another element of randomization to help test robustness
    elif uplow <= 0.5: #If the number is below 0.5, then make a lower matrix
        uplow = 0 #It also makes sure that the random matrices test both conditions in triSolve
        
    M, m = matmaker(e,uplow) #Create test arrays
    x = triSolve(M,m,uplow) #Solve test arrays
    #print(x) #Uncomment this line if you want to see the solution arrays my code produces
    print(np.mean(checkSolve(M,x,m)), ' is the mean of the residuals for size'+ str(e) + ' :)')
    print(np.std(checkSolve(M,x,m)), ' is the standard deviation '+ str(e) + ' :)')
    print() #Print :)
    