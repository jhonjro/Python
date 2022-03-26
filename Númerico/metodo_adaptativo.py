# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 15:18:01 2020

@author: jhon_
"""

import numpy as np
import matplotlib.pyplot as plt


def f(x, t):
    return t


t_0 = 0
t_f = 4
x_0 = 4
h_0 = 0.5
n_max = 200
e_min = 1/np.power(10, 10)
e_max = 1/np.power(10, 6)
h_min = 0.01
h_max = 0.5

st = np.array([])
s = np.array([])
x_k4 = x_0
x_k5 = x_0
# x = x_0
h = h_0
t = t_0
k = 0
while k < n_max and t < t_f:
    st = np.append(st, t)
    s = np.append(s, x_k5)
    if h < h_min:
        h = h_min
    if h > h_max:
        h = h_max
    for i in range(1):
        hx = h
        tx = t + hx*i
        k1 = hx*f(tx, x_k4)
        k2 = hx*f(tx + 1/5*hx, x_k4 + 1/5*k1)
        k3 = hx*f(tx + 3/10*hx, x_k4 + 3/40*k1 + 9/40*k2)
        k4 = hx*f(tx + 3/5*hx, x_k4 + 3/10*k1 - 9/10*k2 + 6/5*k3)
        k5 = hx*f(tx + hx, x_k4 - 11/54*k1 + 5/2*k2 - 70/27*k3 + 35/27*k4)
        x_k4 = x_k4 + 37/378*k1 + 250/621*k3 + 125/594*k4 + 512/1771*k5
    k1 = h*f(t, x_k5)
    k2 = h*f(t + 1/5*h, x_k5 + 1/5*k1)
    k3 = h*f(t + 3/10*h, x_k5 + 3/40*k1 + 9/40*k2)
    k4 = h*f(t + 3/5*h, x_k5 + 3/10*k1 - 9/10*k2 + 6/5*k3)
    k5 = h*f(t + h, x_k5 - 11/54*k1 + 5/2*k2 - 70/27*k3 + 35/27*k4)
    k6 = h*f(t + 7/8*h, x_k5 + 1631/55296*k1 + 175/512*k2 + 575/13824*k3 + 44275/110592*k4 + 253/4096*k5)
    x_k5 = x_k5 + 2825/27648*k1 + 18578/43384*k3 + 13525/55296*k4 + 277/14336*k5 + 1/4*k6
    e = np.abs(x_k4 - x_k5)
    if e > e_max and h > h_min:
        h = h/2  # rechazar paso
    else:
        # aceptar paso
        k = k + 1
        t = t + h
        if e < e_min:
            h = 2*h

plt.figure()
plt.plot(st, s, '.')
plt.grid()
plt.show()
