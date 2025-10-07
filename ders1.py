# klavyeden girilen bir sayıanın pozitif negatif ya da sıfıra eşit olup olmadığını bulunuz.

# sayi= int(input("Lütfen bir sayi giriniz: "))

# if sayi > 0:
#     print("Pozitiftir. ")

# else:
#     if sayi < 0:
#       print("Negatiftir. ")

#     else:
#       print("Sayi sifira eşittir. ")


#2- Klavyeden girilen bir sayının tek ya da çift olup olmadığını bulup ekrana yazdıran program


# sayi = int(input("Lütfen bir sayi giriniz: "))

# if sayi % 2 == 0:
#     print(" Sayi çift sayidir. ")

# else:
#     print(" Sayi tek sayidir. ")


# deger =int(input("Lütfen 0-5 arasında bir değer giriniz: "))
# cevap = "aralıkta degil"
# if deger ==0:
#     cevap = "Sıfır"
# elif deger ==1:
#     cevap = "Bir"
# elif deger ==2:
#     cevap = "İki"
# elif deger ==3:
#     cevap = "Üç"
# elif deger ==4:
#     cevap = "Dört"
# elif deger ==5:
#     cevap =="Beş"

# print("Girdiğiniz sayı",cevap)


# klavyeden girilen bir sayıanın pozitif negatif ya da sıfıra eşit olup olmadığını bulunuz.

# sayi = int(input("Klavyeden bir sayi giriniz: "))
  
# if sayi > 0:
#     print("Girdiğiniz sayi pozitiftir: ")
# elif sayi < 0:
#     print("Girdiğiniz sayi negatiftir: ")  
# else:
#     print("Girilen sayi sifira eşittir")     ,


#Klavyeden vize ve final notu girilen bir öğrencinin geçtiği harf notunu ekrana yazdıran program ort= vize *0.5+ final*0.5

vize =int(input("kalvyeden vize notunu giriniz: "))
final =int(input("Klavyeden final notunu giriniz: "))

ortalama = (vize * 0.5) + (final * 0.5)
print("Ortalama",ortalama)

if ortalama>=90 and ortalama<=100:
    print("Harf notu, AA")
elif ortalama>=80 and ortalama<=90:
    print("Harf notu, BA")
elif ortalama>=70 and ortalama<=80:
    print("Harf notu, BB")
elif ortalama>=60 and ortalama<=70:
    print("Harf notu, CB")
elif ortalama>=50 and ortalama<=60:
    print("Harf notu, CC")
elif ortalama>=40 and ortalama<=50:
    print("Harf notu, DC")
elif ortalama>=30 and ortalama<=40:
    print("Harf notu, DD")
elif ortalama>=20 and ortalama<=30:
    print("Harf notu, FD")
else: 
    print("Harf notu, FF (Kaldınız)")