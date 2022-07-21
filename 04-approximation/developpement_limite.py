# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:24:53 2020

@author: Julien
"""


import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np
import math

def fact(n):
    if n==0 :
        return 1
    else :
        return n*fact(n-1)

def DL(f,a,n):
    return lambda x : np.array([((x-a)**i)*derivative(f, a, 10**-5, i, order=2*i+1)/fact(i) for i in range(n)]).sum()

# def DL(f, a, n):
#     def Result(x):
#         result = 0
#         for m in range(n):
#             df = derivative(f,a,10**-5, m, order=2*n+1)
#             result += ((x - a)**m) * (df/math.factorial(m))
#         return result
#     return Result
    

X = np.linspace(-10,10,1000)
f = lambda x : np.exp(-x/4)*np.sin(4*x)
Y = f(X)
plt.plot(X,Y, label='f(x)')

n = 4
a = 1
for i in range(1,n+1):
    Y = X.copy()
    g = DL(f,a,i)
    for j in range(len(Y)):
        Y[j] = g(Y[j])
    plt.plot(X,Y, label=f'développement à l\'ordre {i}')
    plt.ylim(-12,12)
plt.legend()