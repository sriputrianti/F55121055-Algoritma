def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Contoh penggunaan
array = [15, 99, 75, 12, 22, 55, 95]
sorted_array = bubble_sort(array)
print("Array setelah diurutkan:")
print(sorted_array)
