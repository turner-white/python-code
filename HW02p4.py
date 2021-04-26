# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:50:35 2020

@author: turne
"""
import numpy as np
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
    
    while (iters <= nmax) and (np.abs(xhi-xlo) >= xtol):
        root = (xlo+xhi)/2
        flo = f(xlo)
        fhi = f(xhi)
        fmid = f(root)
        #print(xlo,root,xhi)
        
        if flo*fmid < 0:
            xhi = root
            #print ('the sign change is below midpoint')
            
        if fhi*fmid < 0:
            xlo = root
            #print('the sign change is above midpoint')
            
        elif fmid == 0:
            #print('zero has been found')
            break
            
        iters += 1
        #print(root,iters)
        
    return (root, iters)

def f2(x):
    return (390-(x**3))

print(rf_bisect(f2,7,8,(1.87337*10**-5),30))



