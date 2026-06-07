# NIM/Nama : 13324077/Rifqi Nurul Fikri

import numpy as np

# ln(1+tan(x))

def f(x):
    return np.log(1+np.tan(x)) # fungsi

def integ_rectangular (a, b, n):
    h = (b-a)/n # lebar tiap subinterval
    s = 0.0 # buat variable untuk menyimpan hasil penjumlahan
    for i in range(n):
        x_i = a+i*h # titik kiri tiap interval
        s += f(x_i)
    return h*s

def integ_trapezoidal(a,b,n):
    h = (b-a)/n # lebar tiap subinterval
    s = 0.0 # buat variable untuk menyimpan hasil penjumlahan
    # Jumlahkan nilai fungsi di titik-titik tengah (selain ujung)
    for i in range(1, n):
        x_i = a+i*h
        s += 2*f(x_i)
    return h/2 * (f(a) + s + f(b)) # Terapkan rumus trapezoidal rule

def integ_simpson1_3(a, b, n):
    if n % 2 != 0:
        raise ValueError("n harus genap untuk metode Simpson 1/3")
    h = (b-a)/n
    s = 0.0
    # Tambahkan nilai dengan pola 4 dan 2 secara bergantian
    for i in range(1, n):
        x_i = a+i*h
        if i % 2 == 0:
            s += 2 * f(x_i)
        else:
            s += 4 * f(x_i)
    return h/3 * (f(a) + s + f(b))

def integ_simpson3_8(a, b, n):
    if n % 3 != 0:
        raise ValueError("n harus kelipatan 3 untuk metode Simpson 3/8")
    h = (b-a)/n
    s = 0.0
    for i in range(1, n):
        x_i = a+i*h
        if i % 3 == 0:
            s += 2*f(x_i)
        else:
            s += 3*f(x_i)
    return 3*h/8 * (f(a) + s + f(b))

print(f"Metode segi-empat: {integ_rectangular(0,np.pi/4,300000)}")
print(f"Metode trapesium: {integ_trapezoidal(0,np.pi/4,300000)}")
print(f"Metode simpson 1/3: {integ_simpson1_3(0,np.pi/4,300000)}")
print(f"Metode simpson 3/8: {integ_simpson3_8(0,np.pi/4,300000)}")