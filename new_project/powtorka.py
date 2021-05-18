import numpy as np

# zadanie 1
def zad1():
    return np.arange(2,20*2+1,2)

def zad6():
    # wyrazy jako wektory znaków (liter)
    malina = np.array(list('malina'))
    lizak = np.array(list('lizak'))
    jagoda = np.array(list('jagoda'))

    # przygotowanie "pustej" tablicy 6x6 wypełnionej pustym stringiem
    wykreslanka = np.zeros((6, 6), dtype=str)
    # lub
    wykreslanka = np.empty((6, 6), dtype='str')
    # lub tak
    # wykreslanka = np.full((6,6),"",dtype='str')
    # można też bardziej "na piechotę"

    # teraz np. za pomocą wycinków (slice) możemy nie tylko zwracać
    # określone fragmenty macierzy, ale wstawiać tam wartości
    # należy pamiętać, że rozmiar wycinka musi być taki sam jak
    # rozmiar danych, które chcemy tam umieścić
    wykreslanka[:, 0] = malina
    wykreslanka[2,:5] = lizak
    wykreslanka[5,::-1] = jagoda
    # za pomocą np.put możemy również wstawiać dane do macierzy określając zbiór indeksów
    # na których odpowiadające wartości stawianego wektora mają się znaleźć
    # ale tutaj numeracja indeksów jest "globalna" gdzie indeks 0 to wiersz 0 i kolumna 0
    # a kolejne numery są naliczane do prawej strony np.
    # 0  1  2  3
    # 4  5  6  7
    # 8  9 10 11 itd.
    # np.put(wykreslanka, [ 0, 6, 12, 18, 24, 30 ], wyraz1)
    # np.put(wykreslanka, range(12, 17), wyraz2)
    print(wykreslanka)


# zadanie 7
def zad7(n):
    mat = np.diag([2 for _ in range(n)])
    for indeks in range(1, n):
        vec = [2+(2*indeks) for _ in range(n-indeks)]
        mat += np.diag(vec, indeks)
        mat += np.diag(vec, -indeks)
    print(mat)


zad7(6)
