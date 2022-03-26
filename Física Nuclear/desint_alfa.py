# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:34:29 2020

@author: jhon_
"""

import math

a_v = 15.753
a_s = 17.804
a_c = 0.7103
a_A = 23.69
m_p = 938.272013
m_n = 939.565560
m_e = 0.510998910
c = 299792458
r_0 = 1.4  # 2513
alpha = 1/137  # .035999679
hc = 197.326  # 9631
c1 = 8*math.sqrt(alpha*r_0/hc)
c2 = 2*math.pi*alpha*math.sqrt(2)

# print('Todos los cálculos en adelante son  tratados considerando el modelo de la gota líquida\n')

# Defino la función energía de enlace del nucleo según el módelo semiempírico de masas de Bethe-Weizsacker


def delta(A, Z):
    if A % 2 == 1:
        return 0
    elif Z % 2 == 0:
        return 33.6*math.pow(A, -3/4)
    else:
        return -33.6*math.pow(A, -3/4)


def B(A, Z):
    return a_v*A - a_s*math.pow(A, 2/3) - a_c*Z**2*math.pow(A, -1/3) - a_A*(A-2*Z)**2*A**(-1) + delta(A, Z)

# Defino la función masa del núcleo según el módelo semiempírico de masas de Bethe-Weizsacker


def r(A):
    return r_0*A**(1/3)


def m(A, Z):
    return Z*m_p + (A-Z)*m_n - B(A, Z)


# Defino la función decaimiento alfa según el módelo semiempírico de masas de Bethe-Weizsacker

# if A>4 and Z>=2:

def q_a(A, Z):
    return B(A-4, Z-2) + B(4, 2) - B(A, Z)
    # return m(A,Z) - m(4,2) - m(A-4,Z-2)

# masa reducida


def m_r(A, Z):
    return m(A-4, Z-2) * m(4, 2)/(m(A-4, Z-2) + m(4, 2))

# masa reducida aproximada


def m_ra(A):
    return 4*931.494028/(1 + 4/A)

# frecuencia de interacción con la barrera de Coulomb


def f(A, Z):
    return math.sqrt(q_a(A, Z)/(2*m_r(A, Z)))/(r(A-4)+r(4))*c*10**15

# barrera de potencial


def B_p(A, Z):
    return 2*(Z-2)*alpha*hc/(r(A-4)+r(4))

# probabilidad de transmisión a través de la barrera de potencial


def T(A, Z):
    return math.exp(-4*(Z-2)*alpha*math.sqrt(2*m_r(A, Z)/q_a(A, Z))*(math.acos(math.sqrt(q_a(A, Z)/B_p(A, Z))) - math.sqrt(q_a(A, Z)/B_p(A, Z) - (q_a(A, Z)/B_p(A, Z))**2)))

# Probabilidad de transmisión aproximada a través de la barrera de potencial


def Ta(A, Z):
    return math.exp(c1*math.sqrt(m_r(A, Z)*(Z-2)*A**(1/3)) - c2*(Z-2)*math.sqrt(m_r(A, Z)/q_a(A, Z)))

# Fórmula empírica de Brown


def t_m(A, Z):
    return 10**(-51.37 + 9.54*(Z-2)**(3/5)*q_a(A, Z)**(-1/2))

# Definición de funciones extras:


def f_(q, A, Z):
    return math.sqrt(q/(2*m_r(A, Z)))*c*10**15/r(A)


def T_(q, A, Z):
    return math.exp(-4*(Z-2)*alpha*math.sqrt(2*m_r(A, Z)/q)*(math.acos(math.sqrt(q/B_p(A, Z))) - math.sqrt(q/B_p(A, Z) - (q/B_p(A, Z))**2)))


def Ta_(q, A, Z):
    return math.exp(c1*math.sqrt(m_r(A, Z)*(Z-2)*A**(1/3)) - c2*(Z-2)*math.sqrt(m_r(A, Z)/q))


def t_m_(q, A, Z):
    return 10**(-51.37 + 9.54*(Z-2)**(0.6)*q**(-1/2))

# Cálculo y resultados:


m1 = m(4, 2)
m2 = m(208, 82)
t1 = 8.78
b = math.sqrt(t1**2+2*m1*t1)/(t1+m1+m2)
print(m1)
print(m2)
print(b)


E = math.sqrt(1-b**2)*(t1+m1+m2)

print(E)



# print (T(212,84))

x = math.sqrt((q_a(212, 84)+8.78)/(2*m_r(212, 84)))/(r(208)+r(4))*c*10**15

# print (x)

# m(152,62)

# tr = 0.963**2/(2*m(152,62))
# print (tr)

# e1 = 0.963-tr
# e2 =0.963+tr
# print (e1)
# print (e2)
s = 3*math.sqrt(math.log(2))*0.963*math.sqrt(300*8.6*10**(-5)/(152*10**9))

pa = math.log(2)/(3*10**(-7)*1.1684*10**21*2.9136*10**(-39))

print(pa)
