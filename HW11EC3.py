# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:15:42 2020

@author: turne
"""

import numpy as np

A = np.array([[1,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,0],[0,0,0,0,1,1,1,1],[0,0,0,0,1,2,4,8],
              [0,1,0,3,0,-1,-2,-3],[0,0,0,3,0,0,-1,-3],[0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,3]])

b = np.array([2,3,5,6,0,0,0,0])

Ainv = np.linalg.inv(A)

x = Ainv @ b

print(x)