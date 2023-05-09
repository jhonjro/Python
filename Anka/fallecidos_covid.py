# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 09:17:02 2021

@author: jhon_
"""

import pandas as pd
import numpy as np

import os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)

# df = pd.read_csv(BASE_DIR + '\\Prueba de entrevista\\' + 'fallecidos_covid.txt', sep=";", encoding='ISO-8859-1')
df = pd.read_csv(CURR_DIR + '\\fallecidos_covid.txt', sep=";", encoding='ISO-8859-1')

print('Pregunta 1')
print(df)

# Pregunta 1

df1 = df[df.FECHA_FALLECIMIENTO.isin([20200825])]
df1.head()
print(df1)

# Pregunta 2
print('Pregunta 2')
df2 = df[df.DEPARTAMENTO.isin(['AREQUIPA'])]
df2.head()
df3 = df[df['FECHA_FALLECIMIENTO'] <= 20201024]
df4 = df3[20200430 <= df3['FECHA_FALLECIMIENTO']]

print(df4)

# Pregunta 3
print('Pregunta 3')
# fmin = df.loc[df['FECHA_FALLECIMIENTO'].idxmin()].10

# fmax = df.loc[df['FECHA_FALLECIMIENTO'].idxmax()]
# # TOTAL DE 239 DÍAS
# tasa_muerte = len(df)/239
# print(tasa_muerte)


t = len(pd.unique(df['FECHA_FALLECIMIENTO']))
print(len(df)/t)
print()


# Pregunta 4
print('Pregunta 4')
n = 15
# n = int(input('Ingrese un número :'))
i = 0
while n >= pow(2, i):
    i += 1
r = n-pow(2, i-1)

c = np.arange(i-1) + 1


def potencia(c):
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]


def combinaciones(c):
    l = np.array([])
    for e in sorted(c, key=lambda s: (len(s), s)):
        x = 0
        for k in e:
            x += pow(5, k)
        l = np.append(l, x)
    l = sorted(l)
    print(int(pow(5, i) + l[r]))


combinaciones(potencia(c))

# Pregunta 4 (sol alter)


def binary(n):
    if n == 1:
        return [1]
    else:
        return [n % 2] + binary(n//2)


x = 0
for i in range(len(binary(n))):
    x += pow(5, i+1)*binary(n)[i]
print(x)


# q = np.unique(df['EDAD_DECLARADA'], return_counts=True)
# print(q)
c = np.argmax(df['EDAD_DECLARADA'])

print(np.unique(df['EDAD_DECLARADA'])*[np.argmax(df['EDAD_DECLARADA'])])


# Método alternativo

# import codecs
# from itertools import groupby

# def read_fuente(file):
#     data=[]
#     with open(file,encoding='ISO-8859-1') as f:
#             for line in f:#fic.readlines():
#                 data.append(line)

#     diccionario_covid={'FECHA_CORTE':[],'UUID':[],'FECHA_FALLECIMIENTO':[],
# 'EDAD_DECLARADA':[],'SEXO':[],'FECHA_NAC':[],'DEPARTAMENTO':[],
# 'PROVINCIA':[],'DISTRITO':[]}

#     for line in data[1:]:
#         string_campos=line.split(';')
#         # print(string_campos)
#         diccionario_covid['FECHA_CORTE'].append(string_campos[0])
#         diccionario_covid['UUID'].append(string_campos[1])
#         diccionario_covid['FECHA_FALLECIMIENTO'].append(string_campos[2])
#         diccionario_covid['EDAD_DECLARADA'].append(string_campos[3])
#         diccionario_covid['SEXO'].append(string_campos[4])
#         diccionario_covid['FECHA_NAC'].append(string_campos[5])
#         diccionario_covid['DEPARTAMENTO'].append(string_campos[6])
#         diccionario_covid['PROVINCIA'].append(string_campos[7])
#         diccionario_covid['DISTRITO'].append(string_campos[8])

#     return diccionario_covid

# read_fuente('fallecidos_covid.txt')
