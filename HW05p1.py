# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:14:18 2020

@author: turne
"""

import numpy as np
#Using np.linalg.solve

A1 = np.array([[3,-3,3],[-3,5,1],[3,1,5]]) #Initialize the matrix given in problem 2.1
b1 = np.array([[9],[-7],[12]]) #And the solution column given for the matrix

x1 = np.linalg.solve(A1,b1) #Call np.linalg.solve and set the output to an x variable

A2 = np.array([[4,8,20],[8,13,16],[20,16,-91]]) #Initialize the matrix given in problem 2.2
b2 = np.array([[24],[18],[-119]]) #And the solution column given for the matrix

x2 = np.linalg.solve(A2,b2) #Call np.linalg.solve and set the output to another x variable

print(x1, ' Is the solution for 2.1 using linalg.solve')
print(x2, ' Is the solution for 2.2 using linalg.solve')
print()

#Checking the residual with np.linalg.dot

res1 = np.dot(A1,x1) - b1 #Use np.dot to evaluate A*x
res2 = np.dot(A2,x2) - b2 #Do it again for problem 2.2

print(res1, 'Are the residuals for 2.1')
print(res2, 'Are the residuals for 2.2')
print()

#Finding the inverse (c)

#We know that analytically x = A^-1 * b 

A1i = np.linalg.inv(A1) #Use linalg.inv to take the inverse of the matrix in 2.1
A2i = np.linalg.inv(A2) #Use linalg.inv to take the inverse of the matrix in 2.2

x1i = np.dot(A1i,b1) #Use np.dot to evaluate A^-1*b
x2i = np.dot(A2i,b2) #Do it again for problem 2.2

print(x1i, 'Is the solution for 2.1 calculated using linalg.inv')
print(x2i, 'Is the solution for 2.2 calculated using linalg.inv')
print()

#Problem 17 in textbook (d,e,f)
def solver(R,v): #Define a solving function that can take an R (resistance) and v (voltage) input
    A3 = np.array([[50+R,-1* R,-30],[-R, 65+R, -15],[-30,-15,45]]) #Initialize matrix equation A
    b3 = np.array([[0],[0],[v]]) #Initialize the measurment column b
    i = np.dot(np.linalg.inv(A3),b3) #Compute the solution matrix using linalg.inv and np.dot
    
    res = np.dot(A3,i) - b3 #Compute the residuals as in part b
    if v == 120: #Print condition to display residuals only for R=5 
        print(res, ' Is the residual for 120V')
        print()
    return(i) #Return the solution matrix

vlist = [120,60,30] #Initialize set of voltage inputs
for e in vlist: #Use a for loop to print and solve for me instead of typing a bunch of print statements
    print(solver(5,e), 'Is the solution for ' + str(e) + ' volts.')
    print()
    




