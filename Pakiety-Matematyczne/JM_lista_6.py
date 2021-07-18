# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:48:55 2020

@author: Jakub
"""

"""Lista 5"""

import sympy as sp
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

######
"""Zad. 1"""
######
print("==> Zadanie 1")

def bisekcja(f,a,b,d): # badanie funkcji f na przedziale [a,b] z dokładnoscia d
    f = sp.lambdify(x,f)
    while abs(a - b) > 0:
        c = (a + b)/2
        if abs(f(c)) <= d: # jesli f(c) to w przybliżeniu zero
            break
        elif f(a) * f(c) < 0:
            b = c
        elif f(b) * f(c) < 0:
            a = c
        else:
            return None
    return (a+b)/2

### Przykład
print('Przykład:')
 
x = sp.Symbol('x')
f = x**2 - 4
print('Pierwiastek f = x^2 - 4 znaleziony metodą bisekcji:', bisekcja(f,1,10,1e-10))

######
"""Zad. 2"""
######
print("\n==> Zadanie 2")

def Newton(f,x0,d): # rozpoczęcie szukania miejsca zerowego z dokładnoscią d od x0
    pochodna = sp.lambdify(x,f.diff(x))
    f_save = f
    f = sp.lambdify(x,f)
    k = 0
    while abs(f(x0))  > d:
        x0 = x0 - f(x0)/pochodna(x0)
        X = np.linspace(x0-3,x0+3)
        g = lambda x: pochodna(x0)*(x-x0)+f(x0) # wykres stycznej
        k += 1
        plt.plot(x0,f(x0),'ro')
        plt.plot(X,f(X))
        plt.plot(X,g(X))
        plt.grid(True)
        plt.title("Etap " + str(k) + " | " + str(f_save))
        plt.axhline(0, color="black")
        plt.show()  
    return x0

### Przykład
print('Przykład:')

x = sp.Symbol('x')
f = x**2 - 4
print('Pierwiastek f = x^2 - 4 znaleziony metodą Newtona:',Newton(f,5,1e-10))

######
"""Zad. 3"""
######
print("\n==> Zadanie 3")

x = sp.Symbol('x')
f = x - 2 - sp.log(x)
d = 1e-15
x0 = 30

solve_bisekcja = bisekcja(f,1,5,d)
solve_Newton = Newton(f,x0,d)

solve = fsolve(sp.lambdify(x,f),1)

# Porównanie metody bisekcji z wbudowaną fsolve:
diff_1 = abs(solve[0] - solve_bisekcja)
print("Różnica między rozwiązaniem znalezionym metodą bisekcji a rozwiązaniem z wbudowanej funkcji:\n",diff_1)

# Porównanie metody Newtona z wbudowaną fsolve:
diff_2 = abs(solve[0] - solve_Newton)
print("Różnica między rozwiązaniem znalezionym metodą Newtona a rozwiązaniem z wbudowanej funkcji:\n",diff_2)

print("\nCzy metoda Newtona bliższa wynikowi niż metoda bisekcji?",diff_2 < diff_1)

######
"""Zad. 4"""
######
print("\n==> Zadanie 4")

def bisekcja_list(f,a,b,d): # Wykonanie listy składającej się z kolejnych przybliżeń miejsca zerowego
    f = sp.lambdify(x,f)
    L = []
    while abs(a - b) > 0:
        c = (a + b)/2
        L.append(c)
        if abs(f(c)) <= d:
            break
        elif f(a) * f(c) < 0:
            b = c
        elif f(b) * f(c) < 0:
            a = c
        else:
            return None
    return L

def Newton_list(f,x0,d): # Wykonanie listy składającej się z kolejnych przybliżeń miejsca zerowego
    pochodna = sp.lambdify(x,f.diff(x))
    f = sp.lambdify(x,f)
    L = []
    while abs(f(x0))  > d:
        x0 = x0 - f(x0)/pochodna(x0)
        L.append(x0)
    return L

f = x - 2 - sp.log(x)
d = 1e-10

### Graficzne wyznaczanie rzędu metody bisekcji p_1

bis_L = bisekcja_list(f,1,50,d)

p_1 = np.log(abs(bis_L[len(bis_L)-1]-solve))/np.log(abs(bis_L[len(bis_L)-2]-solve))
x1n_1 = bis_L[len(bis_L)-1]
x1n = bis_L[len(bis_L)-2]
C_1 = abs((x1n_1-solve))/(abs((x1n-solve)))**p_1

print(p_1[0],"--> rząd metody bisekcji to około 1, stała C:",C_1[0])

### Graficzne wyznaczanie rzędu metody Newtona p_2

New_L = Newton_list(f,30,d)

p_2 = np.log(abs(New_L[len(New_L)-1]-solve))/np.log(abs(New_L[len(New_L)-2]-solve))
x2n_1 = New_L[len(New_L)-1]
x2n = New_L[len(New_L)-2]
C_2 = abs((x2n_1-solve))/(abs((x2n-solve)))**p_2

print(p_2[0],"--> rząd metody Newtona to około 2, stała C:",C_2[0])




