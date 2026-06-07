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

x_input = [0,3,5,8,10,12]
y_input = [80, 374.6, 555, 777.6, 880, 934.4]
n = 6 # banyak data
m = 3 # orde
x = 9

# konstruksi matriks augmentasi
A = []
for i in range(m+1):
    array_sementara = []
    for j in range(n):
        array_sementara.append(x_input[i]**j)
    A.append(array_sementara)

a = metodeGauss(m+1,A,y_input) # a0 a1 a2 dst
# cari f(11)
hasil = 0
for i in range(m+1):
    hasil = hasil + a[i]*x**i

print(a)
print(f"Hasil interpolasi f({x}) = {hasil:.4f}")
