n = 6# banyak data
x_input = [0,3,5,8,10,12]
y_input = [70,323.8,445,482.8,370,113.2]
x = 9

hasil = 0
for i in range(n): # 0,1,2,...,n-2,n-1
    perkalian = 1
    for j in range(n):
        if(i != j):
            perkalian = perkalian*(x-x_input[j])/(x_input[i]-x_input[j])
    
    hasil = hasil + y_input[i]*perkalian

print(f"Hasil interpolasi f({x}) = {hasil}")