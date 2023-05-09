# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:02:25 2020

@author: jhon_
"""


def busquedaBinaria(Lista, item):
    low = 0
    high = len(Lista)-1
    encontrado = False
    while (low <= high) and not encontrado:
        mid = (low + high)//2
        if Lista[mid] == item:
            encontrado = True
        else:
            if item < Lista[mid]:
                high = mid-1
            else:
                low = mid+1
    return encontrado


lista1 = [3, 2, 22, 40, 50, 66, 98]

print(busquedaBinaria(lista1, 67))
