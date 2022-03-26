# -*- coding: utf-8 -*-
"""
Created on Wed Dic 12 10:55:14 2020

@author: jhon_
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dT = 0.05 #paso para cáculo númerico
y_i = 0 # y(t[0])
x_i = 0
N = 10


y = np.zeros(2*N+1)
x = np.zeros(2*N+1)
t = np.arange(2*N+1)
y[0] = y_i
x[0] = x_i

#Defino la función

def yd1(v):
    return v

def yd2(v):
    return 10 - 0.25/70*v**2

#Cálculo númerico por el método RK5

for i in range(N):
    k1 = yd1(y[i])
    k12 = yd2(y[i])
    k2 = yd1(y[i] + 0.25*k1*dT)
    k22 = yd2(y[i] + 0.25*k12*dT)
    k3 = yd1(y[i] +1/8*k1*dT + 1/8*k2*dT)
    k32 = yd2(y[i] +1/8*k12*dT + 1/8*k22*dT)
    k4 = yd1(y[i] - 0.5*k2*dT + k3*dT)
    k42 = yd2(y[i] - 0.5*k22*dT + k32*dT)
    k5 = yd1(y[i] + 3/16*k1*dT + 9/16*k4*dT)
    k52 = yd2(y[i] + 3/16*k12*dT + 9/16*k42*dT)
    k6 = yd1(y[i] -3/7*k1*dT + 2/7*k2*dT + 12/7*k3*dT - 12/7*k4*dT + 8/7*k5*dT)
    k62 = yd2(y[i] -3/7*k12*dT + 2/7*k22*dT + 12/7*k32*dT - 12/7*k42*dT + 8/7*k52*dT)
    x[i+1] = x[i] + 1/90*(7*k1 + 32*k3 + 12*k4 + 32*k5 + 7*k6)*dT
    y[i+1] = y[i] + 1/90*(7*k12 + 32*k32 + 12*k42 + 32*k52 + 7*k62)*dT


L = x[10]

def yd2(x, v):
    return 10 - 0.25/70*v**2 - 55*(x-L) - 0.25/70*v

for i in range(N, 2*N):
    k1 = yd1(y[i])
    k12 = yd2(x[i], y[i])
    k2 = yd1(y[i] + 0.25*k1*dT)
    k22 = yd2(x[i] + 0.25*k12*dT, y[i] + 0.25*k12*dT)
    k3 = yd1(y[i] +1/8*k1*dT + 1/8*k2*dT)
    k32 = yd2(x[i] +1/8*k12*dT + 1/8*k22*dT, y[i] +1/8*k12*dT + 1/8*k22*dT)
    k4 = yd1(y[i] - 0.5*k2*dT + k3*dT)
    k42 = yd2(x[i] - 0.5*k22*dT + k32*dT, y[i] - 0.5*k22*dT + k32*dT)
    k5 = yd1(y[i] + 3/16*k1*dT + 9/16*k4*dT)
    k52 = yd2(x[i] + 3/16*k12*dT + 9/16*k42*dT, y[i] + 3/16*k12*dT + 9/16*k42*dT)
    k6 = yd1(y[i] -3/7*k1*dT + 2/7*k2*dT + 12/7*k3*dT - 12/7*k4*dT + 8/7*k5*dT)
    k62 = yd2(x[i] -3/7*k12*dT + 2/7*k22*dT + 12/7*k32*dT - 12/7*k42*dT + 8/7*k52*dT, y[i] -3/7*k12*dT + 2/7*k22*dT + 12/7*k32*dT - 12/7*k42*dT + 8/7*k52*dT)
    x[i+1] = x[i] + 1/90*(7*k1 + 32*k3 + 12*k4 + 32*k5 + 7*k6)*dT
    y[i+1] = y[i] + 1/90*(7*k12 + 32*k32 + 12*k42 + 32*k52 + 7*k62)*dT

#Construyo una tabla con los datos obtenido

tabla=pd.DataFrame(list(zip(x, y)), columns=['x aprox', 'v approx'])
print(tabla)

#Almaceno la tabla en un archivo csv

# tabla.to_csv('tabla1RK5.csv', sep=';')

#Gráfica de la función 'y' e su aproximación

plt.figure()
plt.plot(t, x ,'g.',markersize=12, linestyle='dashed', label='x vs t')
plt.plot(t, y ,'r.',markersize=12, linestyle='dashed', label='y vs t')
ax=plt.gca()
ax.set_title('Aproximación númerica por método RK5')
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.axes.grid(True)
ax.legend()
plt.show()

plt.figure()
plt.plot(x, y ,'b.',markersize=12, linestyle='dashed', label='y vs x')
ax=plt.gca()
ax.set_title('Aproximación númerica por método RK5')
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.axes.grid(True)
ax.legend()
plt.show()

