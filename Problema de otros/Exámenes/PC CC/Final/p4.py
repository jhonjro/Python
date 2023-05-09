# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 16:03:14 2020

@author: jhon_
"""

data = [{'nombre': 'Ana', 'teoria': 13, 'lab': 11},
        {'nombre': 'Jorge', 'teoria': 15, 'lab': 13},
        {'nombre': 'Juan', 'teoria': 17, 'lab': 15},
        {'nombre': 'Marlon', 'teoria': 11, 'lab': 17},
        {'nombre': 'Lucas', 'teoria': 14, 'lab': 19},
        {'nombre': 'Derek', 'teoria': 19, 'lab': 20}]


def indice_menor_elemento(lista):
    menor = lista[0].get('nombre')
    indice = 0
    for i in range(len(lista)):
        if lista[i].get('nombre') < menor:
            menor = lista[i].get('nombre')
            indice = i
    return indice


def ordenar(lista):
    for i in range(len(lista)):
        indice = indice_menor_elemento(lista[i:])
        aux = lista[indice + i]
        lista[indice + i] = lista[i]
        lista[i] = aux
    return lista


data = ordenar(data)


def busquedaBinaria(Lista, item):
    low = 0
    high = len(Lista)-1
    encontrado = False
    while (low <= high) and not encontrado:
        mid = (low + high)//2
        if Lista[mid].get('nombre') == item:
            encontrado = True
        else:
            if item < Lista[mid].get('nombre'):
                high = mid-1
            else:
                low = mid+1
    print('Nota teoria: {}'.format(Lista[mid].get('teoria')))
    print('Nota practica: {}'.format(Lista[mid].get('lab')))


item = input('Ingrese nombre: ')
busquedaBinaria(data, item)
