import random
import math

def f(x):
    return 5*math.cos(x)-1.5*math.sin(x)

x1 = 0
x2 = 6

infinity = 1e12
max_x = 0 
max_z = infinity

for i in range(50000):
    x = x1 + (x2-x1)*random.random()
    z = f(x)
    if z < max_z:
        max_z = z
        max_x = x

print(f"titik optimum ada di ({max_x},{max_z})")
