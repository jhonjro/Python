# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:35:29 2020

@author: jhon_
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from scipy import special
# import math as m
#Editable

t_min = 0
t_max = 0.5
dT = 0.05 #paso para cáculo númerico
y_i = 0 # y(t[0])

N = (t_max-t_min)/dT + 1
t = np.linspace(t_min, t_max, int(N))

n = 1000 #Número de puntos para la gráfica
tg = np.linspace(t_min, t[-1], n)

y = np.zeros(len(t)) # representa a la carga
x = np.zeros(len(t)) # representa a la intensidad de corriente
er1 = np.zeros(len(t))
er2 = np.zeros(len(t))
y[0] = y_i 
x[0] = 0
er1[0]=0
er2[0]=0
C = 10000
#Defino la función 

def yd1(y):
    return y

def yd2(t, x, y):
    return 1/10*np.cos(5*t) - y/5 - x/(5*C)

def ys1(t):
    return 0.00423*np.exp(-0.189443*t) + 0.000236067*np.exp(-0.0105573*t) + 0.00015977*np.sin(5*t) - 0.0039393*np.cos(5*t)

def ys2(t):
    return -0.00080134389*np.exp(-0.189443*t) - 0.0000024922301391*np.exp(-0.0105573*t) + 0.00079985*np.cos(5*t) + 0.0196965*np.sin(5*t)

#Cálculo númerico por el método de Euler

for i in range(len(t)-1):
    k1 = yd1(y[i])
    k12 = yd2(t[i], x[i], y[i])
    k2 = yd1(y[i] + 0.25*k1*dT)
    k22 = yd2(t[i] + 0.25*dT, x[i] + 0.25*k1*dT, y[i] + 0.25*k12*dT)
    k3 = yd1(y[i] +1/8*k1*dT + 1/8*k2*dT)
    k32 = yd2(t[i] + 0.25*dT, x[i] +1/8*k12*dT + 1/8*k22*dT, y[i] +1/8*k12*dT + 1/8*k22*dT)
    k4 = yd1(y[i] - 0.5*k2*dT + k3*dT)
    k42 = yd2(t[i] +0.5*dT , x[i] - 0.5*k22*dT + k32*dT, y[i] - 0.5*k22*dT + k32*dT)
    k5 = yd1(y[i] + 3/16*k1*dT + 9/16*k4*dT)
    k52 = yd2(t[i] + 0.75*dT, x[i] + 3/16*k12*dT + 9/16*k42*dT, y[i] + 3/16*k12*dT + 9/16*k42*dT)
    k6 = yd1(y[i] -3/7*k1*dT + 2/7*k2*dT + 12/7*k3*dT - 12/7*k4*dT + 8/7*k5*dT)
    k62 = yd2(t[i] + dT, x[i] -3/7*k12*dT + 2/7*k22*dT + 12/7*k32*dT - 12/7*k42*dT + 8/7*k52*dT, y[i] -3/7*k12*dT + 2/7*k22*dT + 12/7*k32*dT - 12/7*k42*dT + 8/7*k52*dT)
    x[i+1] = x[i] + 1/90*(7*k1 + 32*k3 + 12*k4 + 32*k5 + 7*k6)*dT
    y[i+1] = y[i] + 1/90*(7*k12 + 32*k32 + 12*k42 + 32*k52 + 7*k62)*dT
    er1[i+1] =  (ys1(t[i+1]) - x[i+1])/ys1(t[i+1])*100
    er2[i+1] = (ys2(t[i+1]) - y[i+1])/ys2(t[i+1])*100
    
#Construyo una tabla con los datos obtenido

tabla=pd.DataFrame(list(zip( t, x, er1)), columns=['t','carga aprox', 'error'])
print(tabla)
tabla=pd.DataFrame(list(zip( t, y, er2)), columns=['t','corriente aprox', 'error'])
print(tabla)

#Almaceno la tabla en un archivo csv

# tabla.to_excel('tabla4.xlsx', sheet_name = 'hola', index = False)

#Gráfica de la función 'y' e su aproximación

plt.figure()
plt.plot(t, y ,'g.',markersize=12, linestyle='dashed', label='approx')
plt.plot(tg, ys2(tg), 'r', label='real')
ax=plt.gca()
ax.set_title('Aproximación númerica de carga por método RK5')
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.axes.grid(True)
ax.legend()
plt.show()

plt.figure()
plt.plot(t, x ,'g.',markersize=12, linestyle='dashed', label='approx')
plt.plot(tg, ys1(tg), 'r', label='real')
ax=plt.gca()
ax.set_title('Aproximación númerica de intensidad por método RK5')
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.axes.grid(True)
ax.legend()
plt.show()

from timeit import timeit
print(timeit("'Hello, world!'.replace('Hello', 'Goodbye')"))
 