#Özel fonksiyonlarda lambda
#lambda tek satırda bir fonksiyon oluşturma
#etiket=lambda parametre1,parametre2.....:işlem

# toplama=lambda x,y,z: x+y+z
# print(toplama(3,4,5))

# ikikati=lambda x:x*2
# print(ikikati(3))

# çifttek=lambda sayi: sayi%2==0
# print(çifttek(14))
# #AYNI İŞE YARIYOR
# def çifttek(sayi):
#     if sayi%2==0:
#         return True
#     else:
#         return False
# print(çifttek(10))

#map fonksiyonu (liste,tuple....),...) ()==tuple
#gonderilen fonksiyonu her bir eleman üzerine uygular.

# def kat_al(x):
#     return x*2
# list(map(kat_al,[1,2,3,4,5]))

# list(map(lambda x:x**2,(1,2,3,4,5,6,7)))

# liste1=[1,2,3]
# liste2=[4,5,6]
# liste3=[7,8,9]

# print(list(map(lambda x,y,z:x*y*z,liste1,liste2,liste3)))

