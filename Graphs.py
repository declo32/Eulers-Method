from matplotlib import pyplot as plt
from EulersMethod import eulersMethod
import math

def diffEq(x, y):
    return y

Xs1 = [0.01 * x for x in range(101)]
Ys1 = [math.exp(x) for x in Xs1]

for i in range(1, 101):
    print(i/100)
    Xs, Ys = zip(*list(eulersMethod(diffEq, 0, 1, 1, 1/i)))

    plt.plot(Xs, Ys, "bo--")
    plt.plot(Xs1, Ys1, "r-")

    plt.title("Approximating e^x with Euler's Method")
    plt.legend(("Approximation with deltaX={0:.4f}".format(1/i), "e^x"),
            loc="upper left")
    plt.savefig("./img/img{0:03d}".format(i))
    plt.close()
