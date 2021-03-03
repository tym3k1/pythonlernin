import sys
print("Podaj tekst")
s = sys.stdin.readline()#naciskajac enter, tworzyjmy nju lajn.
#jest to nispokoziomowa technika
print("Twoj tekst to: "+ s)

a = input("Zapierdol wariacie jakieś literki")
b = int(input("Chyba, ze chcesz cyferki"))

a.isnumeric() #czy jest konwertowalna

print('Wonsz zeczny', end='\n')
print('jest niebezieczny')

#INSTRUKCJA WARUNKOW
if warunek_1:
    instrukcja
elif warunek_2:
    instrukcjab
else:
    instrukcjac

if liczba < 5 and liczba > 0:

if 0 < liczba < 5: