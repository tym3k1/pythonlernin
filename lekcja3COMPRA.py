### JAK NAJKROCEJ NAPISAC POLECENIE
slownik = {1: 'jeden', 2:'dwa'}
zbior = {1, 2, 3}
krotka = (1, 'jeden')
lista = [1, 2, 3, 4]

for klucz in slownik:
    print(slownik[klucz])

for klucz in slownik.items():
    print(klucz)
    print(type(klucz))####krotka

for klucz, wartosc in slownik.items():
    print(klucz)
    print(wartosc)


#################################################

listaa = ['poniedzialek', 'wtorek', 'sroda']

indeks = 1

for dzien in lista:
    print(f'{indeks} dzien tygodnia to {dzien}')
    indeks+=1


for para in enumerate(lista, start=1):
    print(f'{para[0]} dzien tygodnia to {para[1]}')


###########PRACA DOMOWA*$(*&$@*$@($&))




