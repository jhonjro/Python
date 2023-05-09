# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:57:54 2020

@author: jhon_
"""

import math

l = 0
k = 0
def fn(n):
    return math.sqrt((n*(n+1)-2)/30)
def fr(n):
    return (5*n*(n+1)-16)/42
while l<3:
    n = 10*k+1
    if fn(n)%1 == 0 and fr(n)%1 == 0:
        A= n*(n+1)/2
        B= 5*((n*(n+1)-2)/6)
        C= 11*(5*n*(n+1)-16)/42
        print ('A= ' + str(A) + ', B= ' + str(B) + ', C= ' + str(C))
        l+=1
    n= 10*k+3
    if fn(n)%1 == 0 and fr(n)%1 == 0:
        A= n*(n+1)/2
        B= 5*((n*(n+1)-2)/6)
        C= 11*(5*n*(n+1)-16)/42
        print ('A= ' + str(A) + ', B= ' + str(B) + ', C= ' + str(C))
        l+=1
    n = 10*k+6
    if fn(n)%1 == 0 and fr(n)%1 == 0:
        A= n*(n+1)/2
        B= 5*((n*(n+1)-2)/6)
        C= 11*(5*n*(n+1)-16)/42
        print ('A= ' + str(A) + ', B= ' + str(B) + ', C= ' + str(C))
        l+=1
    n = 10*k+8
    if fn(n)%1 == 0 and fr(n)%1 == 0:
        A= n*(n+1)/2
        B= 5*((n*(n+1)-2)/6)
        C= 11*(5*n*(n+1)-16)/42
        print ('A= ' + str(A) + ', B= ' + str(B) + ', C= ' + str(C))
        l+=1
    k+=1