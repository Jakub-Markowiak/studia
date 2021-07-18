# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 11:25:12 2020

@author: Jakub
"""

import numpy as np
import matplotlib.pyplot as plt

######
"""Zad. 1"""
######
"""a. """
print("\n\nZadanie 1.")

t = 200
p = 0.
    
def bladzenie_losowe_2(t=200,p=0.5,start=0):
    Y = [start]             # zdefiniowanie tablicy Y, do której będą dopisywane kolejne wartosci
    def rekurencja_2(t):
        if len(Y) < t:
            random = np.random.choice(2,p=[p,1-p])
            if random == 1:
                Y.append(Y[len(Y)-1] + 1)
                return rekurencja_2(t)
            else:
                Y.append(Y[len(Y)-1] - 1)
                return rekurencja_2(t)
        else:
            return Y
    return rekurencja_2(t)

Y_1 = bladzenie_losowe_2(t,p)
X_1 = list(range(1,t+1))

plt.plot(X_1, Y_1, "bo", markersize=3)
plt.grid(True)
plt.title("Jednowymiarowe błądzenie losowe")
plt.xlabel("$t$")
plt.ylabel("$X$")
plt.axhline(0, color="black")
plt.show()

"""b., c."""

def prawdopodobienstwo_2(Y, z):
    if z == 0:
        return (1,1)
    else:
        def filtruj(element):
            return element == 0 or element == z
        Y_filtered = list(filter(filtruj,Y))
        liczba_wszystkich_zdarzen = Y_filtered.count(z)
        Y_filtered.reverse()
        if Y.count(0) == 0:
            return (0,0)
        else:
            index = Y_filtered.index(0)
            liczba_sprzyjajacych_zdarzen = Y_filtered[index:].count(z) 
        
        return (liczba_sprzyjajacych_zdarzen,liczba_wszystkich_zdarzen)

def rekurencja_2(z, t, s=0, w=0, n=0): ### z <- obliczamy prawdopodobieństwo, że wróci z z-tej pozycji na pozycję zerową, s <- liczba sprzyjających zdarzeń, w <- liczba wszystkich zdarzeń
    if n < t:
        n += 1
        (S,W) = prawdopodobienstwo_2(bladzenie_losowe_2(t,p),z)
        s += S
        w += W
        return rekurencja_2(z, t, s, w, n)
    else:
        if w != 0 and s != 0:
            return s/w
        else:
            return "Za mało prób, aby okreslić prawdopodobieństwo"
        
k = 100 # liczba prób  
print('"Prawdopodobieństwo", że trajektoria wróci z punktu',Y_1[t-1],'do punktu 0 wynosi:',rekurencja_2(Y_1[t-1],k),'.')


######
"""Zad. 2"""
######
print("\n\nZadanie 2.")
"""a. """

t = 200

def bladzenie_losowe_4(t=200,poczatek=(0+0j)):
    P = np.random.randint(4, size=t)
    start = P[0]
    if poczatek == (0+0j):
        if start == 0:
            Y = [0+1j]
        elif start == 1:
            Y = [0-1j]
        elif start == 2:
            Y = [-1+0j]
        elif start == 3:
            Y = [1+0j]
    else:
        Y = [poczatek]
    def rekurencja_4(P):
        if len(Y) < len(P):
            if P[len(Y)-1] == 3:
                Y.append(Y[len(Y)-1] + (1+0j))
                return rekurencja_4(P)
            if P[len(Y)-1] == 2:
                Y.append(Y[len(Y)-1] + (-1+0j))
                return rekurencja_4(P)
            if P[len(Y)-1] == 1:
                Y.append(Y[len(Y)-1] + (0-1j))
                return rekurencja_4(P)
            if P[len(Y)-1] == 0:
                Y.append(Y[len(Y)-1] + (0+1j))
                return rekurencja_4(P)
        else:
            return Y
    return rekurencja_4(P)

B = bladzenie_losowe_4(t)
X_2 = np.real(B)
Y_2 = np.imag(B)

plt.plot(X_2, Y_2, "bo", markersize=2, linestyle="--", linewidth="1")
plt.plot(X_2[t-1],Y_2[t-1], "ro")
plt.grid(True)
plt.title("Dwuuwymiarowe błądzenie losowe")
plt.xlabel("$X$")
plt.ylabel("$Y$")
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.show()

"""b., c."""


def prawdopodobienstwo_4(B, z):
    if z == 0+0j:
        return (1,1)
    else:
        def filtruj(element):
            return element == 0+0j or element == z
        B_filtered = list(filter(filtruj,B))
        liczba_wszystkich_zdarzen = B_filtered.count(z)
        B_filtered.reverse()
        if B.count(0) == 0:
            return (0,0)
        else:
            index = B_filtered.index(0)
            liczba_sprzyjajacych_zdarzen = B_filtered[index:].count(z) 
        
        return (liczba_sprzyjajacych_zdarzen,liczba_wszystkich_zdarzen)

def rekurencja_4(z, t, s=0, w=0, n=0): ### z <- obliczamy prawdopodobieństwo, że wróci z z-tej pozycji na pozycję zerową, s <- liczba sprzyjających zdarzeń, w <- liczba wszystkich zdarzeń
    if n < t:
        n += 1
        (S,W) = prawdopodobienstwo_4(bladzenie_losowe_4(t),z)
        s += S
        w += W
        return rekurencja_4(z, t, s, w, n)
    else:
        if w != 0 and s != 0:
            return s/w
        else:
            return "Za mało prób, aby okreslić prawdopodobieństwo"
        
k = 100 # liczba prób        
print('(Dla k=100) "Prawdopodobieństwo", że trajektoria wróci z punktu',(X_2[t-1],Y_2[t-1]),'do punktu (0,0) wynosi:',rekurencja_4(B[t-1],k),'.')


k = 1000 # liczba prób    
print('(Dla k=1000) "Prawdopodobieństwo", że trajektoria wróci z punktu',(X_2[t-1],Y_2[t-1]),'do punktu (0,0) wynosi:',rekurencja_4(B[t-1],k),'.')