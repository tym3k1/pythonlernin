#AS1/2/3

""" ciung = [x for x in range(101) if x%4==0]

with open('plik.txt', 'w') as file:
    file.write(str(ciung))

with open("plik.txt", "r") as plik:
    for linia in plik:
        print(linia)
 """

""" class NaZakupy:
    
    def __init__(self, nazwa_produktu, ilosc, jednosta_miary, cena_jed):
       self.nazwa_produktu = nazwa_produktu
       self.ilosc = ilosc
       self.jednostka_miary = jednosta_miary
       self.cena_jed = cena_jed
    
    def wyswietl_produkt(self):
        nazwa = self.nazwa_produktu
        ilosc = self.ilosc
        sztuk = self.jednostka_miary
        cena = self.cena_jed
        print("Nazwa produktu: ",nazwa,"\nIlosc produktu: ",ilosc,
        "\nJednostka miary: ",sztuk, "\nCena produktu: ",cena)

    def ile_produktu(self):
        ilosc = self.ilosc
        jednostka_miary = self.jednostka_miary
        return ("Nie rozumiem zadania", ilosc, jednostka_miary)

    def ile_kosztuje(self):
        return (f'{self.nazwa_produktu} kosztuja: {self.ilosc*self.cena_jed} pln')


pierozki = NaZakupy("Pierozki", 10, "kg", 5)  

print(pierozki.wyswietl_produkt())
print(pierozki.ile_produktu())
print(pierozki.ile_kosztuje())
 """

"""class ciagi(object):
        def __init__(self, *args):
            self.wartosc


        def wyswietl_dane():


        def pobierz_elementy():


        def pobierz_parametry():


        def policz_sume():

        def policz_elementy():  """


""" class Slowa:
        def __init__(self, slowo, wyraz):
            self.slowo = slowo
            self.wyraz = wyraz

        def sprawdz_czy_palindrom(self):
            return self.slowo == self.slowo[::-1]

        def sprawdz_czy_metagramy(self):
            wynik = 0
            wyraz = self.wyraz
            slowo = self.slowo
            for x in range(len(slowo)):
                if slowo[x] not in wyraz:
                    wynik += 1
            if wynik == 1:
                return ("Te słowa to metagramy.")
            else:
                return("Jednak nie!")

        def sprawdz_czy_anagramy(self):
            wynik = 0
            wyraz = self.wyraz
            slowo = self.slowo
            for x in range(len(slowo)):
                if slowo[x] not in wyraz:
                    wynik += 1
            if wynik >= 1:
                return ("To nie anagram.")
            else:
                return("To anagram!")

        def wyświetl_wyrazy(self):
            return(f'słowo pierwsze {self.slowo}, drugie {self.wyraz}.')

wyrazy_pierwsze = Slowa("kajak", "kasak")

print(wyrazy_pierwsze.sprawdz_czy_palindrom())
print(wyrazy_pierwsze.sprawdz_czy_metagramy())
print(wyrazy_pierwsze.sprawdz_czy_anagramy())
print(wyrazy_pierwsze.wyświetl_wyrazy()) """

""" class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def idz_w_gore(self, krok):
        self.x = self.x + krok

    def idz_w_dol(self, krok):
        self.x = self.x - krok

    def idz_w_prawo(self, krok):
        self.y = self.y + krok

    def idz_w_lewo(self, krok):
        self.y = self.y - krok

    def pokaz_gdzie_jestes(self):
        return (f'moje współrzędne to X:{self.x}, Y:{self.y}')



        
robotStefan = Robot(10, 22)

print(robotStefan.pokaz_gdzie_jestes())
print(robotStefan.idz_w_dol(3))
print(robotStefan.pokaz_gdzie_jestes())
print(robotStefan.idz_w_gore(12))
print(robotStefan.pokaz_gdzie_jestes())
print(robotStefan.idz_w_prawo(4))
print(robotStefan.pokaz_gdzie_jestes())
print(robotStefan.idz_w_lewo(7))
print(robotStefan.pokaz_gdzie_jestes())


del robotStefan

 
 """
    
