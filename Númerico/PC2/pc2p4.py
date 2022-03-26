# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:55:14 2020

@author: jhon_
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import special
import math as m
#Editable

t_min = 0
t_max = 1
N  = float(input('Ingrese el número de puntos: ')) + 1
print()
# dT = 0.1 #paso para cáculo númerico
dT = (t_max - t_min)/N
y1_i = 1 # y(t[0])
y2_i = 2
t = np.array([])
i = t_min

while i <= t_max:
    t = np.append(t, i)
    i += dT

n = 100 #Número de puntos para la gráfica
tg = np.linspace(t_min, t[-1], n)

y1 = np.zeros(len(t))
y2 = np.zeros(len(t))
y1[0] = y1_i
y2[0] = y2_i

#Defino la función que da la serie de taylor de orden 4 (5 está comentado) para determinar la función 'y'

def yd1(t, y1, y2, h):
    return y1 + h*y2 + np.power(h,2)/m.factorial(2)*(-y2*t -y1) + np.power(h,3)/m.factorial(3)*(y2*(t**2-2) + y1*t)  + np.power(h,4)/m.factorial(4)*(y2*(5*t - t**3) + y1*(3 - t**2)) #+ np.power(h,5)/m.factorial(5)*(y2*(t**4 - 9*t**2 + 8) + y1*(t**3 - 7*t))


#Defino la función que da la serie de taylor de orden 4 (5 que está comentado) para determinar la primera derivada de 'y'

def yd2(t, y1, y2, h):
    return y2 + h*(-y2*t -y1) + np.power(h,2)/m.factorial(2)*(y2*(t**2-2) + y1*t) + np.power(h,3)/m.factorial(3)*(y2*(5*t - t**3) + y1*(3 - t**2)) + np.power(h,4)/m.factorial(4)*(y2*(t**4 - 9*t**2 + 8) + y1*(t**3 - 7*t)) #+ np.power(h,5)/m.factorial(5)*(y2*(-t**5 + 14*t**3 - 33*t) + y1*(-t**4 + 12*t**2 - 15))

#Solución de la ecuación diferencial

def ys(t):
    return np.exp(-t**2/2)*(np.sqrt(2*np.pi)*special.erfi(t/np.sqrt(2)) +1)

#Cálculo númerico por el método de Euler

er_abs = np.zeros(len(t))
ysa = np.zeros(len(t))
ysa[0] = ys(t[0])

for i in range(len(y1)-1):
    y1[i+1] = yd1(t[i], y1[i], y2[i], dT)
    y2[i+1] = yd2(t[i], y1[i], y2[i], dT)
    ysa[i+1] = ys(t[i+1])
    er_abs[i+1] = ysa[i+1] - y1[i+1]
    
#Construyo una tabla con los datos obtenido

tabla=pd.DataFrame(list(zip( t, y1, y2, ys(t), er_abs)), columns=['t','y1 aprox', 'y2 aprox', 'y(t) real', 'error abs'])
print(tabla)

#Almaceno la tabla en un archivo csv

tabla.to_csv('tabla4.csv', sep=';')

#Gráfica de la función 'y' e su aproximación

plt.figure()
plt.plot(t, y1 ,'g.',markersize=12, linestyle='dashed', label='approx')
plt.plot(tg, ys(tg), 'r', label='real')
ax=plt.gca()
ax.set_title('Aproximación númerica por método de Taylor p4')
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.axes.grid(True)
ax.legend()
plt.show()


 