#algorithme de régression linéaire
import random as rand
import matplotlib.pyplot as plt







def fitness(x,y):
    return abs(x-y)

a = 1
b = 1
n = 0.01
def f(x):
    global a
    global b
    return a*x+b


X_dispersion = [i for i in range(0,100,2)]
Y_dispersion = [i*2+4 for i in range(0,100,2)]



def cost(X,Y):
    somme = 0
    for i in range(len(X)):
        x = X[i]
        y = Y[i]
        somme = somme + (f(x)-y)**2
    return somme


def descente_de_gradient(f,X,Y,n):
    global a
    global b
    a_new = a - n*2*sum([(f(x)-y)*x for x,y in zip(X,Y)])/len(X)
    b_new = b - n*2*sum([(f(x)-y) for x,y in zip(X,Y)])/len(X)
    return a_new,b_new

def main():
    global a
    global b
    for i in range(100):
        a,b = descente_de_gradient(f,X_dispersion,Y_dispersion,n)
        print(a,b)
        print(cost(X_dispersion,Y_dispersion))
        print("\n")


main()
print(a,b)
plt.plot(X_dispersion,[f(x) for x in X_dispersion])
plt.plot(X_dispersion,Y_dispersion,'o')
plt.show()