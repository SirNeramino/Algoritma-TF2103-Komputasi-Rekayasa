import math

def f(x:float) -> float:
    return (2*math.sin(x))-((x**2)/10)

a = 0 # batas bawah
b = 4 # batas atas

phi = (5**(1/2) - 1)/2

for i in range(5000):
    x1 = b - phi*(b-a)
    x2 = a + phi*(b-a)
    if f(x1) < f(x2):
        a = x2 
    else:
        b = x1

print(f"x_opt = {(a+b)/2} f_opt = {f((a+b)/2)}")