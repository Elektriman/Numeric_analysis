# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:20:17 2020

@author: Julien
"""

import numpy as np
import matplotlib.pyplot as plt


def NewtonTab(f,df,x_init,e):
    X = [x_init]
    X.append(x_init-f(x_init)/df(x_init))
    while abs(X[-1]-X[-2])>=e and abs(f(X[-1]))>=e :
        X.append(X[-1]-f(X[-1])/df(X[-1]))
    return (X)

def f(x):
    return (x**2+2*x-5)

def df(x):
    return (2*x+2)

def getTan(f, df, X, x):
    b = -df(x)*x+f(x)
    Y = df(x)*X + b
    return Y

fig, ax = plt.subplots(1,1,figsize=(10,7))

def afficherNewton(f, df, R):
    #définition des valeurs en X et Y
    X = np.linspace(min(R)-1, max(R)+1, 1000)
    Y = f(X)
    
    ax.plot(X,Y, label='f(x)=x²+2x-5') #on trace la fonction
    
    for i in range(len(R)):#pour chaque point
        #on trace la tangente
        T = getTan(f, df, X, R[i])
        ax.plot(X,T,c='green', alpha=0.1)
        
        #on trace le trait vertical
        ax.plot([R[i],R[i]],[0,f(R[i])],c='lime', alpha=0.5)
        
        ax.plot(R[i],f(R[i]), '.r', zorder = 3)
        
        #on trace le trait suivant la tangente
        if i>0 :
            ax.plot([R[i-1],R[i]],[f(R[i-1]),0],c='green', alpha=0.5)
    
    ax.plot(R[-1],0,c='r', marker='o', zorder=3) #on marque la solution
    ax.set_ylim([min(Y), max(Y)]) #on limite l'affichage à cause des tangentes
    ax.grid(True, which='both') #grille
    ax.axhline(y=0, color='k') #axe des ordonnées
    ax.axvline(x=0, color='k') #axe des abscisses
    ax.legend()

R = NewtonTab(f, df, 0, 10**-3)

afficherNewton(f, df, R)