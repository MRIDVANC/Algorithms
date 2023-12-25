karma = [9, 5, 6, 8, 47, 2, 3, -1, 24, 7, -6, 8, 5, 1, 34, -5]

n = len(karma)


def insertionSort():
    for i in range(1, n):
        key = karma[i]
        j = i - 1
        while j >= 0 and karma[j] > key:
            karma[j + 1] = karma[j]
            j = j - 1
        karma[j + 1] = key
    return karma


insertionSort()
print(karma)
