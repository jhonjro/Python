# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 10:56:41 2021

@author: jhon_
"""
import numpy as np

import matplotlib.pyplot as plt

steps = 10
R = 3.5
T = 5.0
k = 0.1
lim = 6


m = np.linspace(0, R, steps)
n = np.linspace(0, np.pi, steps)
p = np.linspace(0, 2*np.pi, steps)
m, n, p = np.meshgrid(m, n, p)
d = np.sin(np.pi * m) * np.cos(np.pi * n) * np.cos(np.pi * p)
e = -np.cos(np.pi * m) * np.sin(np.pi * n) * np.cos(np.pi * p)
f = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * m)
     * np.cos(np.pi * n) * np.sin(np.pi * p))


fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
ax.view_init(30, 30)

line = ax.plot3D([], [], [])
line = ax.quiver(m, n, p, d, e, f)
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_zlim(0, 2*lim)


plt.show()
