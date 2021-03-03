tekst = input("Podaj jakiś tekst wariacie: ")
print(tekst.count(" "))

import sys
print("dwie liczby")
s = sys.stdin.readline()
j = sys.stdin.readline() #Wczytuje wierszasd
c=int(s)*int(j)
c=str(c)
sys.stdout.write(c)

#!= == <= >= > <

liczba_1 = int(input("Podaj jakaś cyferke wariacie: "))
if liczba_1<0:
    print(-liczba_1)

liczba_2 = int(input("Podaj jakaś cyferke1 wariacie: "))
liczba_3 = int(input("Podaj jakaś cyferke2 wariacie: "))
liczba_4 = int(input("Podaj jakaś cyferke3 wariacie: "))

if 0 < liczba_2 <= 10:
    if liczba_2>liczby_3 or liczba_3>liczby_4:
        print("To ta liczba")
else:
    print("Nie spełnia warunkow tududu tududu")