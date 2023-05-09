# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 22:26:31 2021

@author: jhon_
"""

import os
from timeit import timeit
import numpy as np
# import numpy.polynomial as P
import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.metrics import r2_score
from scipy.optimize import curve_fit

# from scipy import stats


t = timeit("'Hello, world!'.replace('Hello', 'Goodbye')")

ejemplo_dir = 'C:/Users/jhon_/Mi unidad/Scripts/Python/dynamic_light_scattering'
contenido = os.listdir(ejemplo_dir)

j = 0
N = 100
T = 0.99


def func(x, A, B, C):
    """Modelo para nuestros datos."""
    return A * np.exp(-B * x) + C


for fichero in contenido:
    if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.xlsx'):
        # Cargamos los datos
        print(fichero)
        data = pd.read_excel(
            (os.path.join(ejemplo_dir, fichero)), header=None, engine='openpyxl')

        for column in data.columns:
            bool = data[column].isnull().values.all()
            if bool:
                data.drop(column, axis=1, inplace=True)

        x = data.iloc[:, 0]
        y = data.iloc[:, 1] * -1
        # data = data.dropna()
        # print(data)
        # data = data.to_numpy()
        # x = data[:, 4]
        # y = data[:, 5]

        # Gráfica de datos
        plt.figure(j)
        plt.grid()
        plt.plot(x, y, label='Datos')

        plt.title('Datos\n' + os.path.splitext(fichero)[0])

        plt.xlabel("$x$")
        plt.ylabel("$y$")
        plt.legend()

        plt.savefig('Procesado/Datos' + os.path.splitext(fichero)[0] + '.png')

        plt.show()

        # Autocorrelation
        autocorrelation = np.correlate(x, y, mode="full")
        autocorrelation = autocorrelation[autocorrelation.size // 2:]

        # Guardado en tablas del R^2 vs grado del polinomio
        tabla = pd.DataFrame(list(zip(x, autocorrelation)),
                             columns=['x', 'autocorrelation'])

        tabla.to_excel('Procesado/Autocorrelation ' + os.path.splitext(fichero)
                       [0] + '.xlsx', sheet_name='Autocorrelation', index=False)

        # Ajuste de correlation a exponencial para determinal tamaño de nanopartículas

        (A, B, C), _ = curve_fit(func, x, autocorrelation)
        # print(A, B)

        # Gráfica de autocorrelation y su ajuste polinómico ideal

        plt.figure(j + 1)
        plt.grid()

        plt.plot(x, autocorrelation, label='x vs autocorrelation')

        plt.plot(x, func(x, A, B, C), label='Ajuste')

        plt.title('Autocorrelation\n' + os.path.splitext(fichero)[0])

        plt.xlabel("$x$")
        plt.ylabel("$y$")
        plt.legend()

        plt.savefig('Procesado/Autocorrelation ' +
                    os.path.splitext(fichero)[0] + '.png')

        plt.show()

        j += 2

        file = open('Procesado/Autocorrelation ' +
                    os.path.splitext(fichero)[0] + '.txt', "w")
        file.write("A :" + os.linesep)
        file.write("{}".format(A) + os.linesep)
        file.write("B :" + os.linesep)
        file.write("{}".format(B) + os.linesep)
        file.write("C :" + os.linesep)
        file.write("{}".format(C))
        file.close()


file = open("Procesado/time.txt", "w")
file.write("Tiempo de ejecución" + os.linesep)
# file.write("{} second".format(t))
file.write(f"{t} second")
file.close()
