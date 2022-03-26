# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:55:14 2020

@author: jhon_
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Editable

dT = 0.1 #paso para cáculo númerico
t_min = 0
t_max = 1
y_i = 1 # y(t[0])

t = np.array([])
i = t_min

while i <= t_max:
    t = np.append(t, i)
    i += dT

n = 100 #Número de punto de la gráfica
tg = np.linspace(t_min, t[-1], n)

y = np.zeros(len(t))
y[0] = y_i

#Defino la función derivada de y' que está en función de x & y

def yd(t,y):
    return t*y + t**3

#Solución de la ecuación diferencial

def ys(t):
    return -t**2 + 3*np.exp(t**2/2) - 2

#Cálculo númerico por el método de Euler

er_abs = np.zeros(len(t))
ysa = np.zeros(len(t))
ysa[0] = ys(t[0])

for i in range(len(y)-1):
    y[i+1] = y[i] + yd(t[i], y[i] )*dT
    ysa[i+1] = ys(t[i+1])
    er_abs[i+1] = ysa[i+1] - y[i+1]
    
#Construyo una tabla con los datos obtenido

tabla=pd.DataFrame(list(zip( t, y, ys(t), er_abs)), columns=['t','y(t) aprox', 'y(t) real', 'error abs'])
print(tabla)

#Almaceno la tabla en un archivo csv

tabla.to_csv('tabla2.csv', sep=';')

#Gráfica de la función 'y' y su aproximación

plt.figure()
plt.plot(t, y ,'g.',markersize=12, linestyle='dashed', label='approx')
plt.plot(tg, ys(tg), 'r', label='real')
ax=plt.gca()
ax.set_title('Aproximación númerica por método de Euler p2')
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.axes.grid(True)
ax.legend()
plt.show()