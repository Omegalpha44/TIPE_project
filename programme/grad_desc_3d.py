import matplotlib.pyplot as plt

import numpy as np
import random as rand


a = 0
b = 0
c = 0
k = 0
l = 0
m = 0
X_dispersion = np.linspace(0, 1, 100)
Y_dispersion = [rand.randint(i-20,i+20) for i in range(len(X_dispersion))]
Z_dispersion = [rand.randint(i-20,i+20) for i in range(len(X_dispersion))]
alpha = 0.01


def f(x,y):
    """défini la fonction que l'on souhaite régresser"""
    global a 
    global b 
    global c 
    global k
    global l
    global m
    return (a*x**2+b*x+c) + (k*y**2+l*y+m)

def cost():
    """défini la fonction cost de f"""
    n = len(X_dispersion)
    res = 0
    for i in range(n):
        res+= (f(X_dispersion[i],Y_dispersion[i])-Z_dispersion[i])**2
    return res/n

def gradient():
    global a 
    global b 
    global c 
    global k
    global l
    global m
    n = len(X_dispersion)
    L = [0]*6
    for i in range(n):
        L[0]+= (f(X_dispersion[i],Y_dispersion[i])-Z_dispersion[i])*X_dispersion[i]**2
        L[1]+= (f(X_dispersion[i],Y_dispersion[i])-Z_dispersion[i])*X_dispersion[i]
        L[2]+= (f(X_dispersion[i],Y_dispersion[i])-Z_dispersion[i])
        L[3]+= (f(X_dispersion[i],Y_dispersion[i])-Z_dispersion[i])*Y_dispersion[i]**2
        L[4]+= (f(X_dispersion[i],Y_dispersion[i])-Z_dispersion[i])*Y_dispersion[i]
        L[5]+= (f(X_dispersion[i],Y_dispersion[i])-Z_dispersion[i])
    return L[0]/n, L[1]/n, L[2]/n, L[3]/n, L[4]/n, L[5]/n

def descente_gradient(n):
    global a 
    global b 
    global c 
    global k
    global l
    global m
    global alpha
    for i in range(n):
        a,b,c,x,y,z = gradient()
        k = k - alpha*x
        l = l - alpha*y
        m = m - alpha*z
        a = a - alpha*a
        b = b - alpha*b
        c = c - alpha*c
    return
descente_gradient(10000)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.scatter(X_dispersion, Y_dispersion,Z_dispersion, label="y")
plt.scatter(X_dispersion,Y_dispersion, [f(x,y) for x,y in zip(X_dispersion,Y_dispersion)], label="f(x)")
    """_summary_
    """plt.show()