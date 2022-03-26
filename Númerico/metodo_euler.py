# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:06:34 2020

@author: jhon_
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Editable

dT = 0.09 #paso para cáculo númerico
t_min = 0
t_max = 1
y_i = 0 # y(t[0])

t = np.array([])
i = t_min

while i <= t_max:
    t = np.append(t, i)
    i += dT

n = 100 #número de punto de la gráfica
tg = np.linspace(t_min, t[-1], n)

y = np.zeros(len(t))
y[0] = y_i

#Defino la función derivada de y' que está en función de x & y

def yd(t,y):
    return t*np.exp(2*t)-2*y #editar aquí lol

#Solución de la ecuación diferencial

def ys(t):
    return 1/8*np.exp(-2*t) + 1/4*t*np.exp(2*t) - 1/8*np.exp(2*t) #editar aquí

#Cálculo númerico por el método de Euler

er_abs = np.zeros(len(t))
er_rel = np.zeros(len(t))
ysa = np.zeros(len(t))
ysa[0] = ys(t[0])

for i in range(len(y)-1):
    y[i+1] = y[i] + yd(t[i], y[i] )*dT
    ysa[i+1] = ys(t[i+1])
    er_abs[i+1] = ysa[i+1] - y[i+1]
    er_rel[i+1] = er_abs[i+1]/ys(t[i+1])*100

#Construyo una tabla con los datos obtenido


tabla=pd.DataFrame(list(zip( t, y, ys(t), er_abs, er_rel)), columns=['t','y(t) aprox', 'y(t) real', 'error abs', 'error rel'])
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
