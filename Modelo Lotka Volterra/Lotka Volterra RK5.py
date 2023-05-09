# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 19:32:29 2020

@author: jhon_

Script para resolver el modelo Lotka Volterra para "Dinámica de poblaciones interactuantes", ingresando parámetros por teclado

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from timeit import timeit
# import tkinter as tk
# import openpyxl

# Pido por teclado las funciones
print('Puedes usar las funciones de numpy como np')

# Pido por teclado el intervalo en el cual se ejecutará el método RK5
t_min = 0  # float(input('Ingrese la cota inferior de intervalo a aplicar RK5 '))
t_max = 100  # float(input('Ingrese la cota superior de intervalo a aplicar RK5 '))
dT = 0.1  # float(input('Ingrese el paso para aplicar RK5 '))

# Parémetros del modelo Lotka Volterra
r1 = 0.4  # float(input('Ingrese la tasa de crecimiento de las presas. '))
a1 = 0.3  # float(input('Ingrese el éxito en la caza del depredador, que afecta a la presa. '))
r2 = 0.37  # float(input('Ingrese la tasa de crecimiento de los depredadores. '))
a2 = 0.05  # float(input('Ingrese el éxito en la caza, que afecta al depredador. '))

# Arrays para el tiempo en pasos dT
N = int((t_max-t_min)/dT + 1)
t = np.linspace(t_min, t_max, N)

# Arrays para la gráfica y resolver la ED
n = 100*(N-1)  # 10000
tg = np.linspace(t_min, t[-1], n+1)

# Array para almacenar los datos obtenidos por RK5
x = np.zeros((len(t), 2))


# Defino la función x' y x'' que fue ingresado por teclado
def yd1(t, x):
    return a1*x[0]-r1*x[0]*x[1]


def yd2(t, x):
    return a2*x[0]*x[1]-r2*x[1]


# Solución númerica usando Scipy
def f(x, t):
    return np.array([yd1(t, x), yd2(t, x)])


# Condiciones iniciales de la ED
y00 = 3
y01 = 1
y0 = np.array([y00, y01])
sol = integrate.odeint(f, y0, tg)
x[0, :] = y0
# Cálculo númerico por el método de Euler
for i in range(len(t)-1):
    k1 = np.array([yd1(t[i], x[i, :]), yd2(t[i], x[i, :])])
    k2 = np.array([yd1(t[i] + 0.25*dT, x[i, :] + k1*0.25*dT), yd2(t[i] + 0.25*dT, x[i, :] + k1*0.25*dT)])
    k3 = np.array([yd1(t[i] + 0.25*dT, x[i, :] + 1/8*k1*dT + 1/8*k2*dT), yd2(t[i] + 0.25*dT, x[i, :] + 1/8*k1*dT + 1/8*k2*dT)])
    k4 = np.array([yd1(t[i] + 0.5*dT, x[i, :] - 0.5*k2*dT + k3*dT), yd2(t[i] + 0.5*dT, x[i, :] - 0.5*k2*dT + k3*dT)])
    k5 = np.array([yd1(t[i] + 0.75*dT, x[i, :] + 3/16*k1*dT + 9/16*k4*dT), yd2(t[i] + 0.75*dT, x[i, :] + 3/16*k1*dT + 9/16*k4*dT)])
    k6 = np.array([yd1(t[i] + dT, x[i, :] - 3/7*k1*dT + 2/7*k2*dT + 12/7*k3*dT - 12/7*k4*dT + 8/7*k5*dT), yd2(t[i] + dT, x[i, :] - 3/7*k1*dT + 2/7*k2*dT + 12/7*k3*dT - 12/7*k4*dT + 8/7*k5*dT)])
    x[i+1, :] = x[i, :] + 1/90*(7*k1 + 32*k3 + 12*k4 + 32*k5 + 7*k6)*dT

# Creo tabla apartir de los datos obtenidos por RK5
tabla1 = pd.DataFrame(list(zip(t, x[:, 0], sol[::100, 0], np.abs(sol[::100, 0] - x[:, 0]))), columns=['t', 'x0', 'x0s', 'e0'])
print(tabla1)

tabla2 = pd.DataFrame(list(zip(t, x[:, 1], sol[::100, 1], np.abs(sol[::100, 1] - x[:, 1]))), columns=['t', 'x1', 'x1s', 'e1'])
print(tabla2)

