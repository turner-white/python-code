# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 18:40:05 2020

@author: turne
"""

import numpy as np
from matplotlib import pyplot as plt
import time
from scipy.stats import linregress

#Part A

def myDFT(N): #create the myDFT function as requested. N is the size of the generated array
    starttime = time.time() #Start the timer
    
    h = np.random.random(N) #Generate the random array of size N
    H = np.zeros(N) #Initialize a storage array for the transformed values
    
    for n in range(N): #Loop over every n value in N-1
        summ = 0 #Initialize a sum variable
        for k in range(N): #Loop over every k value in N-1
            summ += h[k]*np.exp((-1j*2*np.pi*k*n)/N) #Increment the sum variable with the equation
        H[n] = summ #Update the storage array with transformed values
    
    runtime = time.time() - starttime #Calculate the time elapsed
    
    return H, runtime #Return the transformed array and the runtime. Here all we want is the runtime

#print(myDFT(6))

Nrange = np.array([10,20,50,100,200,500,1000]) #Generate a test range of N values for myDFT
timelist = np.zeros(len(Nrange)) #Initialize an array for storing the runtime values

for i in range(len(Nrange)): #Loop over all values in Nrange
    timelist[i] = myDFT(Nrange[i])[1] #Record the time elasped by myDFT for each N value
    
plt.plot(np.log(Nrange),np.log(timelist)) #Plot the log-log of timelist and Nrange
plt.scatter(np.log(Nrange),np.log(timelist)) #Overlay with scatter points to look cool
plt.show() #Calculate the slope using linear regression and display to the console.
print('The slope of this line is approximately ' + str(linregress(np.log(Nrange),np.log(timelist))[0]))
#Part B

def myFFT(N): #Define a timing function for np.fft.fft
    starttime = time.time() #Start the timer
    #print(starttime, 'start')
    h = np.random.random(N) #Create the random array
    #print(len(h), 'len')
    
    H = np.fft.fft(h) #Fourier transform it using numpy
    runtime = time.time() - starttime #Record the time it took to do this.
    #print(runtime)
    
    return H, runtime

Nrange2 = np.array([10**5,10**6,10**7]) #Initialize a second Nrange array to test fft
timelist2 = np.zeros(len(Nrange2)) #Initialize another runtime storage array for plotting

for i in range(len(Nrange2)): #Loop over all values in Nrange
    timelist2[i] = myFFT(Nrange2[i])[1] #Update the timelist
    
#print(timelist2)

plt.plot(np.log(Nrange2,np.log(timelist2))) #Again, make a log-log plot
plt.show() #And again, find the slope using linear regression
print('The slope of this line is approximately ' + str(linregress(np.log(Nrange2),np.log(timelist2))[0]))
   