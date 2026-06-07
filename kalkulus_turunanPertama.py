# NIM/Nama : 13324077/Rifqi Nurul Fikri

def f(x):
    return 77*x**2 # fungsi
# Metode Beda Maju
def diff_forward(f_next, f_i, h):
    return (f_next-f_i)/h
# Metode Beda Mundur
def diff_backward(f_i, f_prev, h):
    return (f_i-f_prev)/h
# Metode Beda Tengah
def diff_central(f_next, f_prev, h):
    return (f_next - f_prev)/(2*h)

x_i = 5 # nilai x dari turunan yang ingin dicari
h = 3e-5
# nilai fungsi di titik-titik sekitar x_i
f_prev = f(x_i-h)
f_i = f(x_i)
f_next = f(x_i+h)
# hitung turunan numerik
fwd = diff_forward(f_next, f_i, h)
bwd = diff_backward(f_i, f_prev, h)
ctr = diff_central(f_next, f_prev, h)
print("Turunan beda maju :", fwd)
print("Turunan beda mundur :", bwd)
print("Turunan beda tengah :", ctr)