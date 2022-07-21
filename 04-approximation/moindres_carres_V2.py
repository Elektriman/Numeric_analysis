# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:35:03 2020

@author: Julien
"""

import matplotlib.pyplot as plt
import numpy as np

'''
jeu de données
'''

X1 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
Y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

X2 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
Y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]

X3 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
Y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]

X4 = [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 19.0, 8.0, 8.0, 8.0]
Y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

def VDM(X,p):
    A = []
    for i in range(p+1):
        A.append(X**i)
    return np.flip(np.array(A),0).transpose()

def poly(X,Y,p):
    X,Y = np.array(X),np.array(Y)
    A = VDM(X,p)
    tA = A.transpose()
    tY = Y.transpose()
    
    M = np.dot(tA,A)
    N = np.dot(tA,tY)
    
    return np.linalg.solve(M,N)

def func(coef):
    return lambda x : coef[0]*x**2 + coef[1]*x + coef[2]

j=0
def plot(X,Y,ax):
    global j
    coef = poly(X,Y,2)
    ax.scatter(X,Y, label=f'data')
    x = np.linspace(min(X),max(X),1000)
    ax.plot(x, func(coef)(x), c='C01', label='approx')
    ax.legend()
    ax.axis('equal')
    ax.set_facecolor([0.53,0.54,1/(j+1),1])
    ax.set_title(f'jeu de données {j}')
    j+=1

fig,ax = plt.subplots(1,4, figsize=(10,2.5))

plot(X1,Y1,ax[0])
plot(X2,Y2,ax[1])
plot(X3,Y3,ax[2])
plot(X4,Y4,ax[3])