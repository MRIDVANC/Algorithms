sayi = 10

# Kullanıcıdan girdi alma:
isim = input("Adınızı girin: ")
print("Merhaba, " + isim)

# Koşullu ifade: Bir koşula bağlı olarak kodun akışını değiştirme
if sayi > 0:
    print("Sayı pozitif.")
elif sayi < 0:
    print("Sayı negatif.")
else:
    print("Sayı sıfır.")

# Döngüler: Belirli bir işlemi tekrarlamak için kullanılır.
for i in range(5):
    print("Döngü döngüde", i, ". kez çalıştı.")

# Liste: Verileri gruplamak için kullanılır.
meyveler = ["elma", "armut", "çilek"]
print("Meyve listesi:", meyveler)

# Fonksiyon tanımlama: Tekrar kullanılabilir işlevler tanımlama
def topla(a, b):
    sonuc = a + b
    return sonuc

# Fonksiyon çağırma ve sonuç alınması
sonuc = topla(3, 4)
print("Toplama sonucu:", sonuc)
