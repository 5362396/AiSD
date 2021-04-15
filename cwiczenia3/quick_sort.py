def partition(array, begin, end):
    pivot = begin
    print("before partitioning", array[begin:end+1])
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
        print("partitioning", array[begin:end+1])
    array[pivot], array[begin] = array[begin], array[pivot]
    print("after partitioning", array[begin:end+1])
    return pivot


def _quicksort(array, begin, end):
    if begin >= end:
        return
    print("array=", array)
    pivot = partition(array, begin, end)
    print("pivot index=", pivot, "array=", array)
    _quicksort(array, begin, pivot-1)
    _quicksort(array, pivot+1, end)


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    return _quicksort(array, begin, end)


a = [4, 6, 1, 9, 7]
print("Przed ", a)
quicksort(a)
print("Po ", a)