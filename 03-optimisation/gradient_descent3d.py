# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:59:21 2020

@author: Julien
"""

import matplotlib.pyplot as plt

from scipy.misc import derivative

import numpy as np

def grad(f):
    h = 10**-5
    gradient = lambda x,y : (derivative(lambda x : f(x,y), x, dx=h),derivative(lambda y : f(x,y), y, dx=h))
    return gradient

f = lambda x,y : 4*np.exp(-(x**2/2 + y**2/4))*np.sin(x*(y-1/2))*np.cos(x/2+y)
grad_f = grad(f)

pas = 0.1
x0,y0 = 0.65,-0.3
P = [[x0,y0,f(x0,y0)]]

def chemin(P, pas) :
    d = 1
    i = 0
    while d>0.01 and i<1000 :
        x,y = P[-1][0],P[-1][1]
        u,v = grad_f(x,y)
        d = np.sqrt(u**2+v**2)
        if pas<d :
            u,v = u*pas/d,v*pas/d
        
        P.append([x+u,y+v,f(x+u,y+v)])
        i+=1

chemin(P, pas)
P = np.array(P)

fig2 = plt.figure()
ax2 = fig2.gca(projection='3d')

X = np.linspace(-5,5,100)
Y = np.linspace(-5,5,100)
XX,YY = np.meshgrid(X,Y)
Z = f(XX,YY)

surf = ax2.plot_surface(XX, YY, Z, cmap='RdBu')
plt.plot(P[:,0],P[:,1],P[:,2], color='C02', zorder=3, ls='--')
fig2.colorbar(surf)
plt.show()