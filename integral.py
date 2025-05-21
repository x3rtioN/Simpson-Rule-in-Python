import scipy.integrate as integrate 

import numpy as np 

def integrand(x): 

    return x / np.sqrt(x**2 + 4.78) 

result, error = integrate.quad(integrand, 1, 3) 

print(f'Exact value: {result}, Error estimate: {error}') 