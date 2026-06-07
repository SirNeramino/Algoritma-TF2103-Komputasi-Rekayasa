import numpy as np
import matplotlib.pyplot as plt

#konstanta
g = 9.8 # m/s^2
k = 40 # N/m
L = 0.5 # m
m = 0.25 # kg

def a_der(a,b,c,d):
    return b

def b_der(a,b,c,d):
    return -2*d*b/c - g/c*np.sin(a)

def c_der(a,b,c,d):
    return d

def d_der(a,b,c,d):
    return c*b**2 + g*np.cos(a) - (k/m)*(c-L)

def RK4(a,b,c,d,h):
    k1_1 = a_der(a,b,c,d)
    k1_2 = b_der(a,b,c,d)
    k1_3 = c_der(a,b,c,d)
    k1_4 = d_der(a,b,c,d)

    k2_1 = a_der(a + 0.5*h*k1_1, b + 0.5*h*k1_2, c + 0.5*h*k1_3, d + 0.5*h*k1_4)
    k2_2 = b_der(a + 0.5*h*k1_1, b + 0.5*h*k1_2, c + 0.5*h*k1_3, d + 0.5*h*k1_4)
    k2_3 = c_der(a + 0.5*h*k1_1, b + 0.5*h*k1_2, c + 0.5*h*k1_3, d + 0.5*h*k1_4)
    k2_4 = d_der(a + 0.5*h*k1_1, b + 0.5*h*k1_2, c + 0.5*h*k1_3, d + 0.5*h*k1_4)

    k3_1 = a_der(a + 0.5*h*k2_1, b + 0.5*h*k2_2, c + 0.5*h*k2_3, d + 0.5*h*k2_4)
    k3_2 = b_der(a + 0.5*h*k2_1, b + 0.5*h*k2_2, c + 0.5*h*k2_3, d + 0.5*h*k2_4)
    k3_3 = c_der(a + 0.5*h*k2_1, b + 0.5*h*k2_2, c + 0.5*h*k2_3, d + 0.5*h*k2_4)
    k3_4 = d_der(a + 0.5*h*k2_1, b + 0.5*h*k2_2, c + 0.5*h*k2_3, d + 0.5*h*k2_4)

    k4_1 = a_der(a + h*k3_1, b + h*k3_2, c + h*k3_3, d + h*k3_4)
    k4_2 = b_der(a + h*k3_1, b + h*k3_2, c + h*k3_3, d + h*k3_4)
    k4_3 = c_der(a + h*k3_1, b + h*k3_2, c + h*k3_3, d + h*k3_4)
    k4_4 = d_der(a + h*k3_1, b + h*k3_2, c + h*k3_3, d + h*k3_4)

    a_baru = a + (h/6) * (k1_1 + 2*k2_1 + 2*k3_1 + k4_1)
    b_baru = b + (h/6) * (k1_2 + 2*k2_2 + 2*k3_2 + k4_2)
    c_baru = c + (h/6) * (k1_3 + 2*k2_3 + 2*k3_3 + k4_3)
    d_baru = d + (h/6) * (k1_4 + 2*k2_4 + 2*k3_4 + k4_4)

    return a_baru, b_baru, c_baru, d_baru

t_0 = 0
t_f = 3
h = 0.001
N = int((t_f-t_0)/h)

t_values = [t_0 + i*h for i in range(N + 1)]
a_new = [0 for i in range(N + 1)]
b_new = [0 for i in range(N + 1)]
c_new = [0 for i in range(N + 1)]
d_new = [0 for i in range(N + 1)]

a_new[0] = np.pi/3
b_new[0] = 0
c_new[0] = L
d_new[0] = 0

print("theta \t theta_d r \t r_d")
for i in range(N):
    a_new[i+1], b_new[i+1], c_new[i+1], d_new[i+1] = RK4(a_new[i],b_new[i],c_new[i],d_new[i],h)
    if(i+1)%50 == 0:
        print(f"{a_new[i+1]:.2f} \t {b_new[i+1]:.2f} \t {c_new[i+1]:.2f} \t {d_new[i+1]:.2f}")

# Konversi Koordinat Polar (r, theta) ke Kartesian (x, y)
r_plot = c_new
theta_plot = a_new
# x = r * sin(theta)
x_koordinat = c_new * np.sin(theta_plot)
# y = -r * cos(theta) (Negatif karena y=0 di atas, dan bandul bergerak ke bawah)
y_koordinat = -1 * np.array(c_new) * np.cos(np.array(theta_plot))
plt.figure(figsize=(6, 6))
plt.plot(x_koordinat, y_koordinat, 'b-', label='Lintasan Bandul')
plt.plot(x_koordinat[0], y_koordinat[0], 'ro', label='Titik Awal')
plt.plot(0, 0, 'kx', label='Titik Tumpu') # Titik Tumpu
plt.title('Lintasan Bandul Pegas Elastis')
plt.xlabel('Posisi Horizontal (x)')
plt.ylabel('Posisi Vertikal (y)')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()