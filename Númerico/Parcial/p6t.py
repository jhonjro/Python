# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 01:11:03 2020

@author: jhon_
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:30:42 2020

@author: jhon_
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Solución de la ecuación diferencial.
def fs(x):
    return 1/2*x + 0.3/np.sqrt(2)*np.sin(np.sqrt(2)*x)


# Defino función derivada 0, 1, 2 , 3 y 4
def f0(x, y):
    return y[1]


def f1(x, y):
    return x - 2*y[0]


# Método de RK4 propio
def f(x, y):
    return h*np.array([f0(x, y), f1(x, y)])


x_0 = 0
x_f = 4
y_0 = np.array([0, 0.5])
h_0 = 0.2
# n_max = 2000
# e_min = 1/np.power(10, 12)
ed = 1/np.power(10, 5)
# h_min = 0.001
# h_max = 0.5

sx = np.array([])
sy = np.array([])
y = y_0
h = h_0
x = x_0
k = 0
while x < x_f:
    sx = np.append(sx, x)
    sy = np.concatenate((sy, y), axis=0)
    # if h < h_min:
    #     h = h_min
    # if h > h_max:
    #     h = h_max
    ys = y
    k1 = f(x, y)
    k2 = f(x + 1/2*h, y + 1/2*k1)
    k3 = f(x + 1/2*h, y + 1/4*k1 + 1/4*k2)
    k4 = f(x + h, y - k2 + 2*k3)
    y_k4 = y + 1/6*k1 + 4/6*k3 + 1/6*k4
    y_k5 = y + 1/6*k1 + 4/6*k3 + 1/6*k4
    e = np.abs(y[0] - ys[0])
    if ed >= e:
        h = h*np.abs(ed/e)**0.2  # rechazar paso
    else:
        h = h*np.abs(ed/e)**0.25
    x = x + h

sy = sy.reshape(len(sx), 2)
print(sy)

tabla = pd.DataFrame(list(zip(sx, sy[:, 0])), columns=['x', 'y'])
print(tabla)

tabla.to_excel("p6.xlsx", sheet_name="Taylor")

N = 1000
xg = np.linspace(0, 4, N)

plt.figure()
plt.grid()
plt.plot(sx, sy[:, 0], '.', markersize=12, linestyle='dashed', label='approx')
plt.plot(xg, fs(xg), label='real')
plt.title('Aproximación númerica por método de RK adaptativo propio')
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.grid(True)
plt.legend()
plt.savefig('p6.png')
plt.show()
