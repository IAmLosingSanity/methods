import math

def f(x):
    if x == 0:
        return 0
    return (math.sin(x))/x

def d2f(x):
    return -((pow(x, 2) - 2) * math.sin(x) + 2 * x * math.cos(x))/pow(x, 3)

def integral_rectangle(a, b, n):
    h = (b - a) / n
    total = 0
    for i in range(n):
        x = a + i * h
        total += f(x)
    integral = total * h

    abs_error = abs(integral - (math.cos(8) - 1) / math.cos(1))
    rel_error = abs_error / abs((math.cos(8) - 1) / math.cos(1))

    r = d2f(x) * (b-a) * h**2/24

    return integral, abs_error, rel_error, r

a = 0.0

b = 8.0

n = 1000

result, abs_error, rel_error, r = integral_rectangle(a, b, n)
print(f'numeric integral: {result}, abs error: {abs_error}, rel error: {rel_error}, r: {r}')
