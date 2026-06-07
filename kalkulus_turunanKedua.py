# NIM/Nama : 13324077/Rifqi Nurul Fikri

def f(x):
    return 77*x**2
# Metode beda maju
def diff2_forward(f_i, f_next, f_next2, h):
    return (f_next2 - 2*f_next + f_i)/(h**2)
# Metode beda mundur
def diff2_backward(f_prev2, f_prev, f_i, h):
    return (f_i - 2*f_prev + f_prev2)/(h**2)
# Metode beda tengah
def diff2_central(f_next, f_i, f_prev, h):
    return (f_next - 2*f_i + f_prev)/(h**2)

x_i = 5 # nilai x dari turunan yang ingin dicari
h = 3e-5
# nilai fungsi di sekitar x_i
f_prev2 = f(x_i-2*h)
f_prev = f(x_i-h)
f_i = f(x_i)
f_next = f(x_i+h)
f_next2 = f(x_i+2*h)
# hitung turunan kedua numerik
f2_fwd = diff2_forward(f_i, f_next, f_next2, h)
f2_bwd = diff2_backward(f_prev2, f_prev, f_i, h)
f2_ctr = diff2_central(f_next, f_i, f_prev, h)
print("Turunan kedua beda maju :", f2_fwd)
print("Turunan kedua beda mundur :", f2_bwd)
print("Turunan kedua beda tengah :", f2_ctr)