# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:18:59 2020

@author: turne
"""
import numpy as np
from matplotlib import pyplot as plt

def f(x): #define our base function with no taylor expansion
    return np.exp(-x)

xrange = np.arange(-1,1,0.02) #initalize an array of xvalues over the desired range

bruh = f(xrange) #create a list of yvalues for the base function
n2 = np.polyfit(xrange,bruh,2) #compute polyfit for degree 2 and store to a variable
n3 = np.polyfit(xrange,bruh,3) #compute polyfit for degree 3 and store to a variable
n4 = np.polyfit(xrange,bruh,4) #compute polyfit for degree 4 and store to a variable

#print(n2)
#print(n3)
#print(n4)

def f2(x,p): #define the 2nd degree polynomial function for graphing
    return p[2] + p[1]*x + p[0]*x**2

def f3(x,p): #define the 3rd degree polynomial function for graphing
    return p[3] + p[2]*x + p[1]*x**2 + p[0]*x**3

def f4(x,p): #define the 4th degree polynomail function for graphing
    return p[4] + p[3]*x + p[2]*x**2 + p[1]*x**3 + p[0]*x**4

plt.figure(0) #create a plot for the base function and approximations
plt.plot(xrange,f(xrange)) #plot the base function
plt.plot(xrange,f2(xrange,n2)) #plot the 2nd degree polynomial
plt.plot(xrange,f3(xrange,n3)) #plot the 3rd degree polynomial
plt.plot(xrange,f4(xrange,n4)) #plot the 4th degree polynomial
plt.legend(('e^-x','Deg 2','Deg 3','Deg 4')) #add a legend for readability
plt.title('e^-x Plotted against polynomial fits of degree n') #add a title

plt.figure(1) #create a second plot for the differences
plt.plot(xrange,(f2(xrange,n2)-f(xrange))) #take the difference between the 2nd order fit and the base function
plt.plot(xrange,(f3(xrange,n3)-f(xrange))) #take the difference between the 3rd order fit and the base function
plt.plot(xrange,(f4(xrange,n4)-f(xrange))) #take the difference between the 4th order fit and the base function
plt.legend(('Deg 2','Deg 3','Deg 4')) #add a legend
plt.title('Plot of difference between degree fits and original data') #add a title