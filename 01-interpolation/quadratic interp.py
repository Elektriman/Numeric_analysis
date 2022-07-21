# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 19:40:52 2020

@author: Julien
"""

import numpy as np

import matplotlib.pyplot as plt

X = np.array([-3.0,-2.1,-1.9,-1.1,-0.9, 0.9, 1.1, 1.9, 2.1, 3.0])
Y = np.array([-1.0,-1.0, 1.0, 1.0,-2.0,-2.0, 2.0, 2.0, 0.0, 0.0])

def f(x,a,b,c):
    return(a*x**2+b*x+c)

def find(A,B,T,p):
    L1 = np.array([A[0]**2, A[0], 1])
    L2 = np.array([B[0]**2, B[0], 1])
    
    if p==0:
        L3 = np.array([2*A[0], 1, 0])
    elif p==1:
        L3 = np.array([2*B[0], 1, 0])
    
    M = np.array([L1,L2,L3])
    
    Coef = np.linalg.solve(M, [A[1], B[1], T])
    return Coef

XX = []
for i in range(len(X)-1):
    XX.append(np.linspace(X[i],X[i+1],100))
XX = np.array(XX)

TT = [find((X[0],Y[0]),(X[1],Y[1]),0,0)]
for i in range(1,len(X)-1):
    tan = X[i]*2*TT[i-1][0]+TT[i-1][1]
    TT.append(find((X[i],Y[i]),(X[i+1],Y[i+1]),tan,0))

fig, ax = plt.subplots(1,1)

for i in range(len(XX)):
    y = f(XX[i], TT[i][0], TT[i][1], TT[i][2])
    ax.plot(X[i],Y[i],'or', zorder=3)
    ax.plot(XX[i],y,c='C01')