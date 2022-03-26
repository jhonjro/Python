"""
Created on Thu Dec  3 21:35:29 2020

@author: jhon_
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from timeit import timeit
# import tkinter as tk
# import openpyxl

# Intervalo en el que se ejecutará RK5
t_min = 0
t_max = 0.5
dT = 0.05

# Creación del array t para ejecutar RK5
N = int((t_max-t_min)/dT + 1)
t = np.linspace(t_min, t_max, N)

# Datos para la gráfica de la solución analítica y resolución de la ED
n = 10000
tg = np.linspace(t_min, t[-1], n+1)

# Array para almacenar los datos obtenidos por RK5
x = np.zeros((len(t), 2))


# Defino la función derivada
def yd1(t, x):
    return x[1]


# Defino la función segunda derivada
def yd2(t, x):
    return 1/10*np.cos(5*t) - x[1]/5 - x[0]/(50000)


# Solución númerica usando Scipy
def f(x, t):
    return np.array([x[1], 1/10*np.cos(5*t) - x[1]/5 - x[0]/(50000)])


y0 = np.array([0, 0])
sol = integrate.odeint(f, y0, tg)
x[0, :] = y0

# Cálculo númerico por el método de Euler
for i in range(len(t)-1):
    k1 = np.array([yd1(t[i], x[i, :]), yd2(t[i], x[i, :])])
    k2 = np.array([yd1(t[i] + 0.25*dT, x[i, :] + k1*0.25*dT), yd2(t[i] + 0.25*dT, x[i, :] + k1*0.25*dT)])
    k3 = np.array([yd1(t[i] + 0.25*dT, x[i, :] + 1/8*k1*dT + 1/8*k2*dT), yd2(t[i] + 0.25*dT, x[i, :] + 1/8*k1*dT + 1/8*k2*dT)])
    k4 = np.array([yd1(t[i] + 0.5*dT, x[i, :] - 0.5*k2*dT + k3*dT), yd2(t[i] + 0.5*dT, x[i, :] - 0.5*k2*dT + k3*dT)])
    k5 = np.array([yd1(t[i] + 0.75*dT, x[i, :] + 3/16*k1*dT + 9/16*k4*dT), yd2(t[i] + 0.75*dT, x[i, :] + 3/16*k1*dT + 9/16*k4*dT)])
    k6 = np.array([yd1(t[i] + dT, x[i, :] - 3/7*k1*dT + 2/7*k2*dT + 12/7*k3*dT - 12/7*k4*dT + 8/7*k5*dT),
                  yd2(t[i] + dT, x[i, :] - 3/7*k1*dT + 2/7*k2*dT + 12/7*k3*dT - 12/7*k4*dT + 8/7*k5*dT)])
    x[i+1, :] = x[i, :] + 1/90*(7*k1 + 32*k3 + 12*k4 + 32*k5 + 7*k6)*dT

# Creo tabla apartir de los datos obtenidos por RK5
tabla1 = pd.DataFrame(list(zip(t, x[:, 0], sol[::int(n/10), 0], sol[::int(n/10), 0] - x[:, 0])), columns=['t', 'x0', 'x0s', 'e0'])
print(tabla1)

tabla2 = pd.DataFrame(list(zip(t, x[:, 1], sol[::int(n/10), 1], sol[::int(n/10), 1] - x[:, 1])), columns=['t', 'x1', 'x1s', 'e1'])
print(tabla2)

# Almaceno las tablas obtenidas en un archivo .xlsx
writer = pd.ExcelWriter('Datos RK5.xlsx', engine='openpyxl')

tabla1.to_excel(writer, sheet_name='sol x0', index=False)
tabla2.to_excel(writer, sheet_name='sol x1', index=False)

writer.save()


# Gráfica de la solucion de x con RK5 vs solución analítica
plt.figure(1)
plt.plot(t, x[:, 0], '.', markersize=12, linestyle='dashed', label='approx')
plt.plot(tg, sol[:, 0], label='real')
ax = plt.gca()
ax.set_title('Aproximación númerica de carga eléctrica (x0) por método RK5')
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.axes.grid(True)
ax.legend()
plt.show()


# Gráfica de la solucion de x' con RK5 vs solución analítica
plt.figure(2)
plt.plot(t, x[:, 1], '.', markersize=12, linestyle='dashed', label='approx')
plt.plot(tg, sol[:, 1], label='real')
ax = plt.gca()
ax.set_title('Aproximación númerica de intensidad de corriente (x1) por método RK5')
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.axes.grid(True)
ax.legend()
plt.show()

# Gráfica de la solucion de x y x'' con RK5 vs solución analítica
plt.figure(3)
plt.plot(t, x[:, 0], '.', markersize=12, linestyle='dashed', label='approx')
plt.plot(tg, sol[:, 0], label='real')
plt.plot(t, x[:, 1], '.', markersize=12, linestyle='dashed', label='approx')
plt.plot(tg, sol[:, 1], label='real')
ax = plt.gca()
ax.set_title('Aproximación númerica de intensidad de corriente (x1) por método RK5')
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.axes.grid(True)
ax.legend()
plt.show()

plt.figure(4)
plt.plot(t, sol[::int(n/10), 0] - x[:, 0], '.', markersize=12, linestyle='dashed', label='approx')
ax = plt.gca()
ax.set_title('Error absoluto por método RK5 vs. t')
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.axes.grid(True)
ax.legend()
plt.show()


print(timeit("'Hello, world!'.replace('Hello', 'Goodbye')"))
