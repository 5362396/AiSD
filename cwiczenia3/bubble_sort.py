def bubble_sort(theSeq):
    n = len(theSeq)
    for i in range(n - 1):
        for j in range(0,  n - 1):
            if theSeq[j] > theSeq[j + 1]:
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                print(theSeq)


a = [4, 6, 1, 9, 7]
print("Przed ", a)
bubble_sort(a)
print("Po ", a)