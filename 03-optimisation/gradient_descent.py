# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:45:50 2020

@author: Julien
"""

import matplotlib.pyplot as plt

from scipy.misc import derivative

import numpy as np

def grad(f):
    h = 10**-5
    gradient = lambda x,y : (derivative(lambda x : f(x,y), x, dx=h),derivative(lambda y : f(x,y), y, dx=h))
    return gradient

fig,ax = plt.subplots(1,1)

X = np.linspace(-5,5,1000)
Y = np.linspace(-5,5,1000)
XX,YY = np.meshgrid(X,Y)

f = lambda x,y : 4*np.exp(-(x**2/2 + y**2/4))*np.sin(x*(y-1/2))*np.cos(x/2+y)
grad_f = grad(f)

pas = 0.1
P = [[0.65,-0.3]]
U,V = [],[]

def chemin(P, pas) :
    d = 1
    i = 0
    while d>0.01 and i<1000 :
        x,y = P[-1][0],P[-1][1]
        u,v = grad_f(x,y)
        d = np.sqrt(u**2+v**2)
        if pas<d :
            u,v = u*pas/d,v*pas/d
            
        U.append(u)
        V.append(v)
        
        P.append([x+u,y+v])
        i+=1

chemin(P, pas)
P = np.array(P)
#ax.plot(P[:,0],P[:,1], c='C02')
ax.quiver(P[:-1,0],P[:-1,1],U,V, zorder=3)
ax.axis('equal')

colormap = ax.pcolormesh(XX,YY,f(XX,YY), cmap='RdBu')
fig.colorbar(colormap)
plt.show()