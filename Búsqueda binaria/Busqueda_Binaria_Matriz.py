# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:24:28 2020

@author: jhon_
"""

myNames = []
f = open('names.txt', 'r')

for line in f:
    myNames.append([int(x) for x in line.strip().split()])

x = []
for i in myNames:
    x += i

myNames = x
print(myNames)


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


print(busquedaBinaria(myNames, 12))
