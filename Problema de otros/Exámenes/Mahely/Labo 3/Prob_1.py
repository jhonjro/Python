# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 08:55:15 2021

@author: Mahely Torres Moya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

t = np.linspace(1, 2, 11)
y = np.zeros(11)
h = 0.1


def f(t, y):
    return t*np.exp(t) - 40*y


def fs(t):
    return np.exp(-40*t)/1681*(np.exp(41*t)*(41*t-1) - 40*np.exp(41) + 16810*np.exp(40))


y[0] = 10

# Método de Heun
print('Método de Heun')
for i in range(10):
    y[i+1] = y[i] + h*f(t[i], y[i])
    y[i+1] = y[i] + h/2*(f(t[i], y[i]) + f(t[i+1], y[i+1]))

tabla = pd.DataFrame(list(zip(t, y, fs(t))), columns=['t', 'num', 'real'])
print(tabla)
print()

tg = np.linspace(1, 2, 1001)

plt.figure()
plt.title('Método de Euler mejorado o Heun')
plt.plot(t, y, label='Sol. númerica')
plt.plot(tg, fs(tg), label='Sol. analítica')
plt.legend()
plt.grid()
plt.show()

# Método RK3
print('Método RK3')
for i in range(10):
    k1 = f(t[i], y[i])
    k2 = f(t[i] + 1/2*h, y[i] + 1/2*h*k1)
    k3 = f(t[i] + h, y[i] - h*k1 + 2*h*k2)
    y[i+1] = y[i] + h/6*(k1 + 4*k2 + k3)

tabla = pd.DataFrame(list(zip(t, y, fs(t))), columns=['t', 'num', 'real'])
print(tabla)

tg = np.linspace(1, 2, 1001)

plt.figure()
plt.title('Método Runge-Kutta orden 3')
plt.plot(t, y, label='Sol. númerica')
plt.plot(tg, fs(tg), label='Sol. analítica')
plt.legend()
plt.grid()
plt.show()

# Solución analítica

plt.figure()
plt.title('Solución analítica')
plt.plot(tg, fs(tg), label='Sol. analítica')
plt.legend()
plt.grid()
plt.show()
