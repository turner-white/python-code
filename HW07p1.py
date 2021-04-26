# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:42:30 2020

@author: turne
"""
import numpy as np
from matplotlib import pyplot as plt

def funcSawtooth(nmax): #define the function with one input as specified by the homework pdf nmax is the max sums
    mesh = 1/(10*nmax)
    xrange = np.arange(-2,2,mesh) #initialilze an array of x values from -2 to 2 with a small mesh size
    def fourier(x,n): #define a secondary function to compute the fourier transform equation when called
        return ((-2)/((np.pi*n)**2))*(np.cos(np.pi*n) - 1)*(np.cos((np.pi*n*x)/2)) #code the equation
    
    def f(x): #define another secondary function to compute the original piecewise sawtooth function
        ytemp = [] #initialize an empty list of y values for appending
        for e in x: #loop over every x value in the range of x specified by the input array
            if e <= 0.: #establish the piecewise component of the equation when x is less than 0
                ytemp.append((1/2)*e + 1) #code the equation
            if e > 0.: #establish the piecewise component of the equation when x is greater than 0
                ytemp.append(-(1/2)*e + 1) #code the equation
        return ytemp # return the list of y values
    
    ylist = [] #initialize a separate ylist for the values of the fourier transform function
    for x in xrange: #loop over every x value in the range of xvalues
        y = 1/2 #set the initial value of y to 1/2 as specified by the equation
        for n in range(1,nmax+1): #loop and sum for every value of n up to nmax as specified by the equation
            y += fourier(x,n) #call the predefined function to compute the fourier transform and increment y
        ylist.append(y) #append the ylist with the completed sum value
    
    plt.plot(xrange,ylist) #plot the fourier transformed function 
    plt.plot(xrange,f(xrange)) #plot the original sawtooth function by calling the predefined function above
    plt.title('Sawtooth Function w/ Fourier Transform Overlay') #add a title
    plt.xlabel('nmax = ' + str(nmax))
    plt.legend(('F(x)','f(x)')) #add a legend for readability
    plt.show() #display the plot and close the function
        
    return 

nlist = [1,2,3,30]
for  i in range(len(nlist)):
    plt.figure(i)
    funcSawtooth(nlist[i])

def ModFuncSawtooth(nmax):
    mesh = 1/(10*nmax)
    xrange = np.arange(-6,6,mesh) #initialie an array of x values from -6 to 6 with a small mesh size
    def fourier(x,n): #define a secondary function to compute the fourier transform equation when called
        return ((-2)/((np.pi*n)**2))*(np.cos(np.pi*n) - 1)*(np.cos((np.pi*n*x)/2)) #code the equation
    
    ylist = [] #initialise a ylist for the values of the fourier transform function
    for x in xrange: #loop over every x value in the range of x values
        y = 1/2 #set the initial value of y to 1/2 as specified by the equation
        for n in range(1,nmax+1): #loop and sum for every value of n up to nmax as specified by the equation
            y += fourier(x,n) #call the predefined function to compute the fourier transform and increment y
        ylist.append(y) #append the ylist with the completed sum value
    
    plt.plot(xrange,ylist) #plot the fourier transformed function
    plt.title('ModSawtooth Function w/ Fourier Transform Overlay') #title the plot
    plt.xlabel('nmax = ' +str(nmax))
    plt.legend(('F(x)')) #add a legend, because why not?
    plt.show() #display the plot and close the function
        
    return 

nlist2 = [1,3,30]
for i in range(len(nlist2)):
    plt.figure(i)
    ModFuncSawtooth(nlist2[i])

