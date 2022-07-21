# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:29:55 2020

@author: Julien
"""


import matplotlib.pyplot as plt
import numpy as np

def fact(n):
    if n==0 :
        return 1
    else :
        return n*fact(n-1)

X1 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
Y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

plt.scatter(X1,Y1, label='data')

A = np.ones((len(X1),2))
A[:,0] = np.array(X1)

Y = np.array(Y1)

M = np.linalg.lstsq(A, Y, 0)

approx = lambda x : M[0][0]*x + M[0][1]
X = np.linspace(min(X1)-1,max(X1)+1,100)

plt.plot(X, approx(X), c='C01', zorder=-1, label='approximation')
plt.legend()