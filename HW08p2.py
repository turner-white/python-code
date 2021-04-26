# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 22:12:22 2020

@author: turne
"""
import numpy as np
from matplotlib import pyplot as plt

filename = 'HW08bridge.csv' #Create a filename for the bridge data.
data = np.loadtxt(filename, delimiter = ',') #Read in the data using loadtxt.

Fx = np.fft.fft(data) #Create a Fourier transformed data set using numpy
AFx = np.abs(Fx) #Take the absolute value of Fx
N = len(data) #Find the number of points in the data array
#plt.plot(Fx)
#plt.show()
dt = 20*(10**-3) #Calculate the delta t
Nf = 1/(2*dt) #Calculate the nyquist
df = 1/(dt*N) #Calulate delta f

frange = np.arange(0,(len(data)*df),df) #Initialize an array of frequencies for plotting

#Everything below is just general plotting things, no need to comment.

#print(times[-1])
plt.figure(0)
plt.plot(frange,AFx)
plt.title('Plot of fft of Bridge Data up to Nyquist Frequency.')
plt.xlim(0,Nf)
plt.xlabel('f (Hz)')
plt.ylabel('Amplitude')
plt.show()
print('We can see that there are 3 main peaks around 1, 3, and 18. Zooming in allows us get closer.')

plt.figure(1)
plt.plot(frange,AFx)
plt.xlim(18.5,19.5)
plt.xlabel('f (Hz)')
plt.ylabel('Amplitude')
plt.title('Zoomed DFT vs f from 18.5 to 19.5')
plt.show()
print('Focusing on the rightmost peak, we find a peak in DFT at approximately 19 Hz. ')

plt.figure(2)
plt.plot(frange,AFx)
plt.xlim(3,4)
plt.title('Zoomed DFT vs f from 3 to 4')
plt.xlabel('f (Hz)')
plt.ylabel('Amplitude')
plt.show()
print('Focusing on the middle peak, we find a peak in DFT at approximately 3.5 Hz.')

plt.figure(3)
plt.plot(frange,AFx)
plt.xlim(0.1,1)
plt.title('Zoomed DFT vs f from 0.1 to 1')
plt.xlabel('f (Hz)')
plt.ylabel('Amplitude')
plt.show()
print('Looking over our target range, we '
      + 'find a peak in DFT at approximately 0.85 Hz. This is a problem for the engineers.')