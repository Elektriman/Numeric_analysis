# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:40:17 2020

@author: Julien
"""

import matplotlib.pyplot as plt

import numpy as np

fig,ax = plt.subplots(1,1)

X = np.linspace(-5,5,1000)
Y = np.linspace(-5,5,1000)
XX,YY = np.meshgrid(X,Y)
f = lambda x,y : 4*np.exp(-(x**2/2 + y**2/4))*np.sin(x*(y-1/2))*np.cos(x/2+y)

colormap = ax.pcolormesh(XX,YY,f(XX,YY), cmap='RdBu')
fig.colorbar(colormap)


# fig2 = plt.figure()
# ax2 = fig2.gca(projection='3d')

# X = np.linspace(-5,5,50)
# Y = np.linspace(-5,5,50)
# XX,YY = np.meshgrid(X,Y)
# f = lambda x,y : 4*np.exp(-(x**2/2 + y**2/4))*np.sin(x*(y-1/2))*np.cos(x/2+y)
# Z = f(XX,YY)
# 
#surf = ax2.plot_surface(XX, YY, Z, cmap='RdBu')
#fig2.colorbar(surf)
plt.show()