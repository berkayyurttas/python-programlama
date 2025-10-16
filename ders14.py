# #index() metodu herhangi bir elemanın hangi sırada olduğunu verir
# notlar1=["Eren",100,"İlhan",99,"ali",98,"erman",97,"mehmet",96]


# notlar1[1:9:3]

# notlar1.index("erman")

# #pop()listeden eleman silmek için kullanılır.

# liste=["A","B","C","D","E","F"]
# sil=liste.pop(3)

# #count() herhangi bir elemanın sayısını görüntülemek için.
# ölçüm_degerleri=[1,2,3,4,5,6,7,8,9,4,5,8,7,9,5,6,4]
# ölçüm_degerleri.count(7)


#append() listeye eleman eklemek için.

# liste=[1,2,3,4,10]

# liste.append(12)
# print(liste)


#klavyeden girilen 10 adet değeri bir listeye atama işlemini for ya da while ile yapınız.

# sayilar = []   # Boş bir liste oluşturuyoruz
# i = 0          # Sayaç 0'dan başlıyor

# while i < 10:
#     sayi = int(input(f"{i+1}. sayıyı giriniz: "))  # Kullanıcıdan sayı al
#     sayilar.append(sayi)  # Sayıyı listeye ekle
#     i += 1                # Sayaç 1 artırılır

# print("Girilen sayılar:", sayilar)

#extend() iki listeyi birleştirmek için kullanılır.
# liste1=[1,2,3,4]
# liste2=["bir","iki","üç","dört"]

# liste1.extend(liste2)
# print(liste1)

#del() listeden eleman silmek için kullanılır.
# sayılar=[3,7,15,12]
# del(sayılar[3])
# print(sayılar)

#remove() listeden eleman silmek için kullanılır

# notlar=[100,93,86,78,52,45,95]
# notlar.remove(100)
# print(notlar)

#sorted() liste elemanlarını sıralamak için kullanılır.
# liste=[52,32,15,3,66,8,78,-98,-12,47]
# sorted(liste)
# print (sorted(liste,reverse=True))#büyükten küçüğe doğru

# Liste elemanlarını tersten yazdırmak için .reverse() kullanılır.

# liste.reverse()
# print(liste)

#Liste1 ve liste2 isminde birer boş liste oluşturarak liste1e pozitif 5 tane değer liste 2 ye de negatif 5 tane değer döngü ile atayıp 
#a= liste2 üzerine liste1 i ekle
#b= liste2 nin 4. elemanını siliniz.
#c=birleştirilmiş listeyi büyükten küçüğe sıralayınız.


liste1 = []
liste2 = []

for i in range(5):
    sayilar1 = int(input("Pozitif bir değer giriniz: "))
    sayilar2 = int(input("Negatif bir değer giriniz: "))
    liste1.append(sayilar1)
    liste2.append(sayilar2)

liste2.extend(liste1)  # liste2'nin sonuna liste1 elemanlarını ekler

# İstersen büyükten küçüğe sıralayabilirsin:
liste2.sort(reverse=True)
print("Sıralanmış liste:", liste2)

# Veya 4.elemanı silebilirsin:
liste2.pop(4)
print("4.eleman silindikten sonra:", liste2)
