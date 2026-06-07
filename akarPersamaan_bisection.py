# NAMA: Rifqi Nurul Fikri
# NIM: 13324077
# PROGRAM: Bisection Method

def f(w:float) -> float: # fungsi
    Z = 75
    R = 185 
    L = 0.6
    C = 10**(-6)
    
    return (1/(R*R)) - ((w*C - 1/(w*L))**2) - (1/Z)**2

x1 = 100 # terkaan kiri
x2 = 1000 # terkaan kanan
e = 0.1/10000 # error diizinkan
xr = (x1+x2)/2 # titik tengah terkaan

ea = 100 # asumsi error awal
i = 0 # indeks iterasi

while ea > e: # perulangan bisection method
    i = i + 1
    xl = xr
    xr = (x1+x2)/2
    if f(x1)*f(xr) > 0:
        x1 = xr
    elif f(x1)*f(xr) < 0:
        x2 = xr
    if xl != 0:
        ea = abs((xr-xl)/xl)

print(f"Aproksimasi akar adalah: {xr} dengan jumlah iterasi {i}")