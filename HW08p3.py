# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 19:52:57 2020

@author: turne
"""

from matplotlib import pyplot as plt
import numpy as np

filename = 'C:/Users/turne/Documents/Fall 2020 UNC/Code/GrayImage.jpg'
X = plt.imread(filename)

def PassBoi(I,nmax): #Create a function PassBoi which will make repeated callings easier. I is the image and
                     #nmax specifies the radius of the aperture.
    Hx = np.fft.fft2(I,axes=(0,1)) #Perform a 2D Fourier transform of the image and store in Hx

    Hxshift = np.fft.fftshift(Hx) #Shift Hx so that all passing values are centered in the middle of the array
    lowmask= np.zeros((1100,1100)) #Create a lowmask array of 0s
    highmask = np.zeros((1100,1100)) #Create a highmask array of 0s
    for i in range(len(Hxshift)): #Loop over every kx in Hxshift
        for j in range(len(Hxshift)): #Loop over every ky in Hxshift
            if (i-550)**2 + (j-550)**2 < nmax**2: #If the pixel is within the specified radius, then include it
                lowmask[i][j] = 1                 #in the lowmask.
            else:
                highmask[i][j] = 1 #If the pixel isn't in the lowmask, then we know its in the highmask.
    
    lowmask = np.fft.ifftshift(lowmask) #Un-shift the lowmask so that it hits the right pixels
    highmask = np.fft.ifftshift(highmask) #Un-shift the highmask

    lowbruh = np.fft.ifft2(Hx*lowmask, axes = (0,1)) #Perform the inverse 2D Transformation on only the passed points
    highbruh = np.fft.ifft2(Hx*highmask, axes = (0,1)) #Do the same on the opposite points.
    plt.imshow((np.abs(lowbruh)), cmap = 'Greys_r') #Display the low-pass image
    plt.show()
    print('This is the low-pass image for nmax = ' + str(nmax))
    plt.imshow((np.abs(highbruh)),cmap = 'Greys_r') #Display the high-pass image
    plt.show()
    print('This is the high-pass image for nmax = ' + str(nmax))
    
    return

plt.imshow(X, cmap='Greys_r') #Show the original image for coolness points in the console.
plt.show()
print('----------------This is the original image!----------------')

nlist = [10,30,100,300] #Initialize a list of n values as requested by the homework pdf
#for n in nlist: #For each nmax value, output the corresponding sets of high and low pass images.
 #   PassBoi(X,n)
    
plt.imshow(np.log(np.abs(np.fft.fft2(X,axes=(0,1)))),cmap='Greys_r')
