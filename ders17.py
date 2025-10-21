from math import sqrt

sonDeger = int(input("Hangi sayıya kadar asal sayılar listelensin? "))

deger = 2  # En küçük asal sayı
while deger <= sonDeger:
    kontrol = True  # Başlangıç aşamasında kontrol değişkeni True olarak belirlenir
    geciciDeger = 2
    kok = sqrt(deger)  # Döngüde sırası gelen değerin karekökü hesaplanıyor

    while geciciDeger <= kok:
        if deger % geciciDeger == 0:
            kontrol = False  # Asal sayı özelliği yitiriliyor
            break  # Kontrol döngüsünden çıkılıyor
        geciciDeger += 1  # Bir sonraki kontrol sayısına geçiş

    if kontrol:
        print(deger, end=" ")  # Şarta uyan değer asal olarak kabul edilip yazdırılıyor

    deger += 1  # Asal sayı kontrolü için sonraki sayıya geçiliyor

print()  # Cursor bir sonraki satıra alınıyor