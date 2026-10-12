import numpy as np

x = [1, 2, 3, 4, 5]
y = [4, 5, 6, 8, 12]

m = 5 # jumlah data
n = 2 # derajat polinomial
n = n + 1 # karena mulai dari indeks 0

M = [[0 for j in range(n)] for i in range(m)] # matriks M

for i in range(m):
    for j in range(n):
        M[i][j] = x[i]**j

a = np.linalg.pinv(M) @ y # [a0 a1 a2 .. an-1 an] -> di index 0 itu a0

print(a)

# f(2.5) -> 5.5

sum = 0
for i in range(n):
    sum = sum + a[i]*(2.5)**(i)

print(sum)