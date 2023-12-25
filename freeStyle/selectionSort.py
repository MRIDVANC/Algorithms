karma = [9, 5, 6, 8, 47, 2, 3, -1, 24, 7, -6, 8, 5, 1, 34, -5]


def selectionSort():
    n = len(karma)
    for i in range(n):
        minIndex = i
        for j in range(i+1,n):
            if karma[j] < karma[minIndex]:
                minIndex = j

        karma[i], karma[minIndex] = karma[minIndex], karma[i]

    return karma

selectionSort()

print(karma)