#string veri tipleri

il = "İzmir"
il[0]
il[4]

#title()
#metindeki her kelimenşn ilk harfini yapar

isim="eyüp sabri tuncer"
isim.title()

#upper hepsini büyük yapar

isim.upper()
#lower hepsini küçük yapar
isim2="berkay yurttaş"
isim2.title
#strip boşluk kaldırma
metin = "     python programlama dersi   "
metin.strip()
#split her kelimeyi ayırır
mesaj="Python ile programlama dersi"

# mesaj.split()
print(mesaj.split())

#replace() değişiklik yapmak için.

metin="İstanbul,ankara,izmir,bursa,antalya,konya,adana,gaziantep"
print(metin.replace("İstanbul","Diyarbakır"))

#count() karakter dizisinin kaç kez yer aldığını belirtir
metin="İstanbul,ankara,izmir,bursa,antalya,konya,adana,gaziantep"
print(metin.count("ankara"))

#starswith() metinin bir karakter ile başlayıp başlamadığını bulur

kelime="Türkiye"
print(kelime.startswith("T"))

#find() karakterin sırasını verir. -1 ise yoktur.
kelime="programlama"
print(kelime.find("m"))#6.index


