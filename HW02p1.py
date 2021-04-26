# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:48:05 2020

@author: turne
"""
import numpy as np
from matplotlib import pyplot as plt

def rf_bisect(f,xlo,xhi,xtol,nmax):
#Computes the value of the root for function f bracketed in the domain [xlo, xhi]. 
# PARAMETERS:
#   f     --  (function) The one-dimensional function to evaluate a root of.
#   xlo   --  (float) The lower limit of the bracket.
#   xhi   --  (float) The upper limit of the bracket.
#   xtol  --  (float) The tolerance the calculated root should achieve.
#   nmax  --  (int) The maximum number of iterations allowed.

# RETURNS: (tuple(float, int)) A root of f that meets the tolerance tol the number 
# of iteratons required to converge.
    
#----> Implement your solution for rf_bisect here <-------
    iters = 1
    
    while (iters <= nmax) and (xtol < np.abs(xhi-xlo)): #checks for exceeding max iterations and for tolerance
        root = (xlo+xhi)/2
        flo = f(xlo)
        fhi = f(xhi)
        fmid = f(root)
        #print(xlo,root,xhi)
        
        if flo*fmid < 0: #condition for the case in which the sign change takes place in the lower half
            xhi = root
            #print ('the sign change is below midpoint')
            
        if fhi*fmid < 0: #condition for the case in which the sign change takes place in the upper half
            xlo = root
            #print('the sign change is above midpoint')
            
        elif fmid == 0: #condition for the case in which the sign change does not occur, allows the code to
                        #not reach the maximum number of iterations.
            #print('zero has been found')
            break
            
        iters += 1
        #print(root,iters)
        
    return (root, iters)

#Plot each of the four functions being passed to rf_bisect over the interval of interest. Since you
#are looking for roots where f(x) = 0, you may also wish to plot a horizontal line at y=0 to aid in
#visualizing them. 

# Functions f1, f2, f3, and f4 that may be used to test your implementation of rf_bisect.
def f1(x):
    return 3 * x + 2*np.sin(x) - np.exp(x)

def f2(x):
    return x**3 - 0.125

def f3(x):
    return np.sin(1. / (x + 0.01))

def f4(x):
    return 1. / (x - 0.5)

# Example: Find the root of f2(x) and print the result.

xrange = np.arange(-1,1,0.001)

plt.figure(0)
plt.plot(xrange, f1(xrange))
plt.plot(xrange,np.zeros(len(xrange)))
plt.grid(True)
plt.title('f1 over -1 to 1')
plt.show()
    
plt.figure(1)
plt.plot(xrange, f2(xrange))
plt.plot(xrange,np.zeros(len(xrange)))
plt.grid(True)
plt.title('f2 over -1 to 1')
plt.show()

plt.figure(2)
plt.plot(xrange, f3(xrange))
plt.plot(xrange,np.zeros(len(xrange)))
plt.grid(True)
plt.title('f3 over -1 to 1')
plt.show()
    
plt.figure(3)
plt.plot(xrange, f4(xrange))
plt.plot(xrange,np.zeros(len(xrange)))
plt.grid(True)
plt.ylim(-10,10)
plt.title('f4 over -1 to 1')
plt.show()

tolist = [10**-3,10**-6,10**-12]
for i in range(len(tolist)):
    (root1,iters1) = rf_bisect(f1, -1., 1., tolist[i], 50)
    print('Tolerance of ' + str(tolist[i]))
    print('Root of f1: ' + str(root1))
    print('# iterations: ' + str(iters1))
    fval1=f1(root1)
    print('f1 evaluated at root is: ' + str(fval1))
    print('----------------------------')
    
for i in range(len(tolist)):
    (root2,iters2) = rf_bisect(f2, -1., 1., tolist[i], 50)
    print('Tolerance of ' + str(tolist[i]))
    print('Root of f2: ' + str(root2))
    print('# iterations: ' + str(iters2))
    fval2=f2(root2)
    print('f2 evaluated at root is: ' + str(fval2))
    print('----------------------------')
    
for i in range(len(tolist)):
    (root3,iters3) = rf_bisect(f3, -1., 1., tolist[i], 50)
    print('Tolerance of ' + str(tolist[i]))
    print('Root of f3: ' + str(root3))
    print('# iterations: ' + str(iters3))
    fval3=f3(root3)
    print('f3 evaluated at root is: ' + str(fval3))
    print('----------------------------')

for i in range(len(tolist)):
    (root4,iters4) = rf_bisect(f4, -.75, 1., tolist[i], 50)
    print('Tolerance of ' + str(tolist[i]))
    print('Root of f4: ' + str(root4))
    print('# iterations: ' + str(iters4))
    fval4=f4(root4)
    print('f4 evaluated at root is: ' + str(fval4))
    print('----------------------------')
