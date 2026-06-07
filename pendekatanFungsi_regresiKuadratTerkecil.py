def metodeGauss(banyak_persamaan, koefisien, konstanta):
    solusi = [0 for i in range (banyak_persamaan)]
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

def f_pred(k,x):
    m = len(k) # orde polinom
    res = 0
    for i in range(m):
        res = res + k[i]*x**i
    return res

x_input = [1,3,4,6,8,11]
y_input = [1,0.6,0.5,0.4,0.38,0.35]
n = 6 # banyak data
m = 5 # orde regresi < n

A = [[0 for j in range(m+1)] for i in range(m+1)] # bentuk matrik m+1 x m+1 dengan entri 0

x_power = [0 for i in range (2*m+1)] # membuat sum x^m
for i in range(2*m+1):
    for j in range(n):
        x_power[i] = x_power[i] + x_input[j]**i

for i in range(m+1): # mengisi matriks A
    for j in range(m+1):
        A[i][j] = x_power[i+j]

A[0][0] = n

xy_power = [0 for i in range(m+1)] # membuat vektor xy
for i in range(m+1):
    for j in range(n):
        xy_power[i] = xy_power[i] + y_input[j]*x_input[j]**i

k = metodeGauss(m+1,A,xy_power)

sum_y_input = 0
for i in range(n):
    sum_y_input = sum_y_input + y_input[i]
y_mean = sum_y_input/n

St = 0
for i in range(n):
    St = St + (y_input[i]-y_mean)**2

y_pred = [0 for i in range(n)]

for i in range(n):
    y_pred[i] = f_pred(k,x_input[i])

Sr = 0
for i in range(n):
    Sr = Sr + (y_input[i]-y_pred[i])**2

R_squared = (St-Sr)/St

print(k)
print(St,Sr,R_squared)