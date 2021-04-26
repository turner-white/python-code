# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:33:51 2020

@author: turne
"""
#hey aleks, Sorry i didnt comment my code here, it got to be a bit too late and I ran out of the time that I
#needed to comment it. I really hope that you can follow from the brief comments I put on the side of each 
#line. 
#import cmath as c
import numpy as np
#from matplotlib import pyplot as plt
#define our starting functions, split between the real and imaginary component
def f1(x,y):
    return 2*x**3 - 6*x*y**2

def f2(x,y):
    return 6*x**2*y - 2*y**3
#initialize a test starting value
xvec = np.array([0,1])
#combine both f1 and f2 into a single function
def F(x_vec):
    retvec = np.array([(2*x_vec[0]**3 -6*x_vec[0]*x_vec[1]**2 - 1 ),(6*x_vec[0]**2*x_vec[1] -2*x_vec[1]**3 +3)])
    return(retvec)

#print(F(xvec))
#compute the inverse jacobian of the vector. The inverse jacobian is hardcoded but work is shown in pdf
def Jinv(x_vec):
    x = x_vec[0]
    y = x_vec[1]
    if x == 0 and y == 0: #condition to catch values which don't converge
        #print("There is no determinant!")
        return("There is no determinant!")
    det = 1/((6*x**2 - 6*y**2)**2+(12*x*y)**2)
    retvec = np.array([[6*x**2 - 6*y**2,12*x*y],[-12*x*y,6*x**2 - 6*y**2]])
    return(det*retvec)

#print(Jinv(xvec))
#print(type(Jinv(xvec)[0][0]))
#compute newton raphson
def rf_newton2d(F_system,Jinv_system,x_vec0,tol,maxiter):
    i = 0
    xn = x_vec0
    xn1 = np.zeros(2) #initialization
    t = 20
    while i < maxiter and t >= tol: #while loop to compute newton raphson with custom coded matrix multiplication
        bruh = F_system(xn)
        boi = Jinv_system(xn)
        #print(xn, 'is xn')
        
        dx = -1*np.array([boi[0][0]*bruh[0]+boi[0][1]*bruh[1], boi[1][0]*bruh[0]+boi[1][1]*bruh[1]])
        #print(dx, 'is dx')
        xn1[0] = xn[0] + dx[0]
        xn1[1] = xn[1] + dx[1]
        #print(xn1, 'is xn + dx')
        t = (float(dx[0])**2 + float(dx[1])**2)**0.5 #dx is the change, and so the squared distanve is error
        xn = xn1
        i+=1
        
    #print(i)
    if i == maxiter:
        print('WARNING: Max Iterations have been reached')
    return(xn)
       
#y = rf_newton2d(F,Jinv,xvec,10**-10,30) 
#print(rf_newton2d(F,Jinv,xvec,10*10**-5,20))

veclist = [np.array([1,0]),np.array([-1,0]),np.array([0,1]),np.array([0,-1]),np.array([-1,-1])
           ,np.array([1,1]),np.array([1,-1]),np.array([-1,1]),np.array([0,0])]
#for loop to try every starting value
for e in veclist:
    try:
        print(rf_newton2d(F,Jinv,e,10**-5,20), 'Is the root for starting values ' + str(e[0])+ ', ' + str(e[1]))
    except:
        print(str(e[0]) + ', '+str(e[1]) + (" These starting values don't converge!"))
