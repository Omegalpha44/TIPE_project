
import matplotlib.pyplot as plt
import numpy as np
import random as rand
X_dispersion = np.linspace(0, 1, 100)

Y_dispersion = [rand.randint(i-20,i+20) for i in range(len(X_dispersion))]
a=0
b=0
c=0
alpha = 0.01


def f(x):
    global a
    global b
    global c 
    return a*x**2+b*x+c


def gradient():
    global a
    global b
    global c 
    m = len(X_dispersion)
    res1 = 0
    res2 = 0
    res3=0
    for i in range(m):
        res1+= (f(X_dispersion[i])-Y_dispersion[i])*X_dispersion[i]**2
        res2+= (f(X_dispersion[i])-Y_dispersion[i])*X_dispersion[i]
        res3+= (f(X_dispersion[i])-Y_dispersion[i])
    return res1/m, res2/m, res3/m

def descente_gradient(n):
    global a 
    global b 
    global c 
    for i in range(n):
        x,y,z = gradient()
        a = a - alpha*x
        b = b - alpha*y
        c = c - alpha*z
    return
descente_gradient(10000)

plt.plot(X_dispersion, f(X_dispersion), label="f(x)")
plt.plot(X_dispersion, Y_dispersion, 'o', label="y")
plt.show()
