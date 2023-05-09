# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 16:10:45 2020

@author: jhon_
"""

import tkinter as tk
from timeit import timeit

import matplotlib.pyplot as plt
import numpy as np
# import openpyxl
import pandas as pd
from scipy import integrate

# Ingresar por teclado el orden de la ED
o = int(input('Ingrese el orden de la ED: '))

# Pido por teclado las funciones
print('Puedes usar las funciones de numpy como np')
f1 = input('Ingrese la función primera derivada en función de t, x[0], x[1]: ')
f2 = input('Ingrese la función segunda derivada en función de t, x[0], x[1]: ')

# Pido por teclado el intervalo en el cual se ejecutará el método RK5
t_min = eval(input('Ingrese la cota inferior de intervalo a aplicar RK5: '))
t_max = eval(input('Ingrese la cota inferior de intervalo a aplicar RK5: '))
dT = eval(input('Ingrese el paso para aplicar RK5: '))

# Arrays para el tiempo en pasos dT
N = int((t_max - t_min) / dT + 1)
t = np.linspace(t_min, t_max, N)

# Arrays para la gráfica y resolver la ED
n = 100 * (N - 1)  # 10000

tg = np.linspace(t_min, t[-1], n + 1)

# Array para almacenar los datos obtenidos por RK5
x = np.zeros((len(t), 2))
C = 10000


# Defino la función x' y x'' que fue ingresado por teclado
def yd1(t, x):
    return eval(f1)


def yd2(t, x):
    return eval(f2)

# Solución númerica usando Scipy


def f(x, t):
    return np.array([yd1(t, x), yd2(t, x)])


# Condiciones iniciales de la ED
y00 = eval(input('Ingrese el valor de x(0) '))
y01 = eval(input('Ingrese ingrese el valor de x\'(0) '))
y0 = np.array([y00, y01])
sol = integrate.odeint(f, y0, tg)
x[0, :] = y0
# Cálculo númerico por el método de Euler
for i in range(len(t) - 1):
    k1 = np.array([yd1(t[i], x[i, :]), yd2(t[i], x[i, :])])
    k2 = np.array([yd1(t[i] + 0.25 * dT, x[i, :] + k1 * 0.25 * dT),
                   yd2(t[i] + 0.25 * dT, x[i, :] + k1 * 0.25 * dT)])
    k3 = np.array([yd1(t[i] + 0.25 * dT, x[i, :] + 1 / 8 * k1 * dT + 1 / 8 * k2 * dT),
                   yd2(t[i] + 0.25 * dT, x[i, :] + 1 / 8 * k1 * dT + 1 / 8 * k2 * dT)])
    k4 = np.array([yd1(t[i] + 0.5 * dT, x[i, :] - 0.5 * k2 * dT + k3 * dT),
                   yd2(t[i] + 0.5 * dT, x[i, :] - 0.5 * k2 * dT + k3 * dT)])
    k5 = np.array([yd1(t[i] + 0.75 * dT, x[i, :] + 3 / 16 * k1 * dT + 9 / 16 * k4 * dT),
                   yd2(t[i] + 0.75 * dT, x[i, :] + 3 / 16 * k1 * dT + 9 / 16 * k4 * dT)])
    k6 = np.array([yd1(t[i] + dT, x[i, :] - 3 / 7 * k1 * dT + 2 / 7 * k2 * dT + 12 / 7 * k3 * dT - 12 / 7 * k4 * dT + 8 / 7 * k5 * dT),
                   yd2(t[i] + dT, x[i, :] - 3 / 7 * k1 * dT + 2 / 7 * k2 * dT + 12 / 7 * k3 * dT - 12 / 7 * k4 * dT + 8 / 7 * k5 * dT)])
    x[i + 1, :] = x[i, :] + 1 / 90 * \
        (7 * k1 + 32 * k3 + 12 * k4 + 32 * k5 + 7 * k6) * dT

# Creo tabla apartir de los datos obtenidos por RK5
tabla1 = pd.DataFrame(list(zip(
    t, x[:, 0], sol[::100, 0], sol[::100, 0] - x[:, 0])), columns=['t', 'x0', 'x0s', 'e0'])
print(tabla1)

tabla2 = pd.DataFrame(list(zip(
    t, x[:, 1], sol[::100, 1], sol[::100, 1] - x[:, 1])), columns=['t', 'x1', 'x1s', 'e1'])
print(tabla2)

# Almaceno las tablas obtenidas en un archivo .xlsx
writer = pd.ExcelWriter('Datos_RK5.xlsx', engine='openpyxl')
tabla1.to_excel(writer, sheet_name='sol x0', index=False)
tabla2.to_excel(writer, sheet_name='sol x1', index=False)
writer.save()

# Creo funciones para llamarlas en un ambiente tkinter


def graph1():
    plt.figure(1)
    plt.plot(t, x[:, 0], '+', markersize=12,
             linestyle='dashed', label='approx')
    plt.plot(tg, sol[:, 0], label='real')
    ax = plt.gca()
    ax.set_title(
        'Aproximación númerica de carga eléctrica (x0) por método RK5')
    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')
    ax.axes.grid(True)
    ax.legend()
    plt.show()


def graph2():
    plt.figure(2)
    plt.plot(t, x[:, 1], '+', markersize=12,
             linestyle='dashed', label='approx')
    plt.plot(tg, sol[:, 1], label='real')
    ax = plt.gca()
    ax.set_title(
        'Aproximación númerica de intensidad de corriente (x1) por método RK5')
    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')
    ax.axes.grid(True)
    ax.legend()
    plt.show()


def graph3():
    plt.figure(3)
    plt.plot(x[:, 0], x[:, 1], label=r'$x\[1\] vs x\[0\]$')
    ax = plt.gca()
    ax.set_title(r'$x\[1\] vs x\[0\]$')
    ax.set_xlabel('$X$')
    ax.set_ylabel('$Y$')
    # mng.window.showMaximized()
    # plt.show()
    ax.axes.grid(True)
    ax.legend()
    plt.show()


# Creo ventana tkinter
root = tk.Tk()
root.title('Hola mundo! esta es mi solución de la ED con RK5')
# root.Iconbitmap('dirección')
root.geometry('370x150')

# Creo los botones del ambiente tkinter que llamarás a las funciones que gráficarán
tk.my_buttom = tk.Button(
    root, text='¡Graph it: solución de x!', command=graph1)
tk.my_buttom.pack()

tk.my_buttom = tk.Button(
    root, text='¡Graph it: solución de x\'!', command=graph2)
tk.my_buttom.pack()

tk.my_buttom = tk.Button(
    root, text='¡Graph it: los dos juntos!', command=graph3)
tk.my_buttom.pack()

# Llama a la ventana creada
root.mainloop()

print(timeit("'Hello, world!'.replace('Hello', 'Goodbye')"))
