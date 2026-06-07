import math

# Fungsi untuk menghitung koefisien Fourier dari data diskrit
def fourier_coefficients(x, y, N):
    """
    Menghitung a0, a_n, b_n untuk pendekatan Fourier orde N.
    x dan y: list data (satu periode)
    N: orde maksimum
    """
    n_points = len(x)
    L = x[-1] - x[0]  # panjang periode
    w0 = 2 * math.pi / L  # frekuensi dasar

    a0 = (2 / n_points) * sum(y) / 2
    a = []
    b = []

    for n in range(1, N + 1):
        an = (2 / n_points) * sum(y[i] * math.cos(n * w0 * x[i]) for i in range(n_points))
        bn = (2 / n_points) * sum(y[i] * math.sin(n * w0 * x[i]) for i in range(n_points))
        a.append(an)
        b.append(bn)
    
    return a0, a, b

# Fungsi untuk menghasilkan nilai pendekatan Fourier di titik x
def fourier_approx(x, a0, a, b, L):
    w0 = 2 * math.pi / L
    N = len(a)
    fx = a0
    for n in range(1, N + 1):
        fx += a[n-1]*math.cos(n*w0*x) + b[n-1]*math.sin(n*w0*x)
    return fx

# Contoh penggunaan
if __name__ == "__main__":
    # Contoh sinyal: f(x) = x pada interval [0, 2π]
    x = [i * 0.1 for i in range(63)]
    y = [xi for xi in x]  # sinyal asli

    N = 5  # orde Fourier
    a0, a, b = fourier_coefficients(x, y, N)

    # Menampilkan hasil
    print("a0 =", a0)
    print("a =", a)
    print("b =", b)

    # Prediksi di titik tertentu
    x_test = math.pi / 2
    y_approx = fourier_approx(x_test, a0, a, b, x[-1] - x[0])
    print(f"Pendekatan Fourier f({x_test:.2f}) ≈ {y_approx:.4f}")
