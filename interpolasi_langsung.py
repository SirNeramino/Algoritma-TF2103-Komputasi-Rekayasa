def buatMatriksPolinomial(x_input, derajat_polinomial):
    koefisien = []
    for i in range(derajat_polinomial):
        temp = []
        for j in range(derajat_polinomial):
            temp.append(x_input[i]**j)
        koefisien.append(temp)
    return koefisien

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

# dua buah pasangan input data
# a0 + a1x
banyak_data = 2
x_input = [10,14]
y_input = [1345,1007.4]
x = 11 # nilai x yang ingin diinterpolasi
koefisien = buatMatriksPolinomial(x_input,banyak_data)
solusi = metodeGauss(banyak_data,koefisien,y_input)
hasil = 0
for i in range(banyak_data):
    hasil = hasil + solusi[i]*(x**i)
print(f"Dengan {banyak_data} buah pasangan input data, f({x}) = {hasil}")

# seluruh (enam buah) pasangan input data
# a0 + a1x + a2x^2 + a3x^3 + ... + a5x^5
banyak_data = 6
x_input = [1,3,7,10,14,16]
y_input = [57.1,295.7,991.3,1345,1007.4,286.6]
x = 11 # nilai x yang ingin diinterpolasi
koefisien = buatMatriksPolinomial(x_input,banyak_data)
solusi = metodeGauss(banyak_data,koefisien,y_input)
hasil = 0
for i in range(banyak_data):
    hasil = hasil + solusi[i]*(x**i)
print(f"Dengan {banyak_data} buah pasangan input data, f({x}) = {hasil:.2f}")

