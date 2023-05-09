# -*- coding: utf-8 -*-
"""
Created on 2021-09-25 19:08:39


@author  : Jhon Jairo Rojas Ortiz (jhon.rojas.o@uni.pe)
@version : {1:1.0.0}
"""

import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
from scipy import signal
# from celluloid import Camera


def fourier_onda_cuadrada(x, n):
    m = 2*n-1
    f = (4/np.pi)*(1/m)*np.sin(m*np.pi*x/L)
    return f


# fig = plt.figure()
# camera = Camera(fig)


L = np.pi
ciclos = 1
x = np.linspace(-0.001, 2*ciclos*L, 1000)

f = 0
n = 1
n_total = 10

while n < n_total:
    f += fourier_onda_cuadrada(x, n)
    # plt.plot(x, f, label='n= {}'.format(2*n-1))
    plt.plot(x, f, label='n= {}'.format(2*n-1))
    # camera.snap()
    n += 1


plt.plot(x, signal.square(x), color='k')
plt.legend()
plt.show()
# animation = camera.animate()

# animation.save('fourier.gif')
