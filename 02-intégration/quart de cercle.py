# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:30:13 2020

@author: Julien
"""

import numpy as np
import matplotlib.pyplot as plt
from  scipy.integrate import quad

f = lambda x:np.sqrt(1-x**2)
X = np.linspace(0,1,1000)
plt.plot(X,f(X),zorder=3,lw=3)
N=1000
R = np.random.random((N,2))
EstDessous = R[:,1]<f(R[:,0])
EstDessus = R[:,1]>f(R[:,0])
plt.scatter(R[:,0][EstDessous],R[:,1][EstDessous],marker='.',c='r')
plt.scatter(R[:,0][EstDessus],R[:,1][EstDessus],marker='.',c='k')

print((len(R[EstDessous])/N))
print(quad(f,0,1)[0])