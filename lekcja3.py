#################################################
### INSTRUKCJA ITERACYJNA 4

#range([start], stop[,krok])

for x in range (1, 6, 1):
    print(str(x) + " ")


lista = [3, 4, 6, 12, 1]
for x in lista:
    print(str(x) + " ")

#CIUNG
ciag = range(1, 10000, 1)
ciag = list(ciag)
print(ciag)

for x in range(0, 100, 5):
    print(x)
##########ITERACJACIAGIEMLICZBOWYM
for x in 'range(1, 100, 5)':
    print(str(x) + ' ', end='')

a = int(input("Podaj liczbe ile razy chcesz spotegowac liczby "))
for i in ragne(1, a):
    b = int(input("Podaj liczbe:"))
    print(b*b)



#####################################################


ista = input("Dawaj elementy oddzielone spacja")

lista l= lista.split()

for element in lista:
    print(element)


########### W
########### WHILE Z ELSE

import random
random.seed()
z = random.randint(1, 15)

while( z!= 5):
    print(str(z))
    z = random.randint(1, 15)
else:
    print("Znalazlem pjenc")


####### BREJK
#PAJTON KOMPRACHENSZYNS