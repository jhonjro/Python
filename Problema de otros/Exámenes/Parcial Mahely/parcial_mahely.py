# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 16:31:02 2020

@author: jhon_
"""

import numpy as np
import math as m
import pandas as pd

a = np.array([1])
b = np.array([2])
r = np.array([])


def f(s):
    return 3*s - m.exp(s)


def ms(s):
    return s + (3*s - np.exp(s))/(3 - s)


# Método de Bisección

i = 0
p = True
while p:
    r = np.append(r, (a[i] + b[i])/2)
    if f(a[i])*f(r[i]) < 0:
        a = np.append(a, a[i])
    else:
        a = np.append(a, r[i])
    if f(b[i])*f(r[i]) < 0:
        b = np.append(b, b[i])
    else:
        b = np.append(b, r[i])
    if (b[i] - a[i])/np.power(2, i) < 0.5/np.power(10, 4):
        p = False
    else:
        p = True
    i += 1

tabla = pd.DataFrame(list(zip(a, b, r)), columns=['a', 'b', 'r'])
print(tabla)
print(r[i-1])

# Método de Newton-Raphson

x = np.array([r[i-1]])
i = 0
p = True

while p:
    x = np.append(x, ms(x[i]))
    if np.abs(x[i+1] - x[i]) < 0.5/np.power(10, 4):
        p = False
    i += 1

print(x)
