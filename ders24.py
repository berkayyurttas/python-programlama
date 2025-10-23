#rastgele elemanları atanan listeye ait(-50,+50) listeElemanOrt ile ortalamasını, listeElemanEnbüyük
#ile enbüyük, ikiBolünen fonksiyon ile 2ye bölünen elemanların sayısını veren fonksiyonları p.a ve g.d.d şekliyle yazdır
import random

# 1️⃣ Ortalamayı bulan fonksiyon
def listeElemanOrt(liste):
    return sum(liste) / len(liste)

# 2️⃣ En büyük elemanı bulan fonksiyon
def listeElemanEnbuyuk(liste):
    return max(liste)

# 3️⃣ 2’ye bölünen eleman sayısını bulan fonksiyon
def ikiBolunen(liste):
    sayac = 0
    for eleman in liste:
        if eleman % 2 == 0:
            sayac += 1
    return sayac

# Boş liste oluştur
liste = []

# -50 ile +50 arasında rastgele 10 sayı ekle
for i in range(10):
    sayi = random.randint(-50, 50)
    liste.append(sayi)

# Listeyi küçükten büyüğe sırala
liste.sort()

# Fonksiyonları çağır
ortalama = listeElemanOrt(liste)
enbuyuk = listeElemanEnbuyuk(liste)
cift_sayi_adedi = ikiBolunen(liste)

# Sonuçları yazdır
print("Sıralanmış liste:", liste)
print("Liste elemanlarının ortalaması:", ortalama)
print("Listenin en büyük elemanı:", enbuyuk)
print("2’ye bölünen sayı adedi:", cift_sayi_adedi)