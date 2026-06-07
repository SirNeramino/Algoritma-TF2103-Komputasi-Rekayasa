def vectorNorm(v: list) -> float:
    s = 0
    for u in v:
        s += u*u
    return s**(1/2)


def matrixMul(A, v):
    m = len(A)
    n = len(A[0])

    result = [0 for _ in range(m)]

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


def gaussSolve(A, b):
    n = len(A)

    # buat copy agar A dan b tidak berubah
    M = [row[:] for row in A]
    B = b[:]

    # eliminasi maju
    for k in range(n):
        pivot = M[k][k]
        if pivot == 0:
            raise ValueError("Pivot nol, sistem gagal.")

        # normalisasi baris k
        for j in range(k, n):
            M[k][j] /= pivot
        B[k] /= pivot

        # eliminasi baris bawah
        for i in range(k+1, n):
            faktor = M[i][k]
            for j in range(k, n):
                M[i][j] -= faktor * M[k][j]
            B[i] -= faktor * B[k]

    # substitusi mundur
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = B[i]
        for j in range(i+1, n):
            x[i] -= M[i][j] * x[j]

    return x


A = [
    [4,1,0,0],
    [1,3,1,0],
    [0,1,2,1],
    [0,0,1,1]
]

ukuranVektor = 4

e = 100
ed = 0.1/100   # toleransi

v = [0 for i in range(ukuranVektor)]
v[0] = 1

v_norm = vectorNorm(v)
v = [u/v_norm for u in v]


k = 0
eigenValue = []

while e > ed:
    k += 1

    w = gaussSolve(A, v)

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


print(f"Eigenvalue terkecil = {eigenValue[-1]}")
print(f"Eigenvector = {v}")
print(f"Iterasi = {k}")
