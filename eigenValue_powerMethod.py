def vectorNorm(v: list) -> float:
    s = 0
    for u in v:
        s += u*u
    return s**(1/2)


def matrixMul(A, v):
    m = len(A)
    n = len(A[0])

    result = [0 for i in range(m)]

    for i in range(m):
        for j in range(n):
            result[i] += A[i][j] * v[j]

    return result

def Transpose(A):
    m = len(A)
    n = len(A[0])
    B = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            B[j][i] = A[i][j]
    return B


A = [[1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]]

ukuranVektor = 4

e = 100
ed = 0.1/100

# vektor awal
v = [0 for i in range(ukuranVektor)]
v[0] = 1

v0_size = vectorNorm(v)
v = [u/v0_size for u in v]

k = 0
eigenValue = []

while e > ed:
    k += 1

    w = matrixMul(A, v)

    w_norm = vectorNorm(w)
    v_new = [u / w_norm for u in w]

    Av = matrixMul(A, v_new)
    lam = 0
    for i in range(ukuranVektor):
        lam += v_new[i] * Av[i]

    eigenValue.append(lam)

    if k >= 2:
        e = abs(eigenValue[-1] - eigenValue[-2])
    v = v_new

# hasil
print(f"Eigenvalue terbesar = {eigenValue[-1]}")
print(f"Eigenvector = {v}")
print(f"Iterasi = {k}")
