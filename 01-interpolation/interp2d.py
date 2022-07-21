# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 19:45:19 2020

@author: Julien
"""

import numpy as np

import matplotlib.pyplot as plt


def droite(A,B):
    a = (B[1]-A[1])/(B[0]-A[0])
    b = A[1]-a*A[0]
    return (lambda x:a*x+b)

def parabole(A,B,C):
    L1 = np.array([A[0]**2, A[0], 1])
    L2 = np.array([B[0]**2, B[0], 1])
    L3 = np.array([C[0]**2, C[0], 1])
    
    M = np.array([L1,L2,L3])
    
    Coef = np.linalg.solve(M, [A[1], B[1], C[1]])
    
    return (lambda x: Coef[0]*x**2 + Coef[1]*x + Coef[2])

def cubique(A, B, Ta, Tb):
    L1 = np.array([A[0]**3, A[0]**2, A[0], 1])
    L2 = np.array([B[0]**3, B[0]**2, B[0], 1])
    L3 = np.array([3*A[0]**2, 2*A[0], 1, 0])
    L4 = np.array([3*B[0]**2, 2*B[0], 1, 0])
    
    M = np.array([L1,L2,L3,L4])
    
    Coef = np.linalg.solve(M, [A[1], B[1], Ta, Tb])
    
    return (lambda x: Coef[0]*x**3 + Coef[1]*x**2 + Coef[2]*x + Coef[3])

fig, ax = plt.subplots(1,1, figsize=(20,10))

D1 = np.array([[-9,-1],[-6,-8]])
D2 = np.array([[2,9],[7,8]])
D3 = np.array([[7,8],[10,-1]])
D = np.array([D1,D2,D3])
plt.axis('equal')

for i in range(len(D)):
    X = np.linspace(D[i,0,0],D[i,-1,0],1000)
    f = droite(D[i,0],D[i,1])
    ax.plot(X,f(X), c='C01')
    ax.scatter(D[i,:,0],D[i,:,1], c='C01', zorder=3)

P1 = np.array([[-13,3],[-11,0],[-8,2]])
P2 = np.array([[-13,-3],[-5,-8],[0,-9]])
P3 = np.array([[0,-9],[7,-8],[15,-3]])
P4 = np.array([[9,2],[13,0],[15,-3]])
P = np.array([P1,P2,P3,P4])

for i in range(len(P)):
    X = np.linspace(P[i,0,0],P[i,-1,0],1000)
    f = parabole(P[i,0],P[i,1], P[i,2])
    ax.plot(X,f(X), c='C02')
    ax.scatter(P[i,:,0],P[i,:,1], c='C02', zorder=3)

C1 = np.array([[-6,8,0],[-2,7,-1]])
C2 = np.array([[-2,7,0],[2,9,2]])
C3 = np.array([[-8,2,-0.5],[0,0,0]])
C4 = np.array([[0,0,0],[9,2,0.5]])
C5 = np.array([[-9,-1,-0.5],[0,-3,0]])
C6 = np.array([[0,-3,0],[10,-1,0.5]])
C = np.array([C1,C2,C3,C4,C5,C6])

for i in range(len(C)):
    X = np.linspace(C[i,0,0],C[i,-1,0],1000)
    f = cubique(C[i,0],C[i,1],C[i,0,2],C[i,1,2])
    ax.plot(X,f(X), c='C03')
    ax.scatter(C[i,:,0],C[i,:,1], c='C03', zorder=3)