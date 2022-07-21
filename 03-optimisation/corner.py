# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 11:04:09 2020

@author: Julien
"""


import matplotlib.pyplot as plt

from scipy.optimize import linprog

import numpy as np

C = [-1,4]
A = [[-3,-1],[2,-3],[3,4]]
B = [-29,9,35]
x = (0,None)
y = (0,None)

# Recherche du minimum
res = linprog(C,A,B,bounds=(x,y),method='Simplex')['x']
print(res)
plt.plot(res[0],res[1],'ok')

plt.xlim(res[0]-5,res[0]+10) # Limites des abscisses de la fenêtre graphique
plt.ylim(res[1]-5,res[1]+5) # Limites des ordonnées de la fenêtre graphique

X = np.linspace(res[0]-5 , res[0]+10, 1000)

# 2𝑦 ≤ 𝑥 + 5
a,b,c = A[0][0],A[0][1],B[0]
I1 = lambda x : (c-a*x)/b
y1 = I1(X)
# Usage de la fonction fill pour "remplir" le quadrilatère
# Usage du paramètre alpha pour la transparence
plt.fill_between(X, y1, np.full(len(X),res[1]-5), color='r',alpha=0.2)

# 𝑥 + 𝑦 ≤ 13
a,b,c = A[1][0],A[1][1],B[1]
I2 = lambda x : (c-a*x)/b
y2 = I2(X)
# Usage de la fonction fill pour "remplir" le quadrilatère
# Usage du paramètre alpha pour la transparence
plt.fill_between(X, y2, np.full(len(X),res[1]-5), color='g',alpha=0.2)

# 𝑥 + 4𝑦 ≥ 19
a,b,c = A[2][0],A[2][1],B[2]
I3 = lambda x : (c-a*x)/b
y3 = I3(X)
# Usage de la fonction fill pour "remplir" le quadrilatère
# Usage du paramètre alpha pour la transparence
plt.fill_between(X, y3, np.full(len(X),res[1]-5), color='b',alpha=0.2)

plt.show()