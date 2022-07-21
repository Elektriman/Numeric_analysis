# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 19:28:47 2020

@author: Julien
"""
import numpy as np

import matplotlib.pyplot as plt

A = np.array([-1,-3])
B = np.array([ 1, 4])
C = np.array([ 3,-1])

"""
On cherche deux paraboles :
+ La première passe par A et B
+ La seconde par B et C
+ Les tangentes des paraboles en B sont identiques.

!!! A compléter en CM !!!
"""

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

T = 1

T1 = find(A,B,T,1)
T2 = find(B,C,T,0)

tan = lambda x : T*x + B[1]-T*B[0]

x1 = np.linspace(-2,B[0],100)
x2 = np.linspace(B[0],4,100)
y1 = f(x1, T1[0], T1[1], T1[2])
y2 = f(x2, T2[0], T2[1], T2[2])


plt.scatter([A[0],B[0],C[0]],[A[1],B[1],C[1]],s = 200, marker = 's', color = [[0.7,0.0,0.4]])
plt.annotate("A", (A[0]+0.2,A[1]+0.1))
plt.annotate("B", (B[0]+0.2,B[1]+0.1))
plt.annotate("C", (C[0]+0.2,C[1]+0.1))
plt.plot(x1, y1, label="première parabole")
plt.plot(x2, y2, label="deuxième parabole")
plt.plot(np.hstack([x1,x2]),tan(np.hstack([x1,x2])), c='gray', alpha = 0.3, label='tangente commune')

plt.ylim((-12,6))
plt.legend()

plt.show()