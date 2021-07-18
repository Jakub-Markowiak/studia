# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:30:00 2020

@author: Jakub
"""

"""Lista 5"""

import numpy as np
import math

######
"""Zad. 1"""
######
print("==> Zadanie 1")

"""a. """
print("=====> a.")

A = np.zeros((4,5))
print(A)

"""b. """
print("=====> b.")

B = np.identity(11)
print(B)

"""c. """
print("=====> c.")

C = np.random.rand(5,4)
print(C)

######
"""Zad. 2"""
######
print("==> Zadanie 2")  # W obu podpunktach niemożliwe jest podniesienie macierzy B do kwadratu, gdyż nie są to macierze kwadratowe.

def det(X):
    det_X = np.linalg.det(X)
    if math.isclose(det_X,0,abs_tol=1e-15) == True: ### przybliżenie do 10^(-15)
        return 0
    else:
        return det_X
def inverse(X):
    if det(X) == 0:
        return None
    else:
        return np.linalg.inv(X)
def check_matrix(X):
    if det(X) == 0:
        return print("Wyznacznik macierzy\n",X,"\njest równy " + str(det(X)) + ", zatem nie istnieje macierz do niej odwrotna.","\n")
    else:
        return print("Wyznacznik macierzy\n",X,"\njest równy " + str(det(X)) + ", a jej macierz odwrotna to\n",inverse(X),'\n')


"""a. """
print("=====> a.")  # W podpunkcie a. jedynym istniejącym iloczynem jest Bx(A^2).
 
A = np.array([[0, -1, 1],
             [3, 2, 2],
             [1 ,0, -2]])

B = np.array([[0,1,7],
             [1,2,-2]])

print("BxA^2 =\n", B@(A@A),'\n')
check_matrix(A) # Sprawdzanie, czy istnieje macierz odwrotna do A.

"""b. """
print("=====> b.") # W podpunkcie b. jedynym istniejącym iloczynem jest (A^2)xB.

A = np.array([[3, 2, 2],
             [0,-1, 1],
             [1 ,0, -2]])

B = np.array([[1,0],
             [2,1],
             [-2,7]])

print('A^2xB =\n',(A@A)@B,'\n')
check_matrix(A) # Sprawdzanie, czy istnieje macierz odwrotna do A.

######
"""Zad. 3"""
######
print("==> Zadanie 3")


k = 100

V = np.random.randint(1,7,size=k) # wektor wygenerowany z k wyników rzutu kostką

V_list = V.tolist() # przekonwertowanie wektora do listy, aby użyć funkcji 'count' i policzyć elementy
print("Wylosowano:\n",
      V_list.count(1), "jedynek\n",
      V_list.count(2), "dwójek\n",
      V_list.count(3), "trójek\n",
      V_list.count(4), "czwórek\n",
      V_list.count(5), "piątek\n",
      V_list.count(6), "szóstek\n")

######
"""Zad. 4"""
######
print("==> Zadanie 4")

# 1 - wylosowano orła, 0 - wylosowano reszkę

"""a. """
print("=====> a.")
k = 100 # liczba rzutów w jednym eksperymencie

V_k = np.random.randint(0,2,size=k) # wektor wygenerowany z k (100) wyników rzutu monetą
print("Wypadło",sum(V_k),"orłów w",k,"próbach.")

"""b. """
print("=====> b.")
n = 150 # liczba wykonanych eksperymentów
V_nk = np.random.randint(0,2,size=(n,k)) # tablica wygenerowana z n (150) wektorów wygenerowanych z k (100) wyników rzutu monetą

def sprawdz_sekwencje(V):  
    sekwencja_orlow = "1, 1, 1, 1, 1"
    liczba_sekwencji = repr(V).count(sekwencja_orlow)   # liczy ile razy występuje 'sekwencja orlow' w V
    if liczba_sekwencji > 0:
        return 1 # "sukces"
    else:
        return 0 # "porażka"
    
s = 0
for i in range(len(V_nk)):
    s += sprawdz_sekwencje(V_nk[i])

liczba_sukcesow = s # sukces = wypada 5 lub więcej orłów z rzędu (gdy wypada pięć to przerywam eksperyment i uznaję tę próbę za "sukces")
liczba_wszystkich_zdarzen = n

p = liczba_sukcesow/liczba_wszystkich_zdarzen

print("Prawdopodobieństwo wypadnięcia 5 orłów z rzędu w próbie",k,"rzutów monetą wynosi",p)

"""c. """
print("=====> c.")
L = list(map(sprawdz_sekwencje, V_nk))

liczba_sukcesow = sum(L)
liczba_wszystkich_zdarzen = n

p = liczba_sukcesow/liczba_wszystkich_zdarzen

print("Prawdopodobieństwo wypadnięcia 5 orłów z rzędu w próbie",k,"rzutów monetą wynosi",p)

######

