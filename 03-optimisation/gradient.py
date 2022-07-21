# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:04:42 2020

@author: Julien
"""

import matplotlib.pyplot as plt

import numpy as np


fig,ax = plt.subplots(1,1)

X = np.linspace(-5,5,1000)
Y = np.linspace(-5,5,1000)
XX,YY = np.meshgrid(X,Y)

f = lambda x,y : 4*np.exp(-(x**2/2 + y**2/4))*np.sin(x*(y-1/2))*np.cos(x/2+y)
dx = lambda x,y : -4*x*np.exp(-(x**2/2 + y**2/4))*np.sin(x*(y-1/2))*np.cos(x/2+y)+4*np.exp(-(x**2/2 + y**2/4))*(y-1/2)*np.cos(x*(y-1/2))*np.cos(x/2+y)-4*np.exp(-(x**2/2 + y**2/4))*np.sin(x*(y-1/2))*0.5*np.sin(x/2+y)
dy = lambda x,y : -2*y*np.exp(-(x**2/2 + y**2/4))*np.sin(x*(y-1/2))*np.cos(x/2+y)+4*np.exp(-(x**2/2 + y**2/4))*x*np.cos(x*(y-1/2))*np.cos(x/2+y)-4*np.exp(-(x**2/2 + y**2/4))*np.sin(x*(y-1/2))*np.sin(x/2+y)

def grad(x,y):
    return (dx(x,y),dy(x,y))

colormap = ax.pcolormesh(XX,YY,f(XX,YY), cmap='RdBu')
fig.colorbar(colormap)
a = np.linspace(-5,5,100)
b = np.linspace(-5,5,100)
aa,bb = np.meshgrid(a,b)
U,V = dx(aa,bb),dy(aa,bb)
plt.quiver(aa,bb,U,V, scale=100)
plt.title('gradient de f à l\'échelle 1/100')
plt.show()