def f(x):
    return x**2 / (x**2 + 1)**2

def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        s += f(a + i * h)
    
    return h * s

a = 0
b = 2,5
n = 1000

integral_value = trapezoidal_rule(a, b, n)
print(f"Приближенное значение интеграла: {integral_value}")