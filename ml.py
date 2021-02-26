import random  


try:
    ileliczb = int(input("Podaj ilość liczb:"))
    maksymalnaliczba = int(input("Podaj maksymalna wartosc:"))
    print("Wytypuj %s z %s liczb: " % (ileliczb, maksymalnaliczba))
except ValueError:
    print("Bledne dane!")
    exit()

if ileliczb > maxymalnaliczba:
    exit()

liczby = []
i = 0
while i < ileliczb:
    liczba = random.randint(0, maksymalnaliczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1

typy = set()
i = 0
while i < ileliczb:
    try:
        typ = int(input("Podaj liczbe %s " % (i + 1)))
    except ValueError:
        print("Bledne dane!")
        exit()

    if 0 < typ <= maksymalnaliczba and typ not in typy:
        typy.add(typ)
        i = i + 1

trafione = set(liczby) & typy
if trafione:
    print("\nIlosc trafien: %s" % len(trafione))
    print("Trafione liczby: ", trafione)
else:
    print("Brak trafien. Sprobuj jeszcze raz!")

print(typy)
print(liczby)

