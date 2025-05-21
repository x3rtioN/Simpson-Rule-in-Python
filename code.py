import numpy as np

def f(x, a):
    return x / np.sqrt(x**2 + 4.78)

def composite_simpsons(a, b, M, func, a_param):
    h = (b - a) / (2 * M)
    integral = func(a, a_param) + func(b, a_param)
    
    for i in range(1, M):
        integral += 2 * func(a + 2 * i * h, a_param)
    
    for i in range(1, M + 1):
        integral += 4 * func(a + (2 * i - 1) * h, a_param)
    
    integral *= h / 3
    return integral

a_param = 78  # Last two digits of my student ID
a, b = 1, 3

for M in range(1, 9):
    result = composite_simpsons(a, b, M, f, a_param)
    print(f'M = {M}, S_{M} = {result}')
