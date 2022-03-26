# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 17:15:05 2020

@author: jhon_
"""

import pandas as pd
import numpy as np
from timeit import timeit
import matplotlib.pyplot as plt

x_min = 0
x_max = 5
dT = 0.1
n = int((x_max - x_min)/dT)
h = 0.1
e_m = 10**(-15)
xp = np.linspace(x_min, x_max, 1001)
x = np.linspace(x_min, x_max, n+1)
hp = np.power(10, np.linspace(-15,1))
print(hp)
# Función seno
def f(x):
    return np.sin(x)
#Primera derivada
def Prim_derivada_f(x,h):
    return (f(x+h)-f(x-h))/(2*h)
#Segunda derivada
def Seg_derivada_f(x,h):
    return (f(x+h)-(2*f(x))+f(x-h))/h**2
#Error total númerico 1
def Etn1(x, h):
    return e_m/(2*h) - np.cos(x)*h**2/6


#Error total númerico 2
def Etn2(x, h):
    return 2*e_m/(h**2) + np.sin(x)*h**2/12


#Error absoluto
def Ea1(x, h):
    return np.cos(x) - Prim_derivada_f(x,h)


def Ea2(x, h):
    return -np.sin(x) - Seg_derivada_f(x,h)


y1a = Prim_derivada_f(x,h)
y1r = np.cos(x)
#Construyo una taabla con los datos obtenido


tabla=pd.DataFrame(list(zip(x, y1a, y1r, y1r-y1a, Etn1(x, h))), columns=['x','f1(x) aprox', 'f1(x) real', 'error absol', 'error tot num'])
#Almaceno la tabla en un archivo csv


tabla.to_csv('tabla1.csv', sep=';')
print(tabla)
print()

y2a = Seg_derivada_f(x,h)
y2r = -f(x)

#Construyo una tabla con los datos obtenido

tabla = pd.DataFrame(list(zip(x, y1a, y1r, y1r - y1a, Etn2(x, h))), columns = ['x','f2(x) aprox', 'f2(x) real', 'error absol', 'error tot num'])
print(tabla)

#Almaceno la tabla en un archivo csv

# tabla.to_csv('tabla2.csv', sep=';')

#Gráfica del valor de la primera derivada y su aproximación

plt.figure()
plt.plot(x, y1a,'xg', label='approx')
plt.plot(xp, np.cos(xp), 'r', label='real')
ax=plt.gca()
ax.set_title('Aproximación númerica de la primera derivada')
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
plt.axis()
ax.legend()
plt.show()

# #Gráfica del valor de la primera derivada y su aproximación

plt.figure()
plt.plot(x, y2a,'xg', label='approx')
plt.plot(xp, -np.sin(xp), 'r', label='real')
ax=plt.gca()
ax.set_title('Aproximación númerica de la segunda derivada')
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
plt.axis()
ax.legend()
plt.show()

# #Gráfica de error absoluto y error total númerico 1 en función de h
x = np.pi/6

plt.figure()
plt.plot(hp, Etn1(x, hp), 'gx', label='error total')
plt.plot(hp, Ea1(x, hp), 'r.', label='error absoluto')
# plt.yscale('log')
plt.xscale('log')
ax=plt.gca()
ax.set_title('Error absoluto y total númerico 1 en función de h')
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
# plt.axis()
ax.legend()
plt.show()

# #Gráfica de error absoluto y error total númerico 2 en función de h
plt.figure()
plt.plot(hp, Etn2(x, hp), 'gx', label='error total')
plt.plot(hp, Ea2(x, hp), 'r.', label='error absoluto')
# plt.yscale('log')
plt.xscale('log')
ax=plt.gca()
ax.set_title('Error absoluto y total númerico 2 en función de h')
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
# plt.axis()
ax.legend()
plt.show()

print(timeit("'Hello, world!'.replace('Hello', 'Goodbye')"))
