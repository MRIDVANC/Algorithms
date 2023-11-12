def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


# Kullanıcıdan bir liste alalım
sayilar = input("Sıralanacak sayıları boşluk bırakarak girin: ")
sayi_listesi = list(map(int, sayilar.split()))

# Quick sort uygula
siralanmis_liste = quick_sort(sayi_listesi)

# Sonucu göster
print("Sıralanmış liste:", siralanmis_liste)
