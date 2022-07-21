# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 19:25:50 2020

@author: Julien
"""

import numpy as np

import matplotlib.pyplot as plt

X = np.array([-3.0,-2.1,-1.9,-1.1,-0.9, 0.9, 1.1, 1.9, 2.1, 3.0])
Y = np.array([-1.0,-1.0, 1.0, 1.0,-2.0,-2.0, 2.0, 2.0, 0.0, 0.0])

def tracer(X,Y):
    for i in range(len(X)-1):
        plt.plot([X[i],X[i+1]],[Y[i],Y[i+1]], c='C01')
plt.scatter(X,Y, c='C01')
plt.title('ligne brisée')

tracer(X,Y)
plt.show()