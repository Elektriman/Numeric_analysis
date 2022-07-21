# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 19:24:35 2020

@author: Julien
"""

import numpy as np

import matplotlib.pyplot as plt

from scipy.interpolate import interp1d

X = np.array([-3.0,-2.1,-1.9,-1.1,-0.9, 0.9, 1.1, 1.9, 2.1, 3.0])
Y = np.array([-1.0,-1.0, 1.0, 1.0,-2.0,-2.0, 2.0, 2.0, 0.0, 0.0])

N = np.arange(X.shape[0])
U = np.linspace(N[0], N[-1], 1000)

fig, ax = plt.subplots(1,4, figsize=(20,5))
k = ['linear', 'nearest', 'cubic', 'quadratic']
for i in range(len(k)):
    fx = interp1d(N,X, kind=k[i])
    ax[i].scatter(N,X)
    ax[i].plot(U, fx(U))
    ax[i].set_title(k[i])
    ax[i].axis('equal')
plt.show()
