import math
import matplotlib.pyplot as plt
import numpy as np

a = 0
b = 8
eps = 0.0001

def f(x):
    return math.tanh(3 * math.sin(x)) - 2 * math.cos(x)

def df(x):
    return (3 * math.cos(x))/(pow(math.cosh(3 * math.sin(x)), 2)) + 2 * math.cos(x)

def d2f(x):
    return 2 * math.cos(x) - ((18 * math.cos(x) * math.sinh(3 * math.sin(x)))+(3 * math.sin(x) * math.cosh(3 * math.sin(x))))/(pow(math.cosh(3 * math.sin(x)), 3))

def newton(a, b, eps):
    if f(a)*d2f(a) > 0:
        x0 = b
    else: 
        x0 = a
    while abs(f(x0)) >= eps:
        x0 = x0 - f(x0)/df(x0)
        if f(x0) == 0 or abs(f(x0)) < eps:
            # print("Root found at x = ", x0)
            # print(a<=x0<=b)
            return x0
    print("No solution"); return None
        
print(newton(0, 2, eps))
print(newton(4, 5, eps))
print(newton(7, 8, eps))

#вышел за пределы отрезка
print(newton(2, 4, eps))

#первый попавшийся корень
print(newton(0, 8, eps)) 

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = [f(i) for i in x]

plt.plot(x, y)
plt.grid(True)
plt.title('Graph of f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()