# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:45:00 2020

@author: jhon_
"""

import math
import scipy.constants as c
# import scipy.constants.physical_constants as phy

m_p = c.m_p  # 938.272
m_n = c.m_n  # 939.565
m_e = c.m_e  # 0.511
alpha = c.alpha  # 1/137
u = c.physical_constants.get('atomic mass constant energy equivalent in MeV')[0]
hc = c.h * c.c  # 197.3269631
c = c.c  # 299792458


a_v = 15.753
a_s = 17.804
a_c = 0.7103
a_A = 23.69
r_0 = 1.2513


def q(m1, m2, m3, m4):
    return m1+m2-m3-m4


def t1(m1, m2, m3, m4):
    return ((m3+m4)**2-(m1+m2)**2)/(2*m2)


def b(m1, m2, m3, m4):
    return math.sqrt(t1(m1, m2, m3, m4)**2 + 2*m1*t1(m1, m2, m3, m4))/(t1(m1, m2, m3, m4)+m1+m2)


def t3(m1, m2, m3, m4):
    return ((q(m1, m2, m3, m4)+t1(m1, m2, m3, m4))*(q(m1, m2, m3, m4)+t1(m1, m2, m3, m4)+2*m4) + b(m1, m2, m3, m4)**2*(m3**2-m4**2)/(1-b(m1, m2, m3, m4)**2))/(2*(q(m1, m2, m3, m4)+t1(m1, m2, m3, m4)+m3+m4))


def t4(m1, m2, m3, m4):
    return q(m1, m2, m3, m4) + t1(m1, m2, m3, m4) - t3(m1, m2, m3, m4)


def t(m1, m2, m3, m4):
    return 1/math.sqrt(1-b(m1, m2, m3, m4)**2)*(m1+m2-q(m1, m2, m3, m4)) - (m1+m2) - 20


# Cálculo y resultados:
m1 = 938.3
m2 = 938.3
m3 = 273*m_e
m4 = 939.6+938.3

print(q(m1, m2, m3, m4))
print(t1(m1, m2, m3, m4))
print(b(m1, m2, m3, m4))
# print (t3(m1,m2,m3,m4))
# print (t4(m1,m2,m3,m4))
print(t(m1, m2, m3, m4))
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:45:00 2020

@author: jhon_
"""


a_v = 15.753
a_s = 17.804
a_c = 0.7103
a_A = 23.69
m_p = 938.272013
m_n = 939.565560
m_e = 0.511  # 0998910
c = 299792458
r_0 = 1.2513
alpha = 1/137.035999679
hc = 197.3269631
u = 931.5


def q(m1, m2, m3, m4):
    return m1+m2-m3-m4


def t1(m1, m2, m3, m4):
    return ((m3+m4)**2-(m1+m2)**2)/(2*m2)


def b(m1, m2, m3, m4):
    return math.sqrt(t1(m1, m2, m3, m4)**2 + 2*m1*t1(m1, m2, m3, m4))/(t1(m1, m2, m3, m4)+m1+m2)


def t3(m1, m2, m3, m4):
    return ((q(m1, m2, m3, m4)+t1(m1, m2, m3, m4))*(q(m1, m2, m3, m4)+t1(m1, m2, m3, m4)+2*m4) + b(m1, m2, m3, m4)**2*(m3**2-m4**2)/(1-b(m1, m2, m3, m4)**2))/(2*(q(m1, m2, m3, m4)+t1(m1, m2, m3, m4)+m3+m4))


def t4(m1, m2, m3, m4):
    return q(m1, m2, m3, m4) + t1(m1, m2, m3, m4) - t3(m1, m2, m3, m4)


def t(m1, m2, m3, m4):
    return 1/math.sqrt(1-b(m1, m2, m3, m4)**2)*(m1+m2-q(m1, m2, m3, m4)) - (m1+m2) - 20


# Cálculo y resultados:
m1 = 938.3
m2 = 938.3
m3 = 273*m_e
m4 = 939.6+938.3

print(q(m1, m2, m3, m4))
print(t1(m1, m2, m3, m4))
print(b(m1, m2, m3, m4))
# print (t3(m1,m2,m3,m4))
# print (t4(m1,m2,m3,m4))
print(t(m1, m2, m3, m4))
