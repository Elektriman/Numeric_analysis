# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 19:52:50 2020

@author: Julien
"""

import numpy as np
import random
import matplotlib.pyplot as plt

def tabCoins():
    zone1 = [6,7,3,4]
    zone2 = [7,8,4,5]
    zone3 = [3,4,0,1]
    zone4 = [4,5,1,2]
    return np.array([zone1,zone2,zone3,zone4])

def getZone(x,y):
    if y>1 :
        if x<1 :
            return 0
        else :
            return 1
    else :
        if x<1 :
            return 2
        else :
            return 3

def createFunc(coins, X, Y):
    res = []
    for col in "RGB":
        M = np.zeros((4,4))
        N = np.zeros(4)
        for i in range(len(coins)):
            M[i] = [1,X[coins[i]],Y[coins[i]],X[coins[i]]*Y[coins[i]]]
            if col == "R":
                N[i] = R[coins[i]]
            elif col == "G":
                N[i] = G[coins[i]]
            elif col == "B":
                N[i] = B[coins[i]]

        Coef=np.linalg.solve(M, N)
        res.append(lambda x,y : Coef[0] + Coef[1]*x + Coef[2]*y + Coef[3]*x*y)

    return(np.array(res))

def addPoint(X,Y):
    x = 2*random.random()
    y = 2*random.random()
    size = random.random()*100
    coins = tabCoins()[getZone(x,y)]
    r,g,b = createFunc(coins,X,Y)
    couleur = [r(x,y), g(x,y), b(x,y)]
    plt.scatter(x,y,size,color=couleur)

X = np.array([0,1,2,0,1,2,0,1,2])
Y = np.array([0,0,0,1,1,1,2,2,2])
R = np.array([0,0,0,0.5,0.5,0.5,1,1,1])
G = np.array([0,0.5,1,0,0.5,1,0,0.5,1])
B = np.array([0,0.25,0.5,0.25,0.5,0.75,0.5,0.75,1])

for i in range(9):
    plt.scatter(X[i],Y[i],200,[[R[i],G[i],B[i]]])

plt.title('interpolation de couleur')
for i in range(70):
    addPoint(X,Y)