def iteracyjnie(arr, l, r, x):
    while l < r:
        if arr[l] == x:
            return l
        l = l + 1
    return -1


def recSearch(arr, l, r, x):
    if r < l:
        return -1
    if arr[l] == x:
        return l
    if arr[r] == x:
        return r
    return recSearch(arr, l + 1, r - 1, x)


arr = [12, 34, 54, 2, 3]
n = len(arr)
x = 3
index = recSearch(arr, 0, n - 1, x)
if index != -1:
    print("Element", x, "is present at index %d" % index)
else:
    print("Element %d is not present" % x)
index2 = iteracyjnie(arr, 0, n, x)
if index2 != -1:
    print("Element", x, "is present at index %d" % index2)
else:
    print("Element %d is not present" % x)
