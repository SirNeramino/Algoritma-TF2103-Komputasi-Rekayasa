def metodeGauss(banyak_persamaan, koefisien, konstanta):
    solusi = [0 for _ in range (banyak_persamaan)]
    for k in range(banyak_persamaan):
        # Normalisasi baris pivot
        pivot = koefisien[k][k]
        if(pivot == 0):
            print("Sistem persamaan tidak memiliki solusi")
            break
        
        for j in range(k,banyak_persamaan):
            koefisien[k][j] = koefisien[k][j] / pivot
        konstanta[k] = konstanta[k] / pivot

        # Eliminasi baris di bawah
        for i in range(k+1,banyak_persamaan):
            faktor = koefisien[i][k]
            for j in range(k,banyak_persamaan):
                koefisien[i][j] = koefisien[i][j] - (faktor*koefisien[k][j])
            konstanta[i] = konstanta[i] - (faktor*konstanta[k])

    # Substitusi mundur
    for i in range(banyak_persamaan-1, -1, -1):
        solusi[i] = konstanta[i]
        for j in range(i+1,banyak_persamaan):
            solusi[i] = solusi[i] - (koefisien[i][j]*solusi[j])
    
    return solusi

def f(x,y,z):
    return x+y+z

x1 = 0 # batas bawah
x2 = 10 # batas atas
h = 1 # panjang interval
N = int((x2-x1)/h)

y0 = 10 #  y(x1)
yN = 100 # y(x2)

x_values = [x1+i*h for i in range(N+1)]

A = [[0 for j in range (0,N-1)] for i in range(0,N-1)]

for i in range(N-1):
    A[i][i] = 2

for i in range(N-2):
    A[i][i+1] = -1
    A[i+1][i] = -1

b = [0 for i in range(N-1)]
for i in range(1, N):
    b[i-1] = h*h * f(x_values[i])

b[0] = b[0] + y0
b[N-2] = b[N-2] + yN

y_values = metodeGauss(N-1, A, b)