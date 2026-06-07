def swap(a,b):
    temp = a
    a = b 
    b = temp
    return None

banyak_persamaan = 3
koefisien = [[1,1,-1],
             [0,45,10],
             [42,0,10]]
konstanta = [0,0,50]
solusi = [0,0,0]

for k in range(banyak_persamaan):
    # Normalisasi baris pivot
    if(koefisien[k][k] == 0 and k < banyak_persamaan - 1):
        for i in range(k+1, banyak_persamaan):
            if koefisien[i][k] != 0:
                swap(koefisien[k],koefisien[i])
                break

    pivot = koefisien[k][k]
    if pivot == 0:
        print("Tidak ada solusi")
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

print("Solusi dari sistem persamaan tersebut adalah")
for i in range(banyak_persamaan):
    print(f"x_{i+1}: {solusi[i]}")
