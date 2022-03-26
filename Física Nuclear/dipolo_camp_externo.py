# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:44:01 2020

@author: jhon_
"""

import numpy as np
import matplotlib.pyplot as plt


x_inicial= 0
x_max= 8
dx= 0.1
x= np.arange(x_inicial, x_max+dx, dx)
k1 = 0.15
k0 = 8
I=5

def r(x,k):
    valor= k*x + k0
    return valor

plt.figure()
for i in range(-I,I+1):
    plt.plot(x, r(x,i*k1/I))
ax=plt.gca()
ax.set_xlim(0,9)
ax.set_ylim(6.7,9.3)
# ax.set_title('Energía de dipolo magnético en un campo externo')
ax.set_xlabel('Intensidad de campo magnético $B$ ')
ax.set_ylabel('Energía')
plt.text(8.05, 6.75, r'$ +5$')
plt.text(8.05, 9.15, r'$ -5$')
ax.set_yticklabels([])
ax.set_xticklabels([])
#plt.axis()
ax.legend()
plt.show()