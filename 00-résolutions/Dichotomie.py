# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:07:57 2020

@author: Julien
"""

import numpy as np
import matplotlib.pyplot as plt


def dichoTab(f, a, b, e):
    res = []
    while b-a > e :
        c = (a+b)/2
        res.append(c)
        C = f(c)
        if f(a)*C<0 :
            b=c
        elif f(b)*C<0 :
            a=c
        elif f(a)==0.0 :
            return a
        elif f(b)==0.0 :
            return b
        else :
            return None
    return res

def f(x):
    return (x**2+2*x-5)

X = np.linspace(-5,2.5,1000)
Y = f(X)
plt.plot(X,Y)
plt.grid(True)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

R = dichoTab(f, -5, 2.5, 10**-4)
for i in range(len(R)):
    plt.axvline(x=R[i], c='orange', alpha=0.5)
plt.plot(R[-1],0, marker='o', c='r')

















