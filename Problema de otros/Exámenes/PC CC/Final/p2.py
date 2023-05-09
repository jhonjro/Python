# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 16:01:08 2020

@author: jhon_
"""


def contar(cadena):
    j = 0
    for i in cadena:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            j += 1
    return j


h = input('Ingrese una cadena : ')

print(contar(h))
