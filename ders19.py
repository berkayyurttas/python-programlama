#klavyeden girilen 2 adet sayının toplamına ilişkin olarak:
#alan fonksiyon ile gerekli kodları yazınız...
# 2): Parametre:Alan Geriye:Döndürmeyen

def topla (x,y):
    toplam=x+y
    print(toplam)
x=int(input("Toplanılacak ilk sayıyı giriniz: "))
y=int(input("Toplanılacak ikinci sayıyı giriniz: "))
topla(x,y)
print(topla)
#1): parametre alan geriye döndüren

def topla (x,y):
    toplam=x+y
    return toplam
x=int(input("Toplanılacak ilk sayıyı giriniz: "))
y=int(input("Toplanılacak ikinci sayıyı giriniz: "))
print(topla(x,y),"ana menüye gelen sayı")

#3)- parametre almayan geriye değer döndüren
def topla():
    a=12
    b=23
    toplam=a+b
    return toplam
print(topla(),"ana menuye gelen sayı")

#7)-parametre almayan geriye değer döndürmeyen
def topla():
    a=12
    b=23
    toplam=a+b
    print(toplam)