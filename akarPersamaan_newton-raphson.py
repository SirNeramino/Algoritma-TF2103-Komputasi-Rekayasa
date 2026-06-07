# NAMA: Rifqi Nurul Fikri
# NIM: 13324077
# PROGRAM: Newton-Raphson Method

def f(x:float) -> float: # fungsi
    return x**2-2*x+1

def f_d(x:float) -> float: # turunan fungsi
    return 2*x-2

x = [] # array akar
e = 10^(-9) # error diizinkan

x.append(float(100.0)) # terkaan awal
ea = 1 # asumsi error awal
i = 0 # indeks iterasi

while ea > e  and i < 100: # perulangan newton-raphson method
    i = i + 1
    if f_d(x[i-1]) == 0:
        break
    x.append(x[i-1]-f(x[i-1])/f_d(x[i-1]))
    ea = abs(x[i]-x[i-1])

print(f"Aproksimasi akar adalah: {x[i]}")