# -*- coding: utf-8 -*-
"""
Created on Wed Dic 12 10:55:14 2020

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

n = 100 #Número de puntos para la gráfica
tg = np.linspace(t_min, t[-1], n)

y = np.zeros(len(t))
y[0] = y_i

#Defino la función 

def yd(t, y):
    return 0.1*np.cos(5*t) - 0.2*y

def ys(t):
    return -0.000798722*np.exp(-0.2*t) + 0.0199681*np.sin(5*t) + 0.000798722*np.cos(5*t)

#Cálculo númerico por el método de Euler

for i in range(len(t)-1):
    k1 = yd(t[i], y[i])
    k2 = yd(t[i] + 0.25*dT , y[i] + 0.25*k1*dT)
    k3 = yd(t[i] + 0.25*dT, y[i] +1/8*k1*dT + 1/8*k2*dT)
    k4 = yd(t[i] + 0.5*dT, y[i] - 0.5*k2*dT + k3*dT)
    k5 = yd(t[i] + 0.75*dT, y[i] + 3/16*k1*dT + 9/16*k4*dT)
    k6 = yd(t[i] + dT, y[i] -3/7*k1*dT + 2/7*k2*dT + 12/7*k3*dT - 12/7*k4*dT + 8/7*k5*dT)
    y[i+1] = y[i] + 1/90*(7*k1 + 32*k3 + 12*k4 + 32*k5 + 7*k6)*dT
    
    
#Construyo una tabla con los datos obtenido

tabla=pd.DataFrame(list(zip( t, y)), columns=['t','y aprox'])
print(tabla)

#Almaceno la tabla en un archivo csv

# tabla.to_csv('tabla4.csv', sep=';')

#Gráfica de la función 'y' e su aproximación

plt.figure()
plt.plot(t, y ,'g.',markersize=12, linestyle='dashed', label='approx')
plt.plot(tg, ys(tg), 'r', label='real')
ax=plt.gca()
ax.set_title('Aproximación númerica por método RK5')
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.axes.grid(True)
ax.legend()
plt.show()


 