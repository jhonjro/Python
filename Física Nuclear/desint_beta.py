# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:30:56 2020

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
r_0 = 1.2513
alpha = 1/137.035999679
hc = 197.3269631
uma = 931.494028

#Defino la función energía de enlace del nucleo según el módelo semiempírico de masas de Bethe-Weizsacker

def delta(A,Z):
        if A%2==1:
            return 0
        elif Z%2==0:
            return 33.6*math.pow(A,-3/4)
        else:
            return -33.6*math.pow(A,-3/4)

# Energía de enlace nuclear

def B(A,Z):
    return a_v*A - a_s*math.pow(A,2/3) - a_c*Z**2*math.pow(A,-1/3) - a_A*(A-2*Z)**2*A**(-1) + delta(A,Z)

#Defino la función masa del núcleo según el módelo semiempírico de masas de Bethe-Weizsacker

# Radio nuclear

def r(A):
    return r_0*A**(1/3)

# Masa nuclear

def m(A,Z):
    return Z*m_p + (A-Z)*m_n - B(A,Z)

# Masa atómica añadiendo la energía de enlace electrónico

def M(A,Z):
    return m(A,Z) + Z*m_e -15.75*Z**(7/3)*10**(-6)

#  Defecto de masas

def dm(A,Z):
    return M(A,Z) - uma*A

def q_bn(A,Z):
    return B(A,Z+1) - B(A,Z) +  m_n - m_p - m_e

def q_bp(A,Z):
    return m(A,Z) - m(A,Z-1) - m_e

def q_bc(A,Z):
    return m(A,Z) - m(A,Z-1) + 2*m_e

def n(x):
    return (1/15*(2*x**4-9*x**2-8) * math.sqrt(x**2-1) + x*math.log(x + math.sqrt(x**2-1)))

def tvm(x):
    return (1.16637)**2*(m_e)**5*2.4**2/(8*math.pi**3*6.58211899) * (1/15*(2*x**4-9*x**2-8) * math.sqrt(x**2-1) + x*math.log(x + math.sqrt(x**2-1)))

def constIW(x):
    return math.sqrt(8.867/((m_e)**5/(8*math.pi**3*6.58211899) * (1/15*(2*x**4-9*x**2-8) * math.sqrt(x**2-1) + x*math.log(x + math.sqrt(x**2-1)))))

# Cálculo y resultados:
























