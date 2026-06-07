# NAMA: Rifqi Nurul Fikri
# NIM: 13324077
# PROGRAM: Secant Method

def f(w:float) -> float: # fungsi
    Z = 75
    R = 185 
    L = 0.6
    C = 10**(-6)
    
    return (1/(R*R)) -  (w*C-(1/(w*L))**2) - (1/Z)**2

x = [] # array akar
e = 10^(-12) # error diizinkan

x.append(float(100)) # terkaan awal pertama
x.append(float(200)) # terkaan awal kedua 
ea = 100 # asumsi error awal
i = 1 # indeks iterasi

while ea > e  and i < 1e5: # perulangan secant method
    i = i + 1
    if f(x[i-1])-f(x[i-2]) == 0:
        break
    x.append(x[i-1]- ((x[i-1]-x[i-2])*f(x[i-1])) / (f(x[i-1])-f(x[i-2])))
    if x[i] != 0:
        ea = abs((x[i]-x[i-1])/x[i])

print(f"Aproksimasi akar adalah: {x[i-1]} dengan jumlah iterasi {i}")
