import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random 

def zad1():
    x = np.arange(1, 21, 1)
    y = np.linspace(0,1,20)
    plt.plot( 1/x, y, label='liniowa')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend('1/x = x')
    plt.show()

def zad2():
    x = np.arange(1, 21, 1)
    y = np.linspace(0,1,20)
    plt.plot( 1/x, y, 'g^:' ,label='liniowa')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend('1/x = x')
    plt.show()

def zad3():
    x = np.arange(0, 31, 0.1)
    s = np.sin(x)
    c = np.cos(x)
    plt.plot(x, s, 'g:' ,label='sin(x)')
    plt.plot(x, c, 'r-', label='sin(x)')
    plt.legend()
    plt.show()

def zad4():
    x = np.arange(0, 31, 0.1)
    s = np.sin(x)
    c = np.sin(x)
    plt.plot(x, s+2 ,label='sin(x)')
    plt.plot(x, -c, 'y-', label='sin(x)')
    plt.legend()
    plt.show()

def zad5():
    df = pd.read_csv('iris.data', delimiter=',', header=None)
    data = df
    d = np.abs(data[0]-data[1]) * 100
    c = np.random.randint(0, data[0], 150)
    df.plot.scatter(0, 1, s=d, c=c)
    plt.xlabel('wartość a')
    plt.ylabel('wartość b')
    plt.show()


def zad6():
    xlsx = pd.ExcelFile('new_project/imiona.xlsx')
    dataframe = pd.read_excel(xlsx)
    etykiety = ['K', 'M']
    grouped = dataframe.groupby('Plec').agg({'Liczba': ['sum']}).unstack()
    plt.subplot(324)
    plt.bar(etykiety, grouped)
    plt.xticks(rotation=45)
    plt.ylabel('Ilość narodzin mln')
    plt.xlabel('Płeć')
    plt.subplot(321)
    lolxd = dataframe[dataframe['Plec'] == 'K'].groupby(['Rok']).agg({'Liczba': ['sum']})
    lolxd2 = dataframe[dataframe['Plec'] == 'M'].groupby(['Rok']).agg({'Liczba': ['sum']})
    plt.plot(lolxd, 'm',label='dziewuszka')
    plt.plot(lolxd2, label='opiec')
    plt.subplot(325)
    etykie = range(0,18)
    data = dataframe.groupby(['Rok']).agg({'Liczba': ['sum']}).unstack()
    plt.bar(etykie, data)
    plt.show()
    


def zad7():
    xlsx = pd.ExcelFile('new_project/imiona.xlsx')
    dataframe = pd.read_excel(xlsx)
    wtfmate = range(18)
    lolxd = dataframe[dataframe['Plec'] == 'K'].groupby(['Rok']).agg({'Liczba': ['sum']}).squeeze()
    lolxd2 = dataframe[dataframe['Plec'] == 'M'].groupby(['Rok']).agg({'Liczba': ['sum']}).squeeze()
    plt.bar(wtfmate, lolxd)
    plt.bar(wtfmate, lolxd2, label='opiec', bottom=lolxd)
    plt.show()


def rzucaj(n):
        list1 = []
        for x in range(n):
            rzut = random.randint(1,6)
            list1.append(rzut)
        vect = pd.Series(list1)
        return vect




def zad8():
    x = rzucaj(6)
    print(x)
    plt.hist(x, bins=6, facecolor='g')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()

    
def zad9():
    df = pd.read_csv('new_project\kotlecik.csv', delimiter=';')
    zawodnicy = df['Sprzedawca'].unique()
    newdata = df.groupby(['Sprzedawca']).agg({'Utarg':['sum']}).squeeze()
    wedges, texts, autotexts = plt.pie(newdata, labels=zawodnicy,
                                   autopct=lambda pct: "{:.1f}%".format(pct), textprops=dict(color="black"))
    plt.setp(autotexts, size=14, weight="bold")
    plt.title("Hoa hoa hoa")
    plt.show()


def zad10():
    xlsx = pd.ExcelFile('new_project/imiona.xlsx')
    dataframe = pd.read_excel(xlsx)
    wtfmate = range(18)
    lolxd = dataframe[dataframe['Plec'] == 'K'].groupby(['Rok']).agg({'Liczba': ['sum']}).squeeze()
    lolxd2 = dataframe[dataframe['Plec'] == 'M'].groupby(['Rok']).agg({'Liczba': ['sum']}).squeeze()
    plt.bar(wtfmate, lolxd)
    plt.bar(wtfmate, lolxd2, label='opiec', bottom=lolxd)
    plt.annotate("DWUTYSIECZNY DZIESIATY",(10,200),(0.5,25), arrowprops={"width":10})
    plt.show()


zad8()