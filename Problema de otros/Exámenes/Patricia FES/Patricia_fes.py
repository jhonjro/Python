"""
Created on 2021-09-24 18:00:03


@author  : Patricia Milagros Meza Enciso
@version : {1:1.0.0}
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('seaborn')

fig = plt.figure()
ax = Axes3D(fig)

a = 5

U_0 = 100

x = np.linspace(0, a, 100)
y = np.linspace(0, a, 100)

X, Y = np.meshgrid(x, y)


def U(x, y):
    return 2 * U_0 / (5 * np.pi) * np.sin(2 * np.pi / 5) * np.cos(2 * np.pi * (x + y) / a) + U_0 / np.power(np.pi, 2) * np.power(np.sin(2 * np.pi / 5), 2) * np.cos(2 * np.pi * (x + y) / a) + 2 * U_0 / (5 * np.pi) * np.sin(4 * np.pi / 5) * np.cos(2 * np.pi * x / a) + U_0 / np.power(np.pi, 2) * np.power(np.sin(2 * np.pi / 5), 2) * np.cos(2 * np.pi / 5) * np.cos(2 * np.pi * (x + y) / a)


ax.plot_surface(X, Y, U(X, Y))
ax.set_xlabel('$X (Armstrong)$')
ax.set_ylabel('$Y (Armstrong)$')
ax.set_zlabel(r'$U (Voltios)$', rotation=0)
plt.show()
plt.savefig('patricia_fes.png')
