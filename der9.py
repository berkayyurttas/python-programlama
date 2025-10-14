# sayi=int(input("Lütfen tablo ölçüsü giriniz: "))
# for satir in range(1, sayi+1):
#     for sutun in range(1, sayi+1):
#         deger=satir*sutun
#         print (deger, end=" ")
#     print()

#4*5 lik * kümesi oluşturacak kodu yazınız. iç içe döngü

# satir_sayisi = int(input("Lütfen satır sayısı giriniz: "))
# sutun_sayisi = int(input("Lütfen sütun sayısı giriniz: "))

# for satir in range(satir_sayisi):
#     for sutun in range(sutun_sayisi):
#         print("*", end=" ")
#     print()

#klavyeden girilen sayının faktoriyelini bulan kodu yazınız

sayi= int(input("Bir sayı giriniz: ")) 
fakto=1
for i in range (1, sayi+1):
    fakto=fakto*i
print(fakto)