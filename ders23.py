#bir liste ile gönderilen sayılar toplamını parametre alan geriyede değer döndürmeyen şekliyle yap.-50 ile +50 arasında 10 adet sayı üretmek
#boş liste olcak

import random
def liste_topla(sayilar):
    toplam= sum(sayilar)
    print("Listedeki sayıların toplamı: ",toplam)
liste1= []

for i in range(10):
    sayi=random.randint(-50,+50)
    liste1.append(sayi)

print("Oluşturulan liste: ",liste1)
liste_topla(liste1)
