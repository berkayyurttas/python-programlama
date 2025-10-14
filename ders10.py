#klavyeden girilen bir sayının while ile yazılan faktöriyel bulma

# sayi = int(input("Bir sayı giriniz: ")) 
# faktoriyel = 1
# i = 1
# while i <= sayi:
#     faktoriyel = faktoriyel * i
#     i += 1  # i değerini artırmazsak döngü sonsuz olur
# print(f"Girilen sayının faktoriyeli: {faktoriyel}")

faktoriyel=1
sayac=1
sayi=int(input("Bir sayi giriniz: "))
while sayac<=sayi:
    faktoriyel*=sayac
    sayac+=1
print(sayi," sayısının faktoriyeli: ",faktoriyel)