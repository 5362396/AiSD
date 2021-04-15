def indeks(c):
    if str.islower(c):
        return ord(c)-ord('a')+1
    return ord(c)-ord('A')+27

p = 33554393
b = 64

def karpRabin(w, t):
    bM_1 = 1
    Hw = 0
    Ht = 0

    for i in range(len(w)):
        Hw = (Hw*b+indeks(w[i]))%p
        Ht = (Ht*b+indeks(t[i]))%p

    for i in range(1, len(w)):
        bM_1 = (bM_1*b)%p

    i = 0
    while Hw != Ht:
        Ht = (Ht+b*p-indeks(t[i])*bM_1)%p
        Ht = (Ht*b+indeks(t[i+len(w)]))%p

        if i>len(t)-len(w):
            return -1
        i+=1

    return i

w = "rak"
t = "abrakadabra"

print(karpRabin(w, t))