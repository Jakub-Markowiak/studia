# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:14:28 2020

@author: Jakub
"""

import matplotlib.pyplot as plt
import numpy as np

##############
""" Zad 1. """
##############
x = np.linspace(-np.pi,np.pi)

@np.vectorize
def tg(x):
    if abs(x/(np.pi/2)) - abs(int(x/(np.pi/2))) < 1e-2:
        return None
    else:
        return np.sin(x)/np.cos(x)

@np.vectorize
def ctg(x):
    if abs(x/(np.pi)) - abs(int(x/(np.pi))) < 1e-2:
        return None
    else:
        return np.cos(x)/np.sin(x)
    
x = np.linspace(-np.pi,np.pi,1000)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = tg(x)
y4 = ctg(x)

plt.style.use('grayscale')

plt.subplot(221) # wykres sin(x)
plt.plot(x, y1, label='sin(x)')
plt.ylim(-1.3,1.3)
plt.grid(True,alpha=0.3)
plt.axhline(0, color='black',alpha=0.4)
plt.axvline(0, color='black',alpha=0.4)
plt.title("$y = \\sin(x)$")
plt.xlabel('x')
plt.ylabel('y')
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],\
           ['$-\\pi$','$-\\frac{\pi}{2}$','$0$','$\\frac{\pi}{2}$','$\\pi$'])
    
plt.subplot(222) # wykres cos(x)
plt.plot(x, y2, label='$cos(x)$',linewidth=1.3)
plt.ylim(-1.3,1.3)
plt.grid(True,alpha=0.3)
plt.axhline(0, color='black',alpha=0.4)
plt.axvline(0, color='black',alpha=0.4)
plt.title("$y = \\cos(x)$")
plt.xlabel('x')
plt.ylabel('y')
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],\
           ['$-\\pi$','$-\\frac{\pi}{2}$','$0$','$\\frac{\pi}{2}$','$\\pi$'])


plt.subplot(223) # wykres tg(x)
plt.plot(x, y3, label='tg(x)')
plt.ylim(-3,3)
plt.grid(True,alpha=0.3)
plt.axhline(0, color='black',alpha=0.4)
plt.axvline(0, color='black',alpha=0.4)
plt.axvline(-np.pi/2, color='black',alpha=0.8, linestyle="--")
plt.axvline(np.pi/2, color='black',alpha=0.8, linestyle="--")
plt.title("$y = \\tan(x)$")
plt.xlabel('x')
plt.ylabel('y')
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],\
           ['$-\\pi$','$-\\frac{\pi}{2}$','$0$','$\\frac{\pi}{2}$','$\\pi$'])

    
plt.subplot(224) # wykres ctg(x)
plt.plot(x, y4, label='ctg(x)')
plt.ylim(-3,3)
plt.grid(True,alpha=0.3)
plt.axhline(0, color='black',alpha=0.4)
plt.axvline(0, color='black',alpha=0.4)
plt.axvline(0, color='black',alpha=0.8, linestyle="--")
plt.axvline(-np.pi, color='black',alpha=0.8, linestyle="--")
plt.axvline(np.pi, color='black',alpha=0.8, linestyle="--")
plt.title("$y = \\cot(x)$")
plt.xlabel('x')
plt.ylabel('y')
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],\
           ['$-\\pi$','$-\\frac{\pi}{2}$','$0$','$\\frac{\pi}{2}$','$\\pi$'])

plt.suptitle("Wykresy funkcji trygonometrycznych",fontsize=17)
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.84, wspace=0.35, hspace=0.8)

plt.savefig('trigonometric_functions.png', dpi=600, quality=100, bbox_inches="tight")
plt.show()


##############
""" Zad. 2 """
##############
print("===> Zadanie 2\n")
x = np.linspace(-np.pi,np.pi,10000)
y1 = np.sin(3*x)
y2 = np.cos(-2*x)

plt.plot(x,y1, '-g', label="$\\sin(3x)$")
plt.plot(x,y2, '-b', label="$\\cos(-2x)$")
plt.axvline(-0.942 + -2*np.pi/5,color="red")
plt.axvline(-0.942,color="red") ## próba trafienia z Ox
plt.axvline(-0.942 + 2*np.pi/5,color="red")
plt.axvline(-0.942 + 2*2*np.pi/5,color="red")
plt.axvline(-0.942 + 3*2*np.pi/5,color="red")

plt.axhline(0.75,color="#FF6633")
plt.axhline(-0.25,color="#FF6633") ## próba trafienia z Oy
plt.axhline(-1,color="#FF6633")

X=[-0.942 - 2*np.pi/5, -0.942, -0.942 + 2*np.pi/5, -0.942 + 2*2*np.pi/5, -0.942 + 3*2*np.pi/5]
Y = [-0.25, -0.25, 0.75, -1, 0.75]

plt.scatter(X,Y)
plt.legend()
plt.title("Ręczne poszukiwanie miejsc przecięcia funkcji $\sin(3x)$ i $\cos(-2x)$")
plt.show()

M = list(zip(X,Y))
print("Znalezione współrzędne:\n",M,'\n')


@np.vectorize
def check_root(x):
    y = lambda x: np.sin(3*x) - np.cos(-2*x)
    d = 1e-2
    if y(x+d) > 0 and y(x) < 0:
        print(x,y(x))
        return 0
    elif y(x+d) < 0 and y(x) > 0:
        print(x,y(x))
        return 0
    elif y(x+d) - y(x) < 0 and y(x+2*d) > y(x) and abs(y(x+d)) < 1e-3:
        print(x,y(x))
        return 0
    elif y(x+d) - y(x) > 0 and y(x+2*d) < y(x) and abs(y(x+d)) < 1e-3:
        print(x,y(x))
        return 0
    else:
        return
    
x = np.linspace(-np.pi,np.pi,10000)
plt.plot(x,check_root(x), '-r',linewidth=4)
plt.plot(x,np.sin(3*x)-np.cos(-2*x), '-g')
plt.axhline(0,color="#000000")
plt.xlabel('x')
plt.ylabel('y')
plt.title("Poszukiwanie miejsc zerowych funkcji $f(x)=\sin(3x)-\cos(-2x)$")
plt.show()

##############
""" Zad. 3 """
##############
print("\n\n===> Zadanie 3\n")
plt.style.use("classic")

x = np.linspace(-6,1)
x1 = np.linspace(-5,-2)
x2 = np.linspace(-2,0)

y1 = lambda x: x**2 + 2*x - 2
y2 = lambda x: -3*x - 2
y3 = lambda x: 0*x - 2

plt.plot(x,y1(x), label="$y=x^2+2x-2$")
plt.plot(x,y2(x), label="$y=-3x-2$")
plt.plot(x,y3(x), label="$y=-2$")
plt.grid(True, alpha=0.3)
plt.legend()
plt.fill_between(x1, y1(x1), y2(x1), color="#000000", alpha=0.5, linewidth=0)
plt.fill_between(x2, y3(x2), y2(x2), color="#000000", alpha=0.5, linewidth=0)
plt.axhline(0, color='black',alpha=0.4)
plt.axvline(0, color='black',alpha=0.4)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Rysunek do zadania 3")
plt.show()

##############
""" Zad. 4 """
##############

x = np.arange(-1, 1,0.005)
y = np.arange(-2, 2,0.01)
X, Y = np.meshgrid(x, y)
Z=np.cos(3*np.cos(X**2+Y**2))

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init(20, -20)
ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel("$f(x,y)=\cos(3\cos(x^2+y^2))$")
plt.title("Zadanie 4")
plt.show()

##############
""" Zad. 5 """
##############

x = np.arange(-6, 6,0.05)
y = np.arange(-6, 6,0.05)
X, Y = np.meshgrid(x, y)
Z1 = (X**2 + Y**2)*2
Z2 = 1/2*X - 2*Y + np.pi*10

@np.vectorize
def graph_1(X,Y):
    Z1 = (X**2 + Y**2)*2
    Z2 = 1/2*X - 2*Y + np.pi*10
    if Z1 <= Z2:
        return Z2
    else:
        return Z1

@np.vectorize
def graph_2(X,Y):
    Z1 = (X**2 + Y**2)*2
    Z2 = 1/2*X - 2*Y + np.pi*10
    if Z2 <= Z1:
        return Z2
    else:
        return Z1

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, graph_1(X,Y), cmap='plasma', alpha=0.4)
ax.plot_surface(X, Y, graph_2(X,Y), cmap='plasma', alpha=0.1)
ax.view_init(19, 30)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title("Zadanie 5")
plt.show()