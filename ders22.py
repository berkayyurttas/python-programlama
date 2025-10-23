#klavyeden girilen 3 adet sayıya eşit

#1.sayı karenin kenarı
#1.ve2. satı dikdörtgenin kenarı
#2.sayıyı taban,3.sayı ise üçgenin yükseklik
#Buna göre üçgen,kare,dörtgen isimli fonksiyonlarla alalnları bul
#(geriye değer döndürecek parametre alacak)

import math
def ucgen(b,c):
    alan = b*c/2
    return alan
def kare(a):
    alan = a*a
    return alan
def dikdörtgen(a,b):
    alan = a*b
    return alan
sayi1= int(input("1.kenari giriniz: "))
sayi2= int(input("2.kenari giriniz: "))
sayi3= int(input("3.kenari giriniz: "))

print("üçgen alanı=",ucgen(sayi2,sayi3))
print("karenin alanı=",kare(sayi1))
print("dikdörtgenin alanı=",dikdörtgen(sayi1,sayi2))