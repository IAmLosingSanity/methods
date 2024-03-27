import math

def f(x):
    return 6/(math.sqrt(5 + 4*x - x**2))

def simpson(a, b, n):
    if n % 2:
        raise ValueError("n must be even")

    h = (b - a) / n
    k = 0.0
    x = a + h

    for i in range(1, n // 2 + 1):
        k += 4 * f(x)
        x += 2 * h

    x = a + 2 * h

    for i in range(1, n // 2):
        k += 2 * f(x)
        x += 2 * h
    
    return (h / 3) * (f(a) + f(b) + k)

a = 2
b = 3.5
n = 1000
integral = simpson(a, b, n)
print(f"Приближенное значение интеграла: {integral}")