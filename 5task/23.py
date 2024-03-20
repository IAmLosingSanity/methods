import math

def f(x):
    return x**2 / math.sqrt(9 - x**2)

def d2f(x):
    return - (math.sqrt(9 - x**2)) * (x**3 - 18*x)/(x**4 - 18 * x**2 +81)

def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        x = a + i * h
        total += f(x)

    integral = total * h

    abs_error = abs(integral - ((36 * math.asin(5/6) - 5 * math.sqrt(11))/8))
    rel_error = abs_error / abs(((36 * math.asin(5/6) - 5 * math.sqrt(11))/8))

    r = d2f(x) * (b-a) * h**2/12

    return integral, abs_error, rel_error, r

a = 0.0
b = 2.5
n = 10

integral_value, abs_err, rel_err, r = trapezoidal_rule(a, b, n)
print(f"Приближенное значение интеграла: {integral_value}, абсолютная погрешность: {abs_err}, относительная погрешность: {rel_err}, r: {r}")