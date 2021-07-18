# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 12:15:02 2020

@author: Jakub
"""
from matplotlib.pyplot import figure
import numpy as np
from scipy.special import factorial
from scipy import linalg
import math

"""
LISTA 1
"""


"""Zad.1"""

X=[]
for k in range(4,11):
    X.append(10**k)

f_1 = lambda a: a - (1+a**2)**(1/2)
f_2 = lambda a: (-1)/(a+(1+a**2)**(1/2))

F_1 = []
F_2 = []
R = []
for k in X:
    F_1.append(f_1(k))
    F_2.append(f_2(k))
    R.append(f_1(k)-f_2(k)) 
#zbiór zawierający różnice między wynikami otrzymanymi na dwa różne sposoby dla kolejnych x
    
#Wykres przedstawiający różnice między otrzymanymi wynikami dla kolejnych x
graph_1 = figure().gca()
graph_1.legend
graph_1.plot(X,R,"bo")
graph_1.set_title("Różnice między otrzymanymi wynikami dla kolejnych x",size=10)
graph_1.set_xlabel("$x$")
graph_1.set_ylabel("$f_1(x)-f_2(x)$")

"""Zad.2"""
g_1 = lambda x: (x-1)**4
g_2 = lambda x: x**4 - 4*x**3 + 6*x**2 - 4*x + 1

x = np.linspace(1-10**(-3),1+10**(-3))
yg_1 = g_1(x)
yg_2 = g_2(x)
graph_2 = figure().gca()
graph_2.plot(x,yg_1,"-b", label="$g_1(x) = (x-1)^4$")
graph_2.plot(x,yg_2,"-r", label="$g_2(x) = x^4-4x^3+6x^2-4x+1$")
graph_2.set_title("Wyniki otrzymane dwiema różnymi metodami",size=10)
graph_2.set_xlabel("$x$")
graph_2.set_ylabel("$y$")
graph_2.legend()

"""Zad.3"""
x = np.linspace(-100,100)
def en(x,N):
    S = 0
    for k in range(0,N+1):
        S += x**k/(factorial(k,exact=False))
    return S

graph_3_a = figure().gca()
graph_3_a.plot(x,en(x,100),'-b',linewidth=2, label='$e_{N}(x)=\sum_{k=0}^{100} {x^k}/{k!}$')
graph_3_a.plot(x,np.e**x,'r', label="$f(x) = e^x$")
graph_3_a.set_title("Porównanie funkcji $f(x)$ i $e_{N}(x)$",size=10)
graph_3_a.set_xlabel("$x$")
graph_3_a.set_ylabel("$y$")
graph_3_a.legend()

x = np.arange(-100,100)
graph_3_b = figure().gca()
graph_3_b.plot(x,en(x,1000),'-b',linewidth=2, label='$e_{N}(x)=\sum_{k=0}^{1000} {x^k}/{k!}$')
graph_3_b.plot(x,np.e**x,'r', label="$f(x) = e^x$")
graph_3_b.set_title("Porównanie funkcji $f(x)$ i $e_{N}(x)$",size=10)
graph_3_b.set_xlabel("$x$")
graph_3_b.set_ylabel("$y$")
graph_3_b.legend()

"""Zad.4"""
# Oblicz wyznacznik i znajdź macierz odwrotną do macierzy A i B.
print("==> Zadanie 4")
def det(X):
    det_X = linalg.det(X)
    if math.isclose(det_X,0,abs_tol=1e-15) == True: ### przybliżenie do 10^(-15)
        return 0
    else:
        return det_X
def inverse(X):
    if det(X) == 0:
        return None
    else:
        return linalg.inv(X)
def check_matrix(X):
    if det(X) == 0:
        return print("Wyznacznik macierzy\n",X,"\njest równy " + str(det(X)) + ", zatem nie istnieje macierz do niej odwrotna.","\n")
    else:
        return print("Wyznacznik macierzy\n",X,"\njest równy " + str(det(X)) + ", a jej macierz odwrotna to\n",inverse(X),"\n")

A = np.array([[1.,1.,2.,1.],
              [0.,1.,4.,3.],
              [4.,6.,8.,6.],
              [5.,5.,-5.,5.]])
B = np.array([[2,1,1,2],
              [1,2,1,2],
              [2,1,2,1],
              [2,2,2,2]])

check_matrix(A)
check_matrix(B)

"""Zad.5"""
print("==> Zadanie 5")
#Rozwiąż układy równań liniowych.
def check_solutions(X,S): # X - macierz, S - macierz rozwiązań
    c = 0 #columns
    r = 0 #rows
    for m in X:
        r += 1
    for n in X[0]:
        c += 1
   # print("Columns:",c,"Rows:",r)
    X_extended = np.insert(M, c, values=S,axis=1)
    rank_X = np.linalg.matrix_rank(X)
    rank_X_extended = np.linalg.matrix_rank(X_extended)
   # rank_X - rząd macierzy głównej
   # rank_X_extended - rząd macierzy rozszerzonej
   # c - liczba kolumn/niewiadomych
   
    if rank_X == rank_X_extended:
        if rank_X == c:
            print("Jedno rozwiązanie.")
            return np.linalg.solve(X,S)
        else:
            print("Nieskończenie wiele rozwiązań.")
            return None
    else:
        print("Brak rozwiązań.")
        return None
    
#---> a.
print("----> a.")
M = np.array([[2,1,1],
              [1,-1,-2],
              [1,1,3]])
### X = [x,
###      y,
###      z]

S = ([1,
      3,
      10])

### MX = S => X = M^(-1)S
X = check_solutions(M,S)
print("Rozwiązaniem pierwszego układu równań jest",X,".\n")
        
#---> b.
print("----> b.")
M = np.array([[1,1,1],
              [1,3,2],
              [2,5,6],
              [4,2,1],
              [1,6,-5]])

S = np.array([0,
              1,
              3,
              4,
              1])

X = check_solutions(M,S)
print("Rozwiązaniem drugiego układu równań jest",X,".\n\n\n")