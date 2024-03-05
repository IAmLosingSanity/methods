import math
import matplotlib.pyplot as plt
import numpy as np

a = 0
b = 8
eps = 0.001
 
def root(f, a, b, e):
    fa = f(a)
    fb = f(b)
    if fa*fb > 0:
        return None
    while True:
        c = 0.5*(a+b)
        if abs(b-a) <= e:
            return c;
        fc = f(c)
        if abs(fc) <= e:
            return c;
        if fa*fc<0:
            b = c
            fb = fc
        elif fb*fc<0:
            a = c 
            fa = fc
        else:
            return None
 
print(root(lambda x: math.tanh(3 * math.sin(x)) - 2 * math.cos(x), a, b, eps))