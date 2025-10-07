# klavyeden girilen bir sayıanın pozitif negatif ya da sıfıra eşit olup olmadığını bulunuz.

sayi= int(input("Lütfen bir sayi giriniz: "))

if sayi > 0:
     print("Pozitiftir. ")

else:
     if sayi < 0:
       print("Negatiftir. ")
     else:
        print("Sayi sifira eşittir. ")