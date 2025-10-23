#rastgele seçilen iki adet sayıdan büyük olanı bulan,parametre alan geri döndürmeyen fonksiyonu yazınız,
#fonksiyonadi=en büyük

import random
def enbuyuk(x,y):
    if a>b:
        print("a={} büyüktür b={} den.".format(a,b))
    elif a==b:
        print("iki değer eşittir.")
    else:
        print("b={} büyüktür a={} dan.".format(b,a))
a=random.randint(1,100)
b=random.randint(1,100)
enbuyuk(a,b)