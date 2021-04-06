#isinstance() oraz issubclass()

class Osoba:
    
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik:

    def __init__(self, pensja):
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Osoba, Pracownik):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        Pracownik.__init__(self, pensja)

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


adrian = Menadzer("Adrian", "Mikulski", 12000)
print(adrian.przedstaw_sie())

x = isinstance(adrian, Osoba)
y = isinstance(adrian, Pracownik)
z = isinstance(adrian, Menadzer)

s = issubclass(Menadzer, Pracownik)
p = issubclass(Pracownik, Osoba)
u = issubclass(Menadzer, Osoba)

print(x,y,z,s,p,u)