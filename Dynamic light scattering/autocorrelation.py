# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 17:24:50 2020

@author: jhon_
"""
import os
from timeit import timeit
import numpy as np
import numpy.polynomial as P
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
# from scipy import stats


t = timeit("'Hello, world!'.replace('Hello', 'Goodbye')")

ejemplo_dir = 'C:/Users/jhon_/Mi unidad/Scripts/Python/dynamic_light_scattering'
contenido = os.listdir(ejemplo_dir)

j = 0
N = 100
T = 0.99


for fichero in contenido:
    if os.path.isfile(os.path.join(ejemplo_dir, fichero)) and fichero.endswith('.xlsx'):
        # Cargamos los datos
        data = pd.read_excel(
            fichero, header=None, engine='openpyxl')
        data.head()
        data = data.to_numpy()
        x = data[:, 4]
        y = data[:, 5]

        # * Gráfica de datos

        plt.figure(j)
        plt.grid()
        plt.plot(x, y, label='Datos')

        plt.title('Datos\n' + os.path.splitext(fichero)[0])

        plt.xlabel("$x$")
        plt.ylabel("$y$")
        plt.legend()

        plt.savefig('Procesado/Datos ' + os.path.splitext(fichero)[0] + '.png')

        plt.show()

        # * Autocorrelation

        autocorrelation = np.correlate(x, y, mode="full")
        autocorrelation = autocorrelation[autocorrelation.size//2:]

        # * Guardado en tablas del R^2 vs grado del polinomio

        tabla = pd.DataFrame(list(zip(x, autocorrelation)),
                             columns=['x', 'autocorrelation'])
        # print(tabla)
        tabla.to_excel('Procesado/Autocorrelation ' + os.path.splitext(fichero)
                       [0] + '.xlsx', sheet_name='Autocorrelation', index=False)

        # * Elección del mejor ajuste polinomico

        y_aj = np.zeros(N)
        r2 = np.array([])

        # Ajuste polinómico

        for i in range(N):
            mymodel = P.polynomial.polyfit(x, y, deg=i)
            y_aj = P.polynomial.polyval(x, mymodel)
            r2 = np.append(r2, r2_score(y, y_aj))
            r2[i] = r2_score(y, y_aj)
            if r2[i] > T:
                break

        # Indice del mayor elemento de un array de una dimensión

        def indice_mayor_elemento(lista):
            mayor = lista[0]
            indice = 0
            for i in range(len(lista)):
                if lista[i] > mayor:
                    mayor = lista[i]
                    indice = i
            return indice

        # Ajuste con el ajuste 'ideal'

        i = indice_mayor_elemento(r2)
        mymodel = P.polynomial.polyfit(x, autocorrelation, deg=i)
        x_dom = np.linspace(x[0], x[-1], num=10001)
        y_aj = P.polynomial.polyval(x_dom, mymodel)

        # Gráfica de autocorrelation y su ajuste polinómico ideal

        plt.figure(j+1)
        plt.grid()

        plt.plot(x, autocorrelation, label='x vs autocorrelation')

        plt.plot(x_dom, y_aj, 'm',
                 label='Ajuste polinomial de grado {} de x vs autocorrelation'.format(i))

        plt.title('Autocorrelation\n' + os.path.splitext(fichero)[0])

        plt.xlabel("$x$")
        plt.ylabel("$y$")
        plt.legend()

        plt.savefig('Procesado/Autocorrelation ' +
                    os.path.splitext(fichero)[0] + '.png')

        plt.show()

        j += 2


file = open("Procesado/time.txt", "w")
file.write("Tiempo de ejecución" + os.linesep)
file.write("{} second".format(t))
file.close()
