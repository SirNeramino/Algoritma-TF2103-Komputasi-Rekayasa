import numpy as np

def f(x, y):
    return -2*x**3 + 12*x**2 - 20*x + 8.5

def euler(x,y,h):
    return y + f(x,y)*h

def heun(x,y,h):
    y2 = y + f(x,y)*h
    avg = 0.5*(f(x,y) + f(x+h,y2))*h    
    return y + avg

def midpoint(x,y,h):
    y2 = y + f(x,y)*h/2
    x2 = x + 0.5*h
    return y + f(x2,y2)*h

def ralston(x,y,h):
    k1 = f(x,y)
    k2 = f(x + 0.75*h, y + 0.75*k1*h)
    return y + (k1/3 + 2*k2/3)*h

def runge_kutta_4(x,y,h):
    k1 = f(x,y)
    k2 = f(x + 0.5*h, y + 0.5*k1*h)
    k3 = f(x + 0.5*h, y + 0.5*k2*h)
    k4 = f(x + h, y + k3*h)
    return y + (k1 + 2*k2 + 2*k3 + k4)*h/6

x0 = 0.0
y0 = 1.0
xf = 4.0
h = 0.25
N = int((xf - x0) / h)
# Inisialisasi array hasil
x_values = [x0 + i*h for i in range(N + 1)]
y_new_euler = [0 for i in range(N + 1)]
y_new_heun = [0 for i in range(N + 1)]
y_new_midpoint = [0 for i in range(N + 1)]
y_new_ralston = [0 for i in range(N + 1)]
y_new_rungekutta4 = [0 for i in range(N + 1)]
# Syarat Awal
y_new_euler[0] = y0
y_new_heun[0] = y0
y_new_midpoint[0] = y0
y_new_ralston[0] = y0
y_new_rungekutta4[0] = y0

print("No.\t x \t euler \t\t heun \t\t midpoint \t ralston \t runge kutta 4th")
print("="*95)
for i in range(N):
    x_values[i+1] = x_values[i] + h
    
    y_new_euler[i+1] = euler(x_values[i],y_new_euler[i],h)
    y_new_heun[i+1] = heun(x_values[i],y_new_heun[i],h)
    y_new_midpoint[i+1] = midpoint(x_values[i],y_new_midpoint[i],h)
    y_new_ralston[i+1] = ralston(x_values[i],y_new_ralston[i],h)
    y_new_rungekutta4[i+1] = runge_kutta_4(x_values[i],y_new_rungekutta4[i],h)

    print(f"{i+1}\t {x_values[i+1]:.1f} \t {y_new_euler[i+1]:.4f} \t {y_new_heun[i+1]:.4f}",end="") 
    print(f" \t {y_new_midpoint[i+1]:.4f} \t {y_new_ralston[i+1]:.4f} \t {y_new_rungekutta4[i+1]:.4f}")