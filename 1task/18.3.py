import math
import matplotlib.pyplot as plt
import numpy as np

a = 0
b = 8
eps = 0.01

def f(x):
    return math.tanh(3 * math.sin(x)) - 2 * math.cos(x)

def bisection(a, b, eps):
    while abs(f(b)-f(a)) >= eps:
        mid = (a+b)/2
        if f(mid) == 0 or abs(f(mid)) < eps:
            print("Root found at x = ", mid)
            return mid
        elif f(a)*f(mid) < 0:
            b = mid
        else:
            a = mid
    else: print("No solution"); return -1

for i in range(b):
    print(i)
    bisection(a, b, eps)
    a = a + 1

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = [f(i) for i in x]

plt.plot(x, y)
plt.grid(True)
plt.title('Graph of f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()