# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 12:36:43 2020

@author: mahely_
"""

import numpy as np
x_0 = 1
x_f = 3
h = 0.125


def f(x):
    return x**4 #np.pi*np.power(1+x**3, 2/3)


def met_simp(x_0, x_f, h):
    x = np.arange(x_0, x_f + h, h)
    S=0
    for i in range(1,len(x)-1):
        if i%2 == 0:
            S += 2*f(x[i])
        else:
            S+= 4*f(x[i])
            
    S += f(x[0]) + f(x[-1])
    S*= h/3
    return S

print(met_simp(x_0, x_f, h))
    
def met_alt(x_0, x_f, h):
    def met_extr(x_0, x_f, h):
        x = np.arange(x_0, x_f + h, h)
        M=0
        for i in range(1,len(x)-1):
            if i%2 == 1:
                M += 2*f(x[i])
        M *= h
        return M
    
    def met_trap(x_0, x_f, h):
        x = np.arange(x_0, x_f + h, h)
        T=0
        for i in range(1,len(x)-1):
            T += f(x[i])
        T += (f(x[0]) + f(x[-1]))/2
        T *= h
        return T
    R = 1/3*met_extr(x_0, x_f, h) + 2/3*met_trap(x_0, x_f, h)
    return R

print(met_alt(x_0, x_f, h))




