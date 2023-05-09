# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 22:12:58 2020

@author: jhon_
"""
import numpy as np
import matplotlib.pyplot as plt

m_p = 938.272
m_n = 939.565
m_e = 0.511
dx = 0.01
x = np.arange(m_e, m_n - m_p + dx, dx)


def l_e(x):
    valor = x * ((m_n - m_p) - x)**2 * np.sqrt((x**2 - m_e**2))  # (x**2 - m_e**2)**(1/2)
    return valor


plt.figure()
plt.plot(x, l_e(x), '.')
ax = plt.gca()
ax.set_title('Distribución de energía')
ax.set_xlabel('Energía del electrón emitido')
ax.set_ylabel('Probabilidad')
plt.axis()
plt.grid()
ax.legend('Graphic')
plt.show()
