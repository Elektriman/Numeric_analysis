# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:37:01 2020

@author: Julien
"""

import numpy as np
import matplotlib.pyplot as plt
from  scipy.integrate import quad
import random
import math

# Variables globales
N = 10
Ampli = [random.randint(1,N) for i in range(N)]
Freq = [random.randint(1,N) for i in range(N)]
print(Ampli)
print(Freq)

def f(x):
    S=0
    for i in range(len(Ampli)):
        S+=Ampli[i]*np.sin(Freq[i]*x)
    return S

def signal_bruit(x):
    S=0
    for i in range(len(Ampli)):
        S+=Ampli[i]*np.sin(Freq[i]*x)+2*random.random()-1
    return S

X = np.linspace(0,2*math.pi,400)
plt.plot(X,[signal_bruit(x) for x in X], label='signal brut')

def getAmpli(f,freq):
    return (1/np.pi)*quad(lambda x:f(x)*np.sin(freq*x),0,2*np.pi)[0]

F = np.unique(np.array(Freq))

'''
filtrage proche de l'original
'''
A = np.zeros(F.shape)
for i in range(len(F)):
    A[i] = getAmpli(f,F[i])

def signal_filtre(x):
    S=0
    for i in range(len(A)):
        S+=A[i]*np.sin(F[i]*x)
    return S

plt.plot(X,signal_filtre(X), zorder=3, alpha=0.9, label='signal filtré (ttes les freq)')

'''
filtrage coupant les fréquences inférieures à N/2
'''

F = F[F<N/2]

A = np.zeros(F.shape)
for i in range(len(F)):
    A[i] = getAmpli(f,F[i])

def signal_filtre(x):
    S=0
    for i in range(len(A)):
        S+=A[i]*np.sin(F[i]*x)
    return S

plt.plot(X,signal_filtre(X), zorder=3, alpha=0.7, label='signal filtré (freq<N/2)')


plt.legend()