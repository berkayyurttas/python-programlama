# #yan yana
# kelime = input("Bir kelime giriniz: ")
# for harf in kelime:
#     print(harf,end=" ")

#klavyeden girilen bir cümlenin içerisindeki sesli harflerin adetini bulan prograsmı for döngüsü ile yaz NOT: GİRİLEN CÜMLENİN bütün harfleri küçük ve büyükolacaktır.

kelime=input("Bir cümle giriniz: ")
sesli_harf_sayisi=0
  
for c in kelime:
    if c =="A" or c =="a" or c=="e"\
    or c=="I" or c=="ı" or c=="i"\
    or c== "O" or c=="o" or c=="Ö"\
    or c== "U" or c=="u" or c=="ü":
       print(c, ",", end=" ")
       sesli_harf_sayisi+=1
print(sesli_harf_sayisi, "sesli")
    