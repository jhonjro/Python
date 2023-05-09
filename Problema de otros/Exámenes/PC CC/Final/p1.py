# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 16:01:08 2020

@author: jhon_
"""

precios = []
f = open('precios.txt', 'r', encoding='utf-8')

for line in f:
    precios.append(line.strip().split(';'))


precios = precios[1:]
# print(precios)


def indice_mayor_elemento(lista):
    mayor = lista[0]
    indice = 0
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            indice = i
    return indice


y = [fila[2] for fila in precios]
y = [float(j) for j in y]
i = indice_mayor_elemento(y)

print('Nombre de producto: {}'.format(precios[i][0]))
print('Farmacia: {}'.format(precios[i][1]))
print('Precio unitario: {}'.format(precios[i][2]))
