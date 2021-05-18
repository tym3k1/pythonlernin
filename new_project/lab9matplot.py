import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import xlrd
import openpyxl

xlsx = pd.ExcelFile('new_project/imiona.xlsx')
dataframe = pd.read_excel(xlsx)


def zad1():
    imionka = dataframe.groupby(['Rok']).agg({'Liczba':['sum']})
    imionka.plot()
    plt.show()
    
def zad2():
    plec = dataframe.groupby(['Plec']).agg({'Liczba':['sum']})
    wykres = plec.plot.bar()
    wykres.set_ylabel('Ilosc')
    plt.title('Urodzenia dzieci 00-17 plec')
    plt.show()

def zad3():
    ostatnie_piec = dataframe[dataframe['Rok'] >= 2013].groupby(['Plec']).agg({'Liczba': ['sum']})
    kolko = ostatnie_piec.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(7,7))
    plt.title('Dzieci ale chyba nie tak')
    plt.show()

""" 
irisone = df[df['class']=='Iris-setosa']
    iristwo = df[df['class']=='Iris-versicolor']
    iristhree = df[df['class']=='Iris-virginica']
    irisone.plot(kind="scatter", x="SL", y="SW")
    iristwo.plot(kind="scatter", x="SL", y="SW")
    iristhree.plot(kind="scatter", x="SL", y="SW") """


def zad4():
    df = pd.read_csv('new_project\iris.csv', delimiter=',', names=['SL','SW','PL','PW','class'])
    colors = {'Iris-setosa': 'red', 'Iris-versicolor': 'blue', 'Iris-virginica': 'green'}
    scatter_col = [colors[i] for i in df['class']]
    plt.scatter(df['SL'], df['SW'],c=scatter_col)
    plt.title("sepal width & sepal length")
    plt.show()



def zad5():
    df = pd.read_csv('new_project\kotlecik.csv', delimiter=';')
    newdata = df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']})
    wykres = newdata.plot.bar()
    wykres.set_ylabel('Ilosc zamowien')
    wykres.set_xlabel('Sprzedawcy')
    plt.title('Ilosc zamowien xD')
    plt.show()

#zad5()
#zad4()
#zad3()
#zad2()
#zad1()
