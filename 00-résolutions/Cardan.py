# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:57:13 2020

@author: Julien
"""

import numpy as np
import matplotlib.pyplot as plt
import cmath

def Cardan(C):
    #equation of form ax**3 + bx**2 + cx + d = 0

    a,b,c,d = C[0],C[1],C[2],C[3]
    
    deviation = -b/(3*a) #x coordinate of the inflexion point
    #we deviate the equation to put the inflexion point on the y axis so that we cat get rid of the x**2 term
    
    #parameters of the reduced equation x**3 + px + q = 0
    p = (3*a*c-b**2)/(3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*d*a**2)/(27*a**3)
    
    delta = ((q/2)**2) + ((p/3)**3) #3rd degree equation discriminant
    
    if p==0 and q==0 : #exeption when p and q are null
        return [0]
    
    if delta > 0 : #positive discriminant, one real solution
        R = []
        r = 0.0
        for i in range(3): #computation of the three real solutions obtained from the three conjugate cube roots of the discriminant
            
            #angle of the solution
            l = ((3*q)/(2*p))*(3/-p)**0.5
            theta = (1/3)*np.arccos(l)
            
            R.append(2*((-p/3)**0.5)*np.cos(theta + i*2*np.pi/3)+deviation)
            
            if R[-1].imag < 10**-10 :
                r = -R[-1].real+deviation
        
        print(R, deviation)
        return [r]
    
    elif delta == 0 : #null discriminant, two real solutions
        r0 = (3*q)/p
        r1 = -(3*q)/(2*p)
        
        return [r0+deviation,r1+deviation]
    
    else : #negative discriminant, three real solutions
        R = []
        for i in range(3): #computation of the three real solutions obtained from the three conjugate cube roots of the discriminant
            
            #angle of the solution
            l = ((3*q)/(2*p))*np.sqrt(3/-p)
            theta = (1/3)*np.arccos(l)
            
            R.append(2*np.sqrt(-p/3)*np.cos(theta + i*2*np.pi/3)+deviation)
        
        return R

fig,ax = plt.subplots(1,1)

C = [3,2,7,4]
def f(C,x):
    return(C[0]*x**3 + C[1]*x**2 + C[2]*x + C[3])

deviation = -C[1]/(3*C[0])
R = Cardan(C)
X = np.linspace(deviation-1,deviation+1,1000)
Y = f(C,X)
print(R)

ax.plot(X,Y, zorder=1)
ax.axhline(y=0, c='k', zorder=0)
ax.axvline(x=0, c='k', zorder=0)
ax.scatter(R,np.zeros(len(R)), c='r', zorder=2)
ax.grid(True)
plt.show()
































