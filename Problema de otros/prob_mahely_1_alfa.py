# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 21:27:52 2020

@author: jhon_
"""

import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd
x_0 = -1
x_f = 1
# n = 20
# m = 200


def f(x):
    return 1/(1 + 25*x**2)


def h(n, m):
    g = np.linspace(x_0, x_f, n+1)
    xg = np.linspace(x_0, x_f, m)
    yg = np.zeros(len(xg))
    for k in range(len(xg)):
        x = np.linspace(x_0, x_f, n+1)
        z = np.ones(len(x))
        y = np.zeros(len(x))
        for i in range(len(x)):
            y[i] = f(x[i])
        for i in range(len(x)):
            for j in range(len(x)):
                if j != i:
                    z[i] *= (xg[k]-x[j])/(x[i]-x[j])
            yg[k] += (y[i]*z[i])
    plt.plot(g, f(g), '.', markersize = 0.15*n + 10, label = 'polinomio de orden ' + str(n))
    plt.plot(xg, yg, label=n)


g = np.linspace(x_0, x_f, 200)
plt.figure()
plt.plot(g, f(g), markersize = 12, label = 'real')
# h(50, 200)
# h(20, 400)
h(10, 400)
h(5, 400)
ax = plt.gca()
ax.set_title('Gráfica de polinomio interpolante')
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
# ax.set_ylim(-2,1.2)
ax.axes.grid(True)
ax.legend()
# ax.legend(loc = 'lower right')
plt.savefig('Ejemplo1.jpg', bbox_inches='tight')
plt.show()
