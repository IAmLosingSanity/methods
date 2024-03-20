import math

def f(x):
    return x**2 / math.sqrt(9 - x**2)

def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        s += f(a + i * h)
    
    integral = h * s

    abs_error = abs(integral - ((29 * math.atan(2.5) - 10) / 58))
    rel_error = abs_error / abs((29 * math.atan(2.5) - 10) / 58)

    return integral, abs_error, rel_error

a = 0.0
b = 2.5
n = 1000

integral_value, abs_err, rel_err = trapezoidal_rule(a, b, n)
print(f"Приближенное значение интеграла: {integral_value}, абсолютная погрешность: {abs_err}, относительная погрешность: {rel_err}")