# make a max_heap
def max_heapify(arr, n, i):
    largest = i
    xleft = 2 * i + 1
    xright = 2 * i + 2
    if xleft < n and arr[i] < arr[xleft]:
        largest = xleft
    if xright < n and arr[largest] < arr[xright]:
        largest = xright
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        max_heapify(arr, n, i)
    for j in range(n - 1, 0, -1):
        temp = arr[0]
        arr[0] = arr[j]
        arr[j] = temp
        max_heapify(arr, j, 0)
    return arr


array1 = [22, 33, 1, 2, 4, 2, 98, 11, 12, 21, 35, 9]
print(heap_sort(array1))
