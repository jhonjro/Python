
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021-09-17 23:46:05


@author  : Jhon Jairo Rojas Ortiz (jhon.rojas.o@uni.pe)
@version : {1:1.0.0}
"""

import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(h, w, maxit=20):
    y, x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime == maxit)
        divtime[div_now] = i
        z[diverge] = 2

    return divtime


plt.figure(figsize=(8, 8))
mandelbrot = mandelbrot(2000, 2000, 100)
plt.imshow(mandelbrot)
plt.show()
