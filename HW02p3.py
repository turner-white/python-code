# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:50:35 2020

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
    
    while (iters <= nmax) and (np.abs(xhi-xlo) >= xtol): #checks for exceeding max iterations and for tolerance
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

def fb(x): 
    #Here I define the function given in the textbook by subtracting every term on the right side over and setting
    #it equal to 0. Now we can use bisection to find the root. I hardcoded every number supplied by the textbook
    #because the commented out alternative function with 6 inputs did not cooperate with my rf_bisection function.
    #return (((Q**2)/(2*g*b**2))*((1/h0**2)-(1/x**2))+h0-x-H)
    return (((1.2**2)/(2*9.81*1.8**2))*((1/(0.6**2))-(1/(x**2)))+0.6-x-0.075)

#print(fb(1.2,9.81,1.8,0.6,0.075,1))
#print(fb(1))
#The rest of the code here is just a straightforward display of the answers and plots requested.
xrange = np.arange(0.01,0.6,0.001)
plt.plot(xrange,fb(xrange))
plt.ylim(-1,1)
plt.grid(True)

print(rf_bisect(fb,0.15,0.3,0.0001,30), ' Is the first root found with 12 iterations')
print(rf_bisect(fb,0.4,0.65,0.0001,30), ' Is the second root found with 14 iterations')
print()
print('The solutions are 0.265 and 0.496')