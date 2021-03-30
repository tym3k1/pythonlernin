plik = open(nazwa, [tryb[,bufor]])
#tryb atrybut as w r a r+ w+ a+
#read(10) 10 char
#readline() oneline
#readlines() all


plik = open("tekst.txt","r")

wiersze = plik.readlines()

plik.close


import sys

dane =  sys.stdin.readline() #input ale inaczej

plaik = open("data.txt", "w+")

plik.write(dane)

plik.close()





with open("dane.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")
