########################
#####ZADANIA SE POWTORZ
#####LAB 2 I 3 WSZYSTKIE ZADANIA
####ZAPIERDOL
#####BO TE RZECZY TO CHYBA PRZYDATNE BEDA
#####ZROB WSZYSTKO MORDO, BO TO SROGO
#LAB3-3ZD


""" for x in range (0,50,5):
    print(str(x) + ' ', end='') """




""" lista = input("Dawaj intigery")

lista = lista.split()

for element in lista:
    print(int(element)*int(element)) """


""" lista1 = []
while True:
    i = input("ENTER INT: ")
    lista1.append(i)
    if not i.isnumeric():
        break
    print("YA INPUT: ", i)
print("YA PUT WRONG INPUT") """


""" suma = 0

liczba = int(input("Dawaj incika wariacie: "))
while(liczba!=0):
    ostatnia = liczba%10
    suma += ostatnia
    liczba = round(liczba/10)
print(suma) """


""" p = int(input("Na ile rzedów, chcesz mieć ta wieze hanoi?"))
q=1
for x in range(p):
    for y in range(q):
        print("A", end='')
    print("\n", end='')
    q+=1;
 """


""" w = int(input("Tell em a h8 of ya dejmont 4 x>=3: "))
k=w
c = w//2
idx = 1
while(w>=0):
    if w > ((k//2)+1):
        print(('j'*(c)) + ('w'*(idx)))
        idx += 2
        c-=1
    if w <= (k//2):
        print(('j'*(c)) + ('w'*(idx)))
        idx -= 2
        c+=1
    w=w-1
 """

""" for x in range(1,11,1):
    for y in range(1, 11,1):
        print(x,"*",y,"=", x*y)
 """

""" A=[1 / x for x in range(1,11)]
B=[2 ** i for i in range(1, 10)]
C=[x for x in B if x % 4 == 0]

print(A)
print(B)
print(C) """


""" import random 
c = []
e = []
n=4
d = [[random.randint(-10, 10) for x in range(n)] for x in range(n)]

#c = [[element for element in row] for row in d]
''' for x in range(len(d)):
    c.append(d[x][x])
 '''
 """


items = {"jajka": "szt",
"pomarancze": "szt",
"arbuz": "kg",
"ziemniaki": "kg",
"wodka": "szt",
"borwar": "szt",
"chleb": "szt",
"makaron": "kg"}



print(nowaLista)