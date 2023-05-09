import numpy as np
from matplotlib.pylab import plt
import matplotlib.animation as animation
fig = plt.figure()
ax1 = fig.add_subplot(312, xlim=(0, 7), ylim=(-4, 4))
t = 0.0
L = 7.0
k = np.pi
w = 0.07
A = 2.0
x = np.linspace(0, L, 1001)


def abc(t):
    y = 2*A*np.sin(x*k)*np.cos(w*t)
    line1 = ax1.plot(x, y)
    return line1


ani = animation.FuncAnimation(fig, abc, blit=True, frames=1000, interval=1, repeat=True)
plt.show()
