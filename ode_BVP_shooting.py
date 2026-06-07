"""
dy1/dx = y_2
dy2/dx = -h(T_a - y_1)
"""

def y1_der(y1,y2):
    return y2

def y2_der(y1,y2):
    h_koef = 0.01
    Ta = 20
    return -h_koef*(Ta-y1)

def RK4(y1,y2,h):
    k1_1 = y1_der(y1,y2)
    k1_2 = y2_der(y1,y2)

    k2_1 = y1_der(y1 + 0.5*h*k1_1, y2 + 0.5*h*k1_2)
    k2_2 = y2_der(y1 + 0.5*h*k1_1, y2 + 0.5*h*k1_2)

    k3_1 = y1_der(y1 + 0.5*h*k2_1, y2 + 0.5*h*k2_2)
    k3_2 = y2_der(y1 + 0.5*h*k2_1, y2 + 0.5*h*k2_2)

    k4_1 = y1_der(y1 + h*k3_1, y2 + h*k3_2)
    k4_2 = y2_der(y1 + h*k3_1, y2 + h*k3_2)
    
    y1_new = y1 + (h/6) * (k1_1 + 2*k2_1 + 2*k3_1 + k4_1)
    y2_new = y2 + (h/6) * (k1_2 + 2*k2_2 + 2*k3_2 + k4_2)
    
    return y1_new, y2_new

def ODE_solve(z):
    x0 = 0
    T1 = 40
    T2 = 200 # T(x = L = 10)
    xt = 10
    h = 0.001
    N = int((xt-x0)/h)
    x_value = [x0 + i*h for i in range(N + 1)]
    y1_new = [0 for i in range(N + 1)]
    y1_new[0] = T1
    y2_new = [0 for i in range(N + 1)]
    y2_new[0] = z # tebakan
    for i in range(N):
       y1_new[i+1], y2_new[i+1] = RK4(y1_new[i],y2_new[i],h)
    print(f"T[x = {x_value[N]}] = {y1_new[N]:.4f}")
    return y1_new[N]

def bisection(d):
    x1 = 10 # x1 < x2
    x2 = 20
    e = 1
    e_a = 0.001/100
    f1 = ODE_solve(x1) - d # d = nilai yang diinginkan 
    f2 = ODE_solve(x2) - d
    while e > e_a:
        m = (x2+x1)/2
        fm = ODE_solve(m) - d

        if f1*fm < 0:
            x2 = m
            f2 = fm
        elif fm*f2 < 0:
            x1 = m
            f1 = fm
        else:
            break
        e = abs(x2-x1)

    print(f"dT/dx [x = 0] = {m:.4f}")


T2 = 200 # T(x = L = 10)
bisection(T2)