# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 10:40:42 2020

@author: jhon_
"""

import numpy as np
import pandas as pd
import math as m
import matplotlib.pyplot as plt

dT = 0.2
t_min = 1
t_max = 2

N = (t_max-t_min)/dT + 1
t = np.linspace(t_min, t_max, int(N))

N = 100
tg = np.linspace(t_min, t[-1], int(N))

y = np.zeros(len(t))
ysa = np.zeros(len(t))
er1 = np.zeros(len(t))
er2 = np.zeros(len(t))

y_i = 0
y[0] = y_i

#Solución de la ecuación diferencial.

def ys(t):
    return -t/4 + 1/(4*t) + t*np.log(t)/2 #np.sin(t)

#Defino función y', y'', y''', etc que está en función de t & y.

def yd1(t, y):
    return np.log(t) -y/t    #np.cos(t)

def yd2(t, y):
    return 1/t - np.log(t) + 2*y/t**2 #-np.sin(t)

def yd3(t, y):
    return (2*np.log(t) - 1)/t**2 - 1/t - 6*y/t**3 #-np.cos(t)

def yd4(t, y):
    return (4-10*np.log(t))/t**3 + 1/t**2 + 22*y/t**3  #np.sin(t)

#Método de Euler de 4° orden y(t+h).

def ye(t, y, h):
    return y + yd1(t, y)*h + yd2(t, y)*np.power(h, 2)/m.factorial(2) + yd3(t, y)*np.power(h, 3)/m.factorial(3) + yd4(t, y)*np.power(h, 4)/m.factorial(4)

#Aproximación del error por el método de Taylor.

def error(t, y, h):
    return np.power(h,4)*(yd4(t+h, ye(t, y, h)) - yd4(t,y))/m.factorial(5)

#Cálculo todos los datos.

for i in range(len(t)-1):
    y[i+1] = ye(t[i], y[i], dT)
    ysa[i+1] = ys(t[i]+dT)
    er1[i+1] = error(t[i], y[i], dT)
    er2[i+1] = ysa[i+1] - y[i+1]
    
#Crear tabla con toda la información y imprimir.

ysa[0] = ys(t[0])
tabla=pd.DataFrame(list(zip(t, y, ysa, er1, er2)), columns=['t', 'Taylor', 'Sol. analítica', 'error trunc', 'error absol'])
print(tabla)

#Gráfica del valor de la primera dderivada y su aproximación

plt.figure()
plt.plot(t, y ,'g.',markersize=12, linestyle='dashed', label='approx')
plt.plot(tg, ys(tg), 'r', label='real')
ax=plt.gca()
ax.set_title('Aproximación númerica por método de Euler')
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.axes.grid(True)
ax.legend()
plt.show()



