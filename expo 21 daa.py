def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half = n // 2

    high1, low1 = divmod(x, 10**half)
    high2, low2 = divmod(y, 10**half)

    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    return (z2 * 10**(2 * half)) + ((z1 - z2 - z0) * 10**half) + z0

print("Karatsuba Result:", karatsuba(1234, 5678))
