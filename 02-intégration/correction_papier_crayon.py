# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:32:59 2020

@author: Julien
"""


import numpy as np
import numpy.random

import matplotlib.pyplot as plt
from scipy.integrate import quad

import time
import random
import math

f = lambda x : x**2 -x -1

def rect(f,a,b,n):
    pas = (b-a)/n
    S = 0
    i=a
    while i<b :
        S+=pas*f(i)
        i+=pas
    return S

print(quad(f, 0, 4)[0])
print(rect(f, 0, 4, 4))