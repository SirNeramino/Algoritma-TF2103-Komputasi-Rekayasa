# Least squares linear fit (pure Python)
def fit_line(x, y):
    """
    Mengembalikan (m, c) untuk garis y = m*x + c
    x, y: list atau iterable angka, panjang sama >= 2
    """
    n = len(x)
    if n != len(y) or n < 2:
        raise ValueError("x dan y harus sama panjang dan minimal 2 data")
    
    sx = sum(x)
    sy = sum(y)
    sxx = sum(xi*xi for xi in x)
    sxy = sum(xi*yi for xi, yi in zip(x, y))
    
    denom = n * sxx - sx * sx
    if denom == 0:
        raise ValueError("Denominator nol: kemungkinan semua x sama")
    
    m = (n * sxy - sx * sy) / denom
    c = (sy - m * sx) / n
    return m, c

def predict(m, c, x):
    """Prediksi y untuk x tunggal atau iterable x"""
    try:
        # iterable
        return [m*xi + c for xi in x]
    except TypeError:
        # single value
        return m*x + c

def mse(m, c, x, y):
    """Mean squared error dari model pada data"""
    n = len(x)
    errs = [(m*xi + c - yi)**2 for xi, yi in zip(x,y)]
    return sum(errs) / n

# Contoh penggunaan
if __name__ == "__main__":
    x = [0, 1, 2, 3, 4]
    y = [1, 2, 1.8, 3.6, 3.9]
    m, c = fit_line(x, y)
    print("m =", m, "c =", c)
    print("Prediksi untuk x=[5,6]:", predict(m, c, [5,6]))
    print("MSE pada data:", mse(m, c, x, y))