# Almaceno las tablas obtenidas en un archivo .xlsx
writer = pd.ExcelWriter('Datos_RK5.xlsx', engine='openpyxl')

tabla1.to_excel(writer, sheet_name='sol x0', index=False)
tabla2.to_excel(writer, sheet_name='sol x1', index=False)

writer.save()


# Creo funciones para llamarlas en un ambiente tkinter
def graph1():
    plt.figure(1)
    plt.plot(t, x[:, 0], '+', linestyle='dashed', label='approx')
    plt.plot(tg, sol[:, 0], label='real')
    ax1 = plt.gca()
    ax1.set_title('Aproximación númerica de x[0] vs t por método RK5')
    ax1.set_xlabel('$X$')
    ax1.set_ylabel('$Y$')
    ax1.axes.grid(True)
    ax1.legend()
    plt.show()


def graph2():
    plt.figure(2)
    plt.plot(t, x[:, 1], '+', linestyle='dashed', label='approx')
    plt.plot(tg, sol[:, 1], label='real')
    ax2 = plt.gca()
    ax2.set_title('Aproximación númerica de x[1] vs t por método RK5')
    ax2.set_xlabel('$X$')
    ax2.set_ylabel('$Y$')
    ax2.axes.grid(True)
    ax2.legend()
    plt.show()


def graph3():
    plt.figure(3)
    plt.plot(t, x[:, 0], '+', linestyle='dashed', label='approx')
    plt.plot(tg, sol[:, 0], label='real')
    plt.plot(t, x[:, 1], '+', linestyle='dashed', label='approx')
    plt.plot(tg, sol[:, 1], label='real')
    ax3 = plt.gca()
    ax3.set_title('Aproximación númerica númerica de x[0] & x[1] vs t por método RK5')
    ax3.set_xlabel('$X$')
    ax3.set_ylabel('$Y$')
    # mng.window.showMaximized()
    # plt.show()
    ax3.axes.grid(True)
    ax3.legend()
    plt.show()


def graph4():
    plt.figure(4)
    plt.plot(x[:, 0], x[:, 1], label='Datos númericos')
    ax4 = plt.gca()
    ax4.set_title('x[1] vs x[0]')
    ax4.set_xlabel('$X$')
    ax4.set_ylabel('$Y$')
    # mng.window.showMaximized()
    # plt.show()
    ax4.axes.grid(True)
    ax4.legend()
    plt.show()


def graph5():
    plt.figure(5)
    plt.plot(t, np.abs(sol[::100, 0] - x[:, 0]), label='Error absoluto de x[0]')
    ax1 = plt.gca()
    ax1.set_title('Error absoluto de x[0] vs t por método RK5')
    ax1.set_xlabel('$X$')
    ax1.set_ylabel('$Y$')
    ax1.axes.grid(True)
    ax1.legend()
    plt.show()


def graph6():
    plt.figure(6)
    plt.plot(t, np.abs(sol[::100, 1] - x[:, 1]), label='Error absoluto de x[1]')
    ax1 = plt.gca()
    ax1.set_title('Error absoluto de x[1] vs t por método RK5')
    ax1.set_xlabel('$X$')
    ax1.set_ylabel('$Y$')
    ax1.axes.grid(True)
    ax1.legend()
    plt.show()
# # Creo ventana tkinter
# root = tk.Tk()
# root.title('Hola mundo! esta es mi solución de la ED con RK5')
# # root.Iconbitmap('dirección')
# root.geometry('370x150')

# # Creo los botones del ambiente tkinter que llamarás a las funciones que gráficarán
# tk.my_buttom = tk.Button(root, text = '¡Graph it: solución de x[0] vs t!', command = graph1)
# tk.my_buttom.pack()

# tk.my_buttom = tk.Button(root, text = '¡Graph it: solución de x[1] vs t!', command = graph2)
# tk.my_buttom.pack()


# tk.my_buttom = tk.Button(root, text = '¡Graph it: x[0] & x[1] vs t!', command = graph3)
# tk.my_buttom.pack()


# tk.my_buttom = tk.Button(root, text = '¡Graph it: x[0] vs x[1]!', command = graph4)
# tk.my_buttom.pack()

# Llama a la ventana creada
# root.mainloop()

graph1()
graph2()
graph3()
graph4()
graph5()
graph6()

# Devuele el tiempo de ejecución del programa
print(timeit("'Hello, world!'.replace('Hello', 'Goodbye')"))
