#-*-coding:utf-8-*-
#cozum_Algoritması.py
#@auther:Eray Duman

import random
import itertools

hedefSayi= random.randint(100,999)

def birBasamak():
    return random.randint(1,9)

def ikiBasamak():
    return random.randrange(10,99,10)

sayilar=[ikiBasamak()]+[birBasamak() for i in range(5)]
islemler = "+-*/"
sonuc = None

def permutasyon_sayi(sayilar, length):
    return list(itertools.permutations(sayilar, length))

def permutasyon_fonksiyon(length):
    return list(itertools.product(islemler, repeat=length))

for x in range(len(sayilar)):
    perSayi = permutasyon_sayi(sayilar, x+1)
    fonkSayi = permutasyon_fonksiyon(x)

    if x == 0:
        for y in perSayi:
            if y[0] == hedefSayi:
                sonuc = y[0]
                break
        else:
            continue

    for per in perSayi:
        for functions in fonkSayi:
            value = per[0]
            for fonk in enumerate(functions):
                if fonk[1] == "+":
                    value += per[fonk[0]+1]
                elif fonk[1] == "-":
                    value -= per[fonk[0]+1]
                elif fonk[1] == "/":
                    value /= per[fonk[0]+1]
                else:
                    value *= per[fonk[0]+1]

            if value == hedefSayi:
                sonuc = per,functions
                break
        else:
            continue
        break

    if sonuc is not None:
        break
print("Hedef:{0}\nKullanılacak Sayılar{1}\n".format(hedefSayi,sayilar))
print(sonuc)