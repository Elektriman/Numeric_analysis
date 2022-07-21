# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:26:53 2020

@author: Julien
"""


import numpy as np
import matplotlib.pyplot as plt

def l(x):
    return 1.5*x*(1 - x)

#fonction qui renvoie une troncature de nb à n chiffres après la virgule
def getDec(nb, n):
    s = str(nb)
    i=0
    while i<len(s) and s[i]!="." :
        i+=1
    i = min(len(s), i+n)
    return float(s[:i])

#méthode du point fixe de manière récursive
def pointFixeRec(f, x0, i=0):
    if i>1000 :
        print("la méthode a échoué")
        return None
    else :
        if f(x0)!=x0 :
            return pointFixe(f, f(x0), i+1)
        else :
            return x0

def pointFixe(f, x0, e):
    X=[x0, f(x0)]
    while len(X)<1000 and getDec(X[-2], e)!= getDec(X[-1], e) :
        X.append(f(X[-1]))
    return X

def afficherPF(f, x0, e):
    X = pointFixe(f,x0,e)
    print(X[-1])
    XX = np.linspace(0,1,1000)
    YY = f(XX)
    plt.plot(XX,YY, c='C00', label='f(x)=(3/2) x(1-x)')
    plt.plot(XX,XX, c='C01', label='x=y')
    plt.axvline(x=0, c='k')
    plt.axhline(y=0, c='k')
    plt.grid(True)
    plt.legend()
    
    for i in range(len(X)-2):
        plt.plot([X[i],X[i+1]],[X[i+1], X[i+1]], c='g')
        plt.plot([X[i+1],X[i+1]],[X[i+1],X[i+2]], c='g')
    plt.show()

fig, ax = plt.subplots(1,1)
afficherPF(l, 0.2, 10)