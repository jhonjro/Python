# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:24:22 2020

@author: jhon_
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

h = 0.2
x_min = 0
x_max = 4

N = int((x_max-x_min)/h + 1)
x = np.linspace(x_min, x_max, N)

y = np.zeros((len(x), 2))
y[0, :] = np.array([0, 0.8])


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


# Método RK4 propio
for i in range(20):
    k1 = f(x[i], y[i, :])
    k2 = f(x[i] + 1/2*h, y[i, :] + 1/2*k1)
    k3 = f(x[i] + 1/2*h, y[i, :] + 1/4*k1 + 1/4*k2)
    k4 = f(x[i] + h, y[i, :] - k2 + 2*k3)
    y[i+1, :] = y[i, :] + 1/6*k1 + 4/3*k3 + 1/6*k4

# Crear tabla con toda la información, imprimir y guardado en archivo .xlsx
tabla = pd.DataFrame(list(zip(x, y[:, 0], fs(x)-y[:, 0])), columns=['x', 'y', 'error'])
print(tabla)

tabla.to_excel("p4.xlsx", sheet_name="Taylor")

# Gráfica del valor de la primera dderivada y su aproximación
# para gráficar
N = 1000
xg = np.linspace(x_min, x_max, N)

plt.figure()
plt.grid()
plt.plot(x, y[:, 0], '.', markersize=12, linestyle='dashed', label='approx')
plt.plot(xg, fs(xg), label='real')
plt.title('Aproximación númerica por método de RK4 propio')
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.grid(True)
plt.legend()
plt.savefig('p4.png')
plt.show()
