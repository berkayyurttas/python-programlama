#öz yinelemeli recursive fonksiyon
#kendiniçağıran fonksiyon

# def faktoriyel(n):
#     if n==0:
#         return 1
#     else:
#         return n*faktoriyel(n-1)
# print("faktoriyel 5!",faktoriyel(5))

#random modülü
#random.random: 0-1 arasında rastgele noktalı sayılar üretir.

# import random
# x=random.random()
# print(x)

#randint(): tam sayı üretmek istediğimizde kullanılır.

# import random
# x=random.randint(1,50)
# print(x)

#choice listeden veri seçer.tek eleman
# import random
# liste=["ali","veli","ahmet","ayşe","elif"]
# print(random.choice(liste))

#randrange(), randint gibi tek farklı başlangıç bitiş değeri yazamamak
# import random
# print(random.randrange(10))
# print(random.randint(1,10))

#sample(): listeden örnek almaya yarar.
# import random
# liste2=[1,56,45,-98,100,85,10,3]
# print(random.sample(liste2,3))
