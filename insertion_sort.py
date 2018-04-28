def insertion_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        j = i
        while j > -1:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
    return arr

array1 = [8, 9, 11, 2, 3, 77, 23, 11]
print(insertion_sort(array1))
