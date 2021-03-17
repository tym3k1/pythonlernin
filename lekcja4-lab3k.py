""" def nazwa_funkcji(arg_pozycyjny, arg_domyslny=wartosc, *arg_4, **arg_nieokilosc):
    instrukcje
    ...
    [return values] #occjonalnie """

import math as m

#from matma import * // jako maly skrypy
#from matma import dodaj """

""" def funkc_lin(a, b):
    if a>0: return ('rosnaca')
    if a<0: return ('malejaca')
    if a==0: return ('stala')

print(funkc_lin(5, 2)) """
""" 
def funkc_spr(x1, y1, x2, y2):
    if x1==x2:
        return ('wnolegle')
    elif x1*x2==-1:
        return ('prstpdl')
    else:
        return ('idk') """

""" def fnc_okr(a=1,b=1):
    r=a*a+b*b
    return m.sqrt(r)*2

print(fnc_okr(3,2))
 """

""" def pitagoras(a, b):
     c = a*a+b*b
     return m.sqrt(c)

print(pitagoras(3,4)) """

""" def ciung_aryt(a1= 1, ile=11, r=1):
    suma = 0
    for x in range(a1,ile,r):
        suma += x
    return suma

print(ciung_aryt())
     """

""" def ciag(* liczby):
    # jeżeli nie ma argumentów to
    if len(liczby) == 0:
        return 0.0
    else:
        suma = 0.0
    # sumujemy elementy ciągu
    for i in liczby:
        suma *= i
    # zwracamy wartość sumy
    return suma """

""" def zakupy(** rzeczy):
    suma = 0
    for cos in rzeczy:
        suma = suma + rzeczy[cos]
    return suma
        

print(zakupy(slodycze=7, rozrywka=7))
 """

import dni_tygodnia
""" 
print(dni_tygodnia.dzientyg(1))


 """

print(dni_tygodnia.kwiecien(12))