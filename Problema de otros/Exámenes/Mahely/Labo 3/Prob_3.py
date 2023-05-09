# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:25:24 2021

@author: jhon_
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

N = 6
x = np.linspace(0, 0.9, N + 2)
a = np.zeros(N + 2)
b = np.zeros(N + 2)
c = np.zeros(N + 2)
d = np.zeros(N + 2)
l = np.zeros(N + 2)
u = np.zeros(N + 2)
z = np.zeros(N + 2)
w = np.zeros(N + 2)
x[0] = 0
x[-1] = 0.9
a_ = 0
b_ = 2
h = (0.9-0)/(N + 1)


def p(x):
    return 0


def q(x):
    return 1


def r(x):
    return 1


def fs(t):
    return -0.26322*np.exp(-t) + 1.26322*np.exp(t) - 1


a[1] = 2 + h**2*q(x[1])
b[1] = -1 + h/2*p(x[1])
d[1] = -h**2*r(x[1]) + (1 + h/2*p(x[1]))*a_

for i in range(2, N+1):
    a[i] = 2 + h**2*q(x[i])
    b[i] = -1 + h/2*p(x[i])
    c[i] = -1 - h/2*p(x[i])
    d[i] = -h**2*r(x[i])

a[N+1] = 2 + h**2*q(x[N+1])
c[N+1] = -1 - h/2*p(x[N+1])
d[N+1] = -h**2*r(x[N+1]) + (1 - h/2*p(x[N+1]))*b_

l[1] = a[1]
u[1] = b[1]/l[1]
z[1] = d[1]/l[1]

for i in range(2, N+1):
    l[i] = a[i] - c[i]*u[i-1]
    u[i] = b[i]/l[i]
    z[i] = (d[i] - c[i]*z[i-1])/l[i]

l[N+1] = a[N+1] - c[N+1]*u[N]
z[N+1] = (d[N+1] - c[N+1]*z[N])/l[N+1]

w[0] = a_
w[N+1] = b_
w[N] = z[N]

for i in range(N, 0, -1):
    w[i] = z[i] - u[i]*w[i+1]

tabla = pd.DataFrame(list(zip(x, w, fs(x))), columns=['t', 'num', 'asddas'])
print(tabla)

xg = np.linspace(0, 0.9, 1000)

plt.figure()
plt.title('Método Runge-Kutta orden 4')
plt.plot(x, w, 'xg', label='Sol. númerica')
plt.plot(xg, fs(xg), label='Sol. analítica')
plt.legend()
plt.grid()
plt.show()
