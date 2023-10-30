def insertion_sort(in_array):
    for i in range(1, len(in_array)):
        current_value = in_array[i]
        position = i

        while position > 0 and in_array[position - 1] > current_value:
            in_array[position] = in_array[position - 1]
            position = position - 1

        in_array[position] = current_value

# Kullanıcıdan kaç adet sayı almak istediğini sor
num_of_numbers = int(input("Kaç adet sayı gireceksiniz: "))

dizi = []
for _ in range(num_of_numbers):
    try:
        sayi = int(input("Sayıyı giriniz: "))
        dizi.append(sayi)
    except ValueError:
        print("Hatalı giriş. Sayı harici bir karakter girdiniz. Sayı girişine devam ediliyor.")

# Insertion Sort ile sıralama
insertion_sort(dizi)

print("Sıralanmış Dizi:")
print(dizi)
