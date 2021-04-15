def szukaj(w, t):
    i = 0
    j = 0

    while j < len(w) and i < len(t):
        if w[j] != t[i]:
            i -= j
            j = -1
        i+=1
        j+=1

    if j == len(w):
        return i-len(w)
    return -1

t = "abrakadabra"
w = "rak"
print(szukaj(w, t))