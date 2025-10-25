#10 elemanlı bir listeye elemanlar rastgele atanmak isteniyor.
#a)- Lisste elemanlarından 3 tanesini seçip ortalama alıp geriye değer döndürmeyen fonks.


# import random 

# def liste_ortalama(sayilar):
#     secilenler=random.sample(sayilar,3)
   
#     ortalama=sum(secilenler)/len(secilenler)
#     print(f"Seçilen sayılar {secilenler}")
#     print(f"Ortalama {ortalama} ")



# liste=[random.randint(1,100)for i in range(10)]

# print(f"Oluşturulan liste {liste}")
# liste_ortalama(liste)


#b)_ Listeden rastgele tek eleman seçip onun tek ya da çift olup olmadığını bul

# import random
# liste=[random.randint(1,100) for i in range(10)]
# print(f"Oluşturulan liste:{liste}")

# secili_sayi= random.choice(liste)
# print(f"Seçilen sayı {secili_sayi}")
# if secili_sayi%2==0:
#     print(f"seçilen sayı {secili_sayi} çifttir")
# else:
#     print(f"seçilen sayı {secili_sayi} tektir")

#c)- Farklı bir fonksiyonda liste içerisine 5 adet 0-1 arası sayı atayınız. geriye değer döndürmeyen
import random

def liste_doldur():
    liste= []
    for i in range(5):
         liste.append(random.randint(0,1))
    print(f"Oluşturulan liste {liste}")
liste_doldur()