import numpy as np

import matplotlib.pyplot as plt

from numpy import sin, cos

import matplotlib.animation as animation


steps = 100
r = 3.5
T = 5.0
k = 0.1
lim = 6

u = np.linspace(0, np.pi, steps)
v = np.linspace(0, 2*np.pi, steps)
u, v = np.meshgrid(u, v)
x = r*np.sin(u)*np.cos(v)
y = 1.5*r*np.sin(u)*np.sin(v)
z = 0.5*r*np.cos(u)
x = x.ravel()
y = y.ravel()
z = z.ravel()

m = np.linspace(-lim, lim, 10)
n = np.linspace(-lim, lim, 10)
p = np.linspace(0, 2*lim, 10)
m, n, p = np.meshgrid(m, n, p)
d = np.sin(np.pi * m) * np.cos(np.pi * n) * np.cos(np.pi * p)
e = -np.cos(np.pi * m) * np.sin(np.pi * n) * np.cos(np.pi * p)
f = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * m)
     * np.cos(np.pi * n) * np.sin(np.pi * p))

# print(u.shape)
# print(v.shape)
# print(x.shape)
# print(y.shape)
# print(z.shape)

fig = plt.figure()
#ax = Axes3D(fig)
ax = fig.add_subplot(111, projection='3d')
ax.view_init(30, 30)

line = ax.plot3D([], [], [])
line = ax.quiver(m, n, p, d, e, f)
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_zlim(0, 2*lim)


def update(t):
    global x
    global y
    global z
    w1 = 5.0*sin(2*np.pi*t*k/T)
    w2 = 5.0*cos(2*np.pi*t*k/T)
    w3 = 0.5*k*t
#    w1=5*sin(1.5*t)*cos(1.8*t)
#    w2=5*sin(1.5*t)*sin(1.8*t)
#    w3=5*cos(1.5*t)

    x1 = x+w1
    y1 = y+w2
    z1 = z+w3
    line = ax.plot3D(x1, y1, z1, 'g')
#    Axes.set_xlim(line, auto=True)
#    Axes.set_ylim(line, auto=True)
#    Axes.set_zlim(line, auto=True)
    #autoscale(line, tight=True)
    # ax.set_autoscale_on(True)
    return line


ani = animation.FuncAnimation(fig, update, interval=10, blit=True)
# ani.save(filename='plot3d_fluid.mp4',fps=30,dpi=300)

plt.show()
