def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Dizi oluşturma
dizi = [64, 25, 12, 22, 11]

# Selection Sort ile sıralama
selection_sort(dizi)

# Sıralanmış diziyi yazdırma
print("Sıralanmış dizi:", dizi)
