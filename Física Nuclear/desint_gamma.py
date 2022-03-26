# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 00:08:53 2020

@author: jhon_
"""


import math
from decimal import Decimal

a_v = 15.753
a_s = 17.804
a_c = 0.7103
a_A = 23.69
m_p = 938.272013
m_n = 939.565560
m_e = 0.511#0998910
c = 299792458
r_0 = 1.2#513
alpha = 1/137#.035999679
hc = 197#.3269631
u = 931.5


# factorial doble

def fd(l):
    if l%2==0:
        k=l/2
        return 2**k*math.factorial(k)
    else:
        k=(l+1)/2
        return math.factorial(l)/(2**(k-1)*math.factorial(k-1))

# Radio del núcleo

def r(A):
    return r_0*math.pow(A,1/3)

# Constante de desintegración gamma eléctrico

def gE(E,A,l):
    return 2*(l+1)/(l*fd(2*l+1)**2)*math.pow(3/(l+3),2)*math.pow(E/hc, 2*l+1)*alpha*c*math.pow(r(A),2*l)*10**15

# Constante de desintegración gamma magnético

def gM(E,A,l):
    return 20*(l+1) / (l*fd(2*l+1)**2) * math.pow(3/(l+3),2) * (hc/m_p)**2 * math.pow(E/hc, 2*l+1) * alpha * c * math.pow(r(A),2*l-2) * 10**15

# Tiempo de vida media modo 1 primero E

def tau1(E,A,j1,j2):
    t=0
    for l in range(math.floor(math.fabs(j1-j2)), math.floor(j1+j2+1), 2):
        t += gE(E,A,l)
        print ('E' + str(l) + ': ' +  '%E' %Decimal(gE(E,A,l)))
        if l+1 <= j1+j2:
            t += gM(E,A,l+1)
            print ('M' + str(l+1) + ': ' + '%E' %Decimal(gM(E,A,l+1)))
            if l+1 == j1+j2:
                print ('lambda : ' + '%E' %Decimal(t))
        else:
            t+= 0
            print ('lambda : ' + '%E' %Decimal(t))
    return math.log(2)/t

# Tiempo de vida media modo 2 primero M

def tau2(E,A,j1,j2):
    t=0
    for l in range(math.floor(math.fabs(j1-j2)), math.floor(j1+j2+1), 2):
        t += gM(E,A,l)
        print ('M' + str(l) + ': ' + '%E' %Decimal(gM(E,A,l)))
        if l+1 <= j1+j2:
            t += gE(E,A,l+1)
            print ('E' + str(l+1) + ': ' + '%E' %Decimal(gE(E,A,l+1)))
            if l+1 == j1+j2:
                print ('lambda : ' + '%E' %Decimal(t))
        else:
            t+= 0
            print ('lambda : ' + '%E' %Decimal(t))
    return math.log(2)/t

# Cálculo y resultados:

print ('%E' % tau1(0.9,16,2,3))
