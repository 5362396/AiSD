def indeks(c):
    if str.islower(c):
        return ord(c)-ord('a')+1
    return ord(c)-ord('A')+27

K = 26*2+2*2+1
shift = [x for x in range(K)]
def init_shifts(w):
    for i in range(K):
        shift[i] = len(w)
    
    for i in range(len(w)):
        shift[indeks(w[i])] = len(w) - i - 1

def booyerMoor(w, t):
    init_shifts(w)
    i = j = len(w)-1

    while j >= 0:
        while t[i] != w[j]:
            x = shift[indeks(t[i])]
            if len(w)-j > x:
                i += len(w)-j
            else:
                i += x
            if i >= len(t):
                return -1
            j = len(w) - 1
        i-=1
        j-=1

    return i+1

print(booyerMoor("rak", "abrakadabra"))

