def insertion_sort(theSeq):
    n = len(theSeq)
    for i in range(1, n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos - 1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
            theSeq[pos] = value
            print(theSeq)


a = [4, 6, 1, 9, 7]
print("Przed ", a)
insertion_sort(a)
print("Po ", a)