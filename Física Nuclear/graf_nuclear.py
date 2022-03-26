
"""
Created on Fri Aug 14 21:57:12 2020

@author: jhon_
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import constants as c

a_v = 15.753
a_s = 17.804
a_c = 0.7103
a_A = 23.69
m_p = c.m_p  # 938.272
m_n = c.m_n  # 939.565
m_e = c.m_e  # 0.511
alpha = c.alpha  # 1/137

n = 127

# A = pd.read_excel("libro1.xlsx", sheet_name='Hoja1', header=None)
# A = A.to_numpy() + 0.0

A = np.linspace(0, 10, n)
Z = np.arange(n) + 1.0
B = np.zeros(n)
B_p = np.zeros(n)
M = np.zeros(n)


def delta(i):
    if A[i] % 2 == 1:
        return 0
    elif Z[i] % 2 == 0:
        return 33.6*A[i]**(-3/4)
    else:
        return -33.6*A[i]**(-3/4)


for i in range(n):
    B[i] = a_v*A[i] - a_s*A[i]**(2/3) - a_c*Z[i]**2*A[i]**(-1/3) - a_A*(A[i]-2*Z[i])**2*A[i]**(-1) + delta(i)

for i in range(n):
    B_p[i] = (a_v*A[i] - a_s*A[i]**(2/3) - a_c*Z[i]**2*A[i]**(-1/3) - a_A*(A[i]-2*Z[i])**2*A[i]**(-1) + delta(i))/A[i]


for i in range(n):
    M[i] = Z[i]*m_p + (A[i] - Z[i])*m_n - B[i]

# print(A)
plt.figure()
plt.plot(Z, B)
ax = plt.gca()
ax.set_title('Distribución de energía')
ax.set_xlabel('Energía del electrón emitido')
ax.set_ylabel('Probabilidad')
plt.axis()
ax.legend()
plt.show()


plt.figure()
plt.plot(Z, B_p, 'o-', markersize=2, linewidth=0.5)
plt.show()


plt.figure()
plt.plot(Z, M)
plt.show()
