# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 16:03:07 2020

@author: jhon_
"""
data = [['Ana', 13, 15, 16],
        ['Juan', 18, 13, 17],
        ['Jorge', 19, 19, 18],
        ['Mario', 3, 18, 19],
        ['Marlon', 14, 5, 12],
        ['Julio', 13, 7, 13]]


def indice_menor_elemento(lista):
    menor = lista[0][valor]
    indice = 0
    for i in range(len(lista)):
        if lista[i][valor] < menor:
            menor = lista[i][valor]
            indice = i
    return indice


def ordenar(lista):
    for i in range(len(lista)):
        indice = indice_menor_elemento(lista[i:])
        aux = lista[indice + i]
        lista[indice + i] = lista[i]
        lista[i] = aux
    return lista


dic = {
    'nombre': 0,
    'prac': 1,
    'lab': 2,
    'proy': 3
}
j = True
while j:
    x = input('Por cual columna ordeno ')
    if x == '0':
        j = False
    else:
        valor = dic.get(x)
        ordenar(data)
        for i in range(len(data)):
            print(data[i])
