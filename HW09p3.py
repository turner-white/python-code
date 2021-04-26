# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:40:25 2020

@author: turne
"""
import numpy as np
from matplotlib import pyplot as plt

def RK4integrate(F,x,y,xStop,h): #Copy in the code from the textbook
    def run_kut4(F,x,y,h):
            K0 = h*F(x,y)
            K1 = h*F(x + h/2.0, y + K0/2.0)
            K2 = h*F(x + h/2.0, y + K1/2.0)
            K3 = h*F(x + h, y + K2)
            return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        h = min(h,xStop - x)
        y = y + run_kut4(F,x,y,h)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X),np.array(Y)


def Fcoupled(x,y): #Define Fcoupled where y is a vector of y1 and y2
    y1 = y[0] #Extract y1
    y2 = y[1] #Extract y2
    dy1 = y2 #Solve for dy1
    dy2 = x-(2*x+3)*y2-6*x*y1 #Solve for dy2
    return np.array([dy1,dy2]) #Return a vector of dy1 and dy2

hlist = [1,0.1,0.01,0.001]

xin = 0 #Define starting x value
yin = [1,1] #Define y input for starting values to Fcoupled

x1,y1 = RK4integrate(Fcoupled,xin,yin,4,1) #Compute RK4 for h of 1
x2,y2 = RK4integrate(Fcoupled,xin,yin,4,0.1) #Compute RK4 for h of 0.1
x3,y3 = RK4integrate(Fcoupled,xin,yin,4,0.01) #Compute RK4 for h of 0.01
x4,y4 = RK4integrate(Fcoupled,xin,yin,4,0.001) #Compute RK4 for h of 0.001

plt.plot(x1,y1) #Make nice plots with titles and things
plt.title('y1 & y2 vs x for h = 1')
plt.ylim(-10,40) #Limit y to observe the fact that RK4 is trying its best to approximate even when h is crap
plt.legend(('y1','y2'))
plt.grid(True)
plt.show()
plt.plot(x2,y2)
plt.title('y1 & y2 vs x for h = 0.1')
plt.legend(('y1','y2'))
plt.grid(True)
plt.show()
plt.plot(x3,y3)
plt.title('y1 & y2 vs x for h = 0.01')
plt.legend(('y1','y2'))
plt.grid(True)
plt.show()
plt.plot(x4,y4)
plt.title('y1 & y2 vs x for h = 0.001')
plt.legend(('y1','y2'))
plt.grid(True)
plt.show()


    


    