karma = [9, 5, 6, 8, 47, 2, 3, -1, 24, 7, -6, 8, 5, 1, 34, -5]

n = len(karma)


def bubbleSort():
    for i in range(0, len(karma)):
        for j in range(0, len(karma) - i - 1):
            if karma[j] >= karma[j + 1]:
                karma[j], karma[j + 1] = karma[j + 1], karma[j]
    return karma


bubbleSort()
print("Sorted array: ", karma)
print('Length : ', len(karma))
