def insertion_sort(in_array):
    for i in range(1, len(in_array)):
        current_value = in_array[i]
        position = i

        while position > 0 and in_array[position - 1] > current_value:
            in_array[position] = in_array[position - 1]
            position = position - 1

        in_array[position] = current_value


# 5 adet sayıyı kullanıcıdan al
print('5 adet sayı giriniz')
dizi = []
for _ in range(5):
    sayi = int(input())
    dizi.append(sayi)

# Insertion Sort ile sıralama
insertion_sort(dizi)

print("Sıralanmış Dizi:")
print(dizi)
