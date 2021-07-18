# -*- coding: utf-8 -*-
"""

@author: Jakub
"""
import matplotlib.pyplot as plt
import numpy as np

######
"""zad. 1"""
######

phi = np.cos(np.pi/2) + 1j * np.sin(np.pi/2)
N = 23000

z_1 = np.empty(N, np.complex)
z_1[0] = 0

for n in range(1,N):
    if np.random.rand(1) < 0.5:
        z_1[n] = (1+1j)*z_1[n-1]/2
    else:
        z_1[n] = (1 - (1-1j)*z_1[n-1])/2
        
x_1 = z_1.real
y_1 = z_1.imag

z_2 = z_1 * phi
x_2 = z_2.real
y_2 = z_2.imag

z_3 = z_1 * phi ** 2
x_3 = z_3.real
y_3 = z_3.imag

z_4 = z_1 * phi ** 3
x_4 = z_4.real
y_4 = z_4.imag

plt.plot(x_1,y_1, '.', markersize=0.2, color="#FF6633")
plt.plot(x_2,y_2, '.', markersize=0.2, color="pink")
plt.plot(x_3,y_3, '.', markersize=0.2, color="green")
plt.plot(x_4,y_4, '.', markersize=0.2, color="blue")
plt.title("Smok Heighwaya")
plt.xlabel("$Re(z)$")
plt.ylabel("$Im(z)$")
plt.show()

