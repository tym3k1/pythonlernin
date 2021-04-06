""" class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj 
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        return f'nazwa materialu: {self.rodzaj}'


class Ubrania(Material):
    def __init__(self, rozmiar, kolor, dla_kogoo):
        self.rozmiar = rozmiar 
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        return f'Co?{self} Rozmiar?{self.rozmiar} Kolor?{self.kolor} Plec?{self.dla_kogo}'


class Sweter(Ubrania):
    self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_dane(self):
        return f'Co?{self.rodzaj_swetra} Rozmiar?{self.rozmiar} Kolor?{self.kolor} Plec?{self.dla_kogo}'

bawelna = Material("Bawelna", 10, 10)
kardigan = Ubrania()


         """

""" 
class Ksztalty:
    # definicja konstruktora
    def __init__(self, x, y):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


class Kwadrat(Ksztalty):
    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self, kwadrat):
        if isinstance(kwadrat, Kwadrat):
            return self.x + kwadrat.x

    def __ge__(self, kwadrat):
        if self.x < kwadrat.x:
            return "first object smaller than other"
        else:
            return "first object not smaller than other"

    def __gt__(self, kwadrat):
        if self.x < kwadrat.x:
            return "first object smaller than other"
        else:
            return "first object not smaller than other"

    def __le__(self, kwadrat):
        if self.x > kwadrat.x:
            return "first object smaller than other"
        else:
            return "first object not smaller than other"

    def __lt__(self, kwadrat):
        if self.x > kwadrat.x:
            return "first object smaller than other"
        else:
            return "first object not smaller than other"



    
kw = Kwadrat(5)
kw1 = Kwadrat(22)
print(kw > kw1)
print(kw >= kw1)
print(kw < kw1)
print(kw <= kw1)
 """


""" class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstruktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(0,0)
p2 = Point(1,1)
p3 = Point(2,1)
p4 = Point(1,2)
p5 = Point(2,2)
p6 = Point(3,3)

print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
p1.update(1)
print(p1.counter)
print(p2.counter)
p4.counter = p1.counter
print(p4.counter)
print(p4.counter == p1.counter)
p3.update(1)
print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
p3.update(1)
print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
p1.counter = []
print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter) """




