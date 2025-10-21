#klavyeden kısa ve uzun kenarı girilen dikdörtgenin alan isminde bir fonksiyon kullanılarak parametre alan geriye değer döndürmeyen 
#şekliyle gerekli programı yazınız.
def alan (x,y):
    alan=x*y
    print(alan)
x=int(input("kısa kenarı giriniz: "))
y=int(input("uzun kenarı giriniz: "))
alan(x,y)
print(alan)