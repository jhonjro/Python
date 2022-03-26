# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:34:29 2020

@author: jhon_
"""

#import numpy as np
#import matplotlib.pyplot as plt
import math

a_v = 15.753
a_s = 17.804
a_c = 0.7103
a_A = 23.69
m_p = 938.272013
m_n = 939.565560
m_e = 0.510998910
c = 299792458
r_0 = 1.2513
alpha = 1/137.035999679
hc = 197.3269631
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
    return (Z*m_p + (A-Z)*m_n - B(A, Z))


# Defino la función decaimiento alfa según el módelo semiempírico de masas de Bethe-Weizsacker

# if A>4 and Z>=2:

def q_a(A, Z):
    return B(A-4, Z-2) + B(4, 2) - B(A, Z)

# else:
#     print('No es posible el decaimiento alfa de este núcleo')

# masa reducida


def m_r(A, Z):
    return m(A-4, Z-2) * m(4, 2)/(m(A-4, Z-2) + m(4, 2))

# masa reducida aproximada


def m_ra(A):
    return 4*931.494028/(1 + 4/A)

# frecuencia de interacción con la barrera de Coulomb


def f(A, Z):
    return math.sqrt(q_a(A, Z)/(2*m_r(A, Z)))/r(A)*c*10**15

# barrera de potencial


def B_p(A, Z):
    return 2*(Z-2)*alpha*hc/r(A)

# probabilidad de transmisión a través de la barrera de potencial


def T(A, Z):
    return math.exp(-4*(Z-2)*alpha*math.sqrt(2*m_r(A, Z)/q_a(A, Z))*(math.acos(math.sqrt(q_a(A, Z)/B_p(A, Z))) - math.sqrt(q_a(A, Z)/B_p(A, Z) - (q_a(A, Z)/B_p(A, Z))**2)))

# probabilidad de transmisión aproximada a través de la barrera de potencial


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


print('Cáculos realizados:')

ru = f_(7.33, 244, 98)*T_(7.33, 244, 98)*19.4*60/(f(228, 90)*T(228, 90))
# ru = f(244,98)*T(244,98)*t_m(244,98)/(f(228,90)*T(228,90))

print('Tiempo de vida media de Th : ' + str(ru) + ' s')
print('Tiempo de vida media de Th según Brown : ' + str(t_m(228, 90)) + ' s')

p_a = math.log(2)/(f_(7.33, 244, 98)*T_(7.33, 244, 98)*19.4*60)
# p_a =  math.log(2)/(f(244,98)*T(244,98)*t_m(244,98))
print('Probabilidad de preformación : ' + str(p_a))
error = math.fabs(ru - t_m(228, 90))/ru*100

print('Error : ' + str(error) + ' %')

re = input('¿Continuar?[y/n] : ')

while re == 'y' or re == 'Y':
    Z = float(input('Ingrese el número atómico: '))
    A = float(input('Ingrese el número másico: '))
    print('\nEnergía de enlace : ' + str(B(A, Z)) + ' MeV')
    print('Masa nuclear : ' + str(m(A, Z)) + ' MeV/c^2')
    print('Masa nuclear : ' + str(m(A, Z)/931.5) + ' uma')
    print('Q_a :' + str(q_a(A, Z)) + ' Mev')
    if q_a(A, Z) > 0:
        print('El decaimiento alfa de este núcleo es espontáneo')
    else:
        print('El decaimiento alfa de este núcleo no es espontáneo')
    print('Masa reducida : ' + str(m_r(A, Z)) + ' MeV/c^2')
    print('Masa reducida aprox. : ' + str(m_ra(A)) + ' MeV/c^2')
    print('Frecuencia de interacción : ' + str(f(A, Z)) + ' s^-1')
    print('barrera de potencial es ' + str(B_p(A, Z)))
    print('Probabilidad de trasmisión : ' + str(T(A, Z)))
    print('Tiempo de vida media según Brown : ' + str(t_m(A, Z)) + ' s')
    re = input('¿Continuar? [y/n] : ')
