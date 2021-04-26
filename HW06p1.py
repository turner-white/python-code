# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:27:09 2020

@author: turne
"""
import numpy as np
from matplotlib import pyplot as plt

#Check Conditioning
def checkConditioning(tvec): #Make a checkConditioning function that can compute the norm and determinant
    t1 = tvec[0] #We know that t1 is the first element in tvec
    t2 = tvec[1] #t2 is the second element in tvec
    t3 = tvec[2] #t3 is the third element in tvec
    
    A = np.array([[1,t1,0.5*t1**2],[1,t2,0.5*t2**2],[1,t3,0.5*t3**2]]) #Initialize the solved A matrix
    normsum = 0 #Initialize sum value for euclidian norm

    for i in range(len(A)): #Loop over all rows of the matrix
        for j in range(len(A)): #Loop over all columns of the matrix
            normsum += (A[i][j])**2 #Square each value and add it to the sum value
        
    norm = np.sqrt(normsum) #Square root the overall sum value
    R = np.abs(np.linalg.det(A))/norm #Compute the ratio of determinant to norm
    return R

#def partc(dt):
    #t = np.array([0,dt,2*dt])
    #Rt = checkConditioning(t)

dtrange = np.arange(0.1,5.1,0.1) #Create a plotting range for delta t
Rlist = [] #Create an empty list to store corresponding R values
for dt in dtrange:
    t = np.array([0,dt,2*dt]) #Create the tvec matrix using even intervals of dt
    Rlist.append(checkConditioning(t)) #Compute the R value and append it to the plotting list
    
plt.plot(dtrange,Rlist) #Plot R as a function of dt
plt.title('R as a function of dt',fontsize=16)
plt.xlabel('dt',fontsize=14)
plt.ylabel('R',fontsize=14)
plt.show()
print('The highest R indicates the best conditioning. The largest R value is ' + str(max(Rlist)) + 
      ' and is found at t = ' + str(dtrange[np.argmax(Rlist)]))
#Part d
t2range = np.arange(0.1,10,0.1) #Create a second plotting range for t2 from 0-10
Rlist2 = [] #Create a second empty list to store corresponding R values
for t2 in t2range:
    t = np.array([0,t2,10]) #Create the tvec matrix with set t1 & t3 values, varying t2 across the range
    Rlist2.append(checkConditioning(t)) #Compute the R value and append it to the plotting list

plt.figure(1)
plt.plot(t2range,Rlist2) #Plot again, as a function of t2
plt.title('R as a function of t2', fontsize=16)
plt.xlabel('t2',fontsize=14)
plt.ylabel('R',fontsize=14)
plt.show()
print('The highest R indicates the best conditioning. The largest R value is ' + str(max(Rlist2)) + 
      ' and is found at t = ' + str(dtrange[np.argmax(Rlist2)]))
print()
#Part e
s1t = np.array([0,5,10]) #Initialize trial matrices
s2t = np.array([0,1,10])#Initialize trial matrices
s1x = np.array([0.30,4.425,14.30]) #Initialize trial matrices
s2x = np.array([0.30,0.665,14.30]) #Initialize trial matrices

def solver(tvec,xvec):
    t1 = tvec[0] #More formula convenience indexing
    t2 = tvec[1]
    t3 = tvec[2]
    x1 = xvec[0]
    x2 = xvec[1]
    x3 = xvec[2]
    
    A = np.array([[1,t1,0.5*t1**2],[1,t2,0.5*t2**2],[1,t3,0.5*t3**2]]) #Same matrix from check
    b = np.array([x1,x2,x3]) #Compute measuerment matrix
    
    ret = np.linalg.solve(A,b) #Solve the system of equations with builtin functions
    return ret

print(solver(s1t,s1x),' Are the solution values for strategy 1 (even time intervals)') #Display the solutions
print(solver(s2t,s2x), 'Are the solution values for strategy 2 (uneven time intervals)') #Display the solutions
print()
#part f
dx = 0.005 #Create error increment delta x
upper1x = np.array([0.30, 4.425 + dx, 14.30 + dx]) #Initialize upper bound for strategy 1's xvec
lower1x = np.array([0.30, 4.425 - dx, 14.30 - dx]) #Initialise lower bound for strategy 1's xvec
upper2x = np.array([0.30,0.665 + dx,14.30 + dx]) #Initialize upper bound for strategy 2's xvec
lower2x = np.array([0.30,0.665 - dx, 14.30 - dx]) #Initialize lower bound for strategy 2's xvec

print(solver(s1t,upper1x),'Are the upper bound solution values for s1') #Display the solutions and their differences
print(solver(s1t,lower1x), 'Are the lower bound solution values for s1')
print(solver(s2t,upper2x), 'Are the upper bound solution values for s2')
print(solver(s2t,lower2x), 'Are the lower bound solution values for s2')
print()

print(np.abs((solver(s1t,upper1x) - solver(s1t,lower1x))[1]) , 'Is the error in v0 accumulated in strategy 1')
print(np.abs((solver(s1t,upper1x) - solver(s1t,lower1x))[2]), 'Is the error in a accumulated in strategy 1')
print(np.abs((solver(s2t,upper2x) - solver(s2t,lower2x))[1]), 'Is the error in v0 accumulated in strategy 2')
print(np.abs((solver(s2t,upper2x) - solver(s2t,lower2x))[2]), 'Is the error in a accumulated in strategy 2')






    