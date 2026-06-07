x_input = [0,3,5,8,10,12]
y_input = [70,323.8,445,482.8,370,113.2]
n = 6 # banyak data
m = 3 # orde
x = 9

def g(i,j):
    if i - j == 1: # base case
        return (y_input[i]-y_input[j])/(x_input[i]-x_input[j])
    elif i - j > 1: # recursive case
        return (g(i,j+1)-g(i-1,j))/(x_input[i]-x_input[j])

hasil = y_input[0]
print(f"{hasil}, ",end="")
for i in range(1,m+1): # 1,2,3,..,n-2,n-1
    perkalian = g(i,0)
    print(f"{perkalian}, ",end="")
    for j in range(0,i): # 0,1,2,..,i-2,i-1
        perkalian = perkalian*(x-x_input[j])
    hasil = hasil + perkalian


print(f"Hasil interpolasi f({x}) = {hasil}")