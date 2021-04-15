def silnia_r(n):
    if (n == 0):
        return 1
    else:
        return n * silnia_r(n - 1)


def silnia_i(n):
    liczba = 1
    for i in range(1, n + 1):
        liczba = liczba * i
    return liczba


def silnia_ogonowa(n, akumulator=1):
    if (n == 0):
        return akumulator
    else:
        return silnia_ogonowa(n - 1, akumulator * n)


def silnia(n):
    return silnia_ogonowa(n, 1)


print(silnia_r(10))
print(silnia_r(0))
print(silnia_i(10))
print(silnia_i(0))
print(silnia_ogonowa(10))
print(silnia(0))
