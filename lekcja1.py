import random

liczba = random.randint(0, 10)

for i in range(3):
    odp = input("Podaj liczbe od 0 do 10: ")
    odp = int(odp)

    if odp == liczba:
        print("Zgadles.")
    elif odp > liczba:
        print("Liczba jest mnijesza.")
    else:
        print("Liczba jest większa.")
