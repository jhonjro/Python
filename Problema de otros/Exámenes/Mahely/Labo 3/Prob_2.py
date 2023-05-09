# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 10:25:46 2021

@author: Mahely Torres Moya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

t = np.array([0])
y = np.array([3])
h = 1/6


def f(t, y):
    return -0.6*np.sqrt(y)


def fs(t):
    return np.power(-0.3*t + np.sqrt(3), 2)


print('Método RK3')
while True:
    if y[-1] > 0:
        k1 = f(t[-1], y[-1])
    else:
        break
    if y[-1] + 1/2*h*k1 > 0:
        k2 = f(t[-1] + 1/2*h, y[-1] + 1/2*h*k1)
    else:
        break
    if y[-1] + 1/2*h*k2 > 0:
        k3 = f(t[-1] + 1/2*h, y[-1] + 1/2*h*k2)
    else:
        break
    if y[-1] + h*k3 > 0:
        k4 = f(t[-1] + h, y[-1] + h*k3)
    else:
        break
    y = np.append(y, y[-1] + h/6*(k1 + 2*k2 + 2*k3 + k4))
    t = np.append(t, t[-1] + h)


tabla = pd.DataFrame(list(zip(t, y)), columns=['t', 'num'])
print(tabla)

tg = np.linspace(0, t[-1], 1000)

plt.figure()
plt.title('Método Runge-Kutta orden 4')
plt.plot(t, y, 'xg', label='Sol. númerica')
plt.plot(tg, fs(tg), label='Sol. analítica')
plt.legend()
plt.grid()
plt.show()
