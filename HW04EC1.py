# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:35:41 2020

@author: turne
"""

#import cmath as c
import numpy as np
from matplotlib import pyplot as plt
import datetime

rootdic = {}

def f1(x,y):
    return 2*x**3 - 6*x*y**2
rootdic[f1] = []

def f2(x,y):
    return 6*x**2*y - 2*y**3

xvec = np.array([0,1])

def F(x_vec):
    retvec = np.array([(2*x_vec[0]**3 -6*x_vec[0]*x_vec[1]**2 - 1 ),(6*x_vec[0]**2*x_vec[1] -2*x_vec[1]**3 +3)])
    return(retvec)

#print(F(xvec))

def Jinv(x_vec):
    x = x_vec[0]
    y = x_vec[1]
    if x == 0 and y == 0:
        #print("There is no determinant!")
        return("There is no determinant!")
    det = 1/((6*x**2 - 6*y**2)**2+(12*x*y)**2)
    retvec = np.array([[6*x**2 - 6*y**2,12*x*y],[-12*x*y,6*x**2 - 6*y**2]])
    return(det*retvec)

#print(Jinv(xvec))
#print(type(Jinv(xvec)[0][0]))

def rf_newton2d(F_system,Jinv_system,x_vec0,tol,maxiter):
    i = 0
    xn = x_vec0
    xn1 = np.zeros(2)
    t = 20
    while i < maxiter and t >= tol:
        bruh = F_system(xn)
        boi = Jinv_system(xn)
        #print(xn, 'is xn')
        
        dx = -1*np.array([boi[0][0]*bruh[0]+boi[0][1]*bruh[1], boi[1][0]*bruh[0]+boi[1][1]*bruh[1]])
        #print(dx, 'is dx')
        xn1[0] = xn[0] + dx[0]
        xn1[1] = xn[1] + dx[1]
        #print(xn1, 'is xn + dx')
        t = (float(dx[0])**2 + float(dx[1])**2)**0.5
        xn = xn1
        i+=1
    
    #uni = [[1.06546973,-0.47115078],[-0.94076341,-0.68714847],[-0.12470632,1.15829925]]
    
    return xn
       
#y = rf_newton2d(F,Jinv,xvec,10**-10,30) 
#print(rf_newton2d(F,Jinv,xvec,10*10**-5,20))


uni = [[1.06546973,-0.47115078],[-0.94076341,-0.68714847],[-0.12470632,1.15829925]]

xnum = 250
ynum = 250
x = np.linspace(-1.5,1.5,xnum)
y = np.linspace(-1.5,1.5,ynum)

        
def fractal(F_system,Jinv_system,tol,maxiter):
    #zs = []
    print('I started at' + str(datetime.datetime.now()))
    ztemp = np.zeros((len(x),len(y)))
    #print(xc,yc)
    #for e1 in (x):
        #for e2 in (y):
            #zs.append((e1 + 1j*e2))
    for i in range(len(x)):
        for j in range(len(y)):
            xvec = [x[i],y[j]]
            root = rf_newton2d(F_system,Jinv_system,xvec,10**-5,50)
            angle = np.arctan(root[1]/root[0])
            ztemp[i][j] = angle
            
    plt.imshow(ztemp,cmap='YlOrRd')
    plt.xticks([])
    plt.yticks([])
    plt.ylabel('Im', fontsize=16)
    plt.xlabel('Re',fontsize = 16)
    
    
    #print(ztemp[0])
    
    
    #p = plt.plot(cord)
    print('I finished at' + str(datetime.datetime.now()))
    return 

fractal(F,Jinv,10**-5,uni)

