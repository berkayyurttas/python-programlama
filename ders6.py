
# for i in range(16):
#     print("{0:3} {1:16}".format(i, 10**i))

# print("{} {} yi seviyor!".format("Ali", "Ayşe"))
# # "Ali Ayşe'yi seviyor!"
# print("{} {} yasında bir {}dur".format("Ahmet","18","futbolcu"))

# #end yan yana yazmayı sağlar
# for i in range(10):
#     print(i, end="")
#     if i ==5:
#         i = 20
#     print("({})".format(i), end=" ")
# print()

# #####################################
# kelime= input("Bir kelime giriniz: ")

# for harf in kelime:
#     print(harf)  #yanyana istiyorsak harf, end=""


#1 ile 100 arasında 3 ve 5e bölünebilen kaç adet sayı vardır
# adet=0
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i)
#         adet+=1
# print(adet)

#50 ve 150 arasında 7 ye tam bölünen veya 5e tam bölünmeyen veya 2 ye tam bölünmeyen sayıların toplamını yazdırınız.

# sum=0
# for i in range(50,150):
#     if i%7==0 or i%5!=0 or i%2!=0:
#         print(i)
#         sum+=i
# print(sum)

#-100 ile +100 arasında 100 dahil değil 2 ve 5 e bölünen kaç adet sayı vardır.

# adet =0
# for i in range(-100,100):
#     if i%2==0 and i%5==0:
#         print(i)
#         adet+=1
# print(adet)