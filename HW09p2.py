# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:40:25 2020

@author: turne
"""
import numpy as np
from matplotlib import pyplot as plt

def CreateSystem(kvec,mvec): #Define our function as specified
    n = len(mvec) #Calculate the length of the matrix
    ret = np.zeros((n,n)) #Create a nxn storage matrix to return
    
    ret[0,0] = (-1*kvec[0]-kvec[1])/mvec[0] #Set the first value of the first row
    ret[0,1] = (kvec[1])/mvec[0] #Set the second value of the first row
    
    for i in range(1,n-1): #Loop from the second row to the second to last row
        ret[i,i-1] = (kvec[i])/mvec[i] #Set the i-1 value in the ith row
        ret[i,i] = (-1*kvec[i]-kvec[i+1])/mvec[i] #Set the i value in the ith row
        ret[i,i+1] = (kvec[i+1])/mvec[i] #Set the i+1 value in the ith row
        
    ret[n-1,n-2] = kvec[n-1]/mvec[n-1] #Set the second to last value of the last row
    ret[n-1,n-1] = (-1*kvec[n-1]-kvec[n])/mvec[n-1] #Set the last value of the last row
    
    return ret #Return the system

ktest = [1,1,1] #Define test parameters
mtest = [1,1] #Define test parameters

print(CreateSystem(ktest,mtest)) #Display the created system in case 1
print()
test = CreateSystem(ktest,mtest) #Set the system equal to a variable
#part c
w,v = np.linalg.eig(test) #Compute the eigenvalues and vectors
print(w, ' Are the eigenvalues of matrix c.') #Display to the console
print(v, 'This is the eigendecomposition of the test matrix c.') #Display to the console
print()
#part d
ktest2 = [1,1,1,1] #Define test parameters
mtest2 = [1,1,1] #Define test parameters
w2,v2 = np.linalg.eig(CreateSystem(ktest2,mtest2)) #Compute the eigencalues and vectors again for system 2
print(w2, ' Are the eigenvalues of matrix d.') #Display to the console
print(v2, 'This is the eigendecomposition of the test matrix d.') #display to the console
print()
#part e
N = 1000 #Set the number of masses
bonds1 = np.zeros(N+1) #Initialize the kvec array
for i in range(len(bonds1)): #Loop over all indices in bonds
    bonds1[i] = 1 #Set equal to 1 because the exact value of k is not important
atoms1 = np.zeros(N) #Initialie the mvec array
for i in range(N): #Loop over all indices in atoms1
    if i % 2 == 0: #If value is even
        atoms1[i] = 1.5 #Set to 1.5
    else:
        atoms1[i] = 1 #Otherwise make it 1

crystal1 = CreateSystem(bonds1,atoms1) #Create the system for crystal 1
eig2 = np.linalg.eig(crystal1)[0] #Compute the eigenvalues

bin1 = [] #Set an empty bin for histogram plotting
s1 = -3.40 #Create starting bin number
while s1 <= 0: #While bin number is less than 0
    bin1.append(s1) #Put the number in the bin
    s1 += 0.05 #Increment by 0.05 for the next bin
    
plt.hist(eig2,bin1) #Display the histogram plot
plt.show() #Show the plot

bonds2 = np.zeros(N+1) #Initialize a second kvec array
for i in range(len(bonds2)): #Set everything to 1 again
    bonds2[i] = 1
atoms2 = np.zeros(N) #Initialize a second mvec array
for i in range(N): #Loop over all indices
    if i % 2 == 0: #Determine if even
        atoms2[i] = 1.2 #Set to 1.2 instead of 1.5
    else:
        atoms2[i] = 1 #Otherwise set to 1

crystal2 = CreateSystem(bonds2,atoms2) #Create the system for crystal 2
eig3 = np.linalg.eig(crystal2)[0] #Compute the eigenvalues

bin2 = [] #Set an empty bin for histogram plotting
s2 = -3.75 #Create starting bin value
while s2 <= 0: #While bin is less than 0
    bin2.append(s2) #Put the number in the bin list
    s2 += 0.05 #Increment by 0.05
    
plt.hist(eig3,bin2) #Display the second histogram plot
plt.show() #Show the plot



