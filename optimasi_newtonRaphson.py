import math
e = 2.7182818284590452353602874713527
def f(x:float) -> float:
    return (20*(e**(-x/2))) - (18*x*(e**(-x/2))) + (2*(x**2)*(e**(-x/2)))

def f_d(x:float) -> float:
    return -(28*(e**(-x/2))) + (13*x*(e**(-x/2))) - ((x**2)*(e**(-x/2)))

def f_dd(x:float) ->float:
    pembilang = x**2-17*x+54
    penyebut = 2* (e**(x/2))
    return pembilang/penyebut

x = [] # array akar

x.append(float(1)) # terkaan awal
ea = 100 # asumsi error awal
i = 0 # indeks iterasi

while i < 100: # perulangan newton-raphson method
    i = i + 1
    if f_dd(x[i-1]) == 0:
        break
    x.append(x[i-1] - (f_d(x[i-1])/f_dd(x[i-1])))

print(f"x_opt = {x[i-1]} f_opt = {f(x[i-1])}")