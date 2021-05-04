#SERIE DANYCH
#RAMKA DANYCH

import pandas as pd
import numpy as np

import xlrd
import openpyxl

xlsx = pd.ExcelFile('new_project/imiona.xlsx')
dataframe = pd.read_excel(xlsx)
print(dataframe)
#2-1
print(dataframe[dataframe['Liczba']>1000])
#2-2
print(dataframe[dataframe['Imie']=='TYMOTEUSZ'])
#2-3
print(dataframe.agg({'Liczba':['sum']}))
#2-4
datka = dataframe.groupby(['Rok']).agg({'Liczba':['sum']})
datka=datka[:6]
print(datka)
#2-5
print(dataframe.groupby(['Plec']).agg({'Liczba':['sum']}))
#2-6
nowadat = dataframe.groupby(['Rok', 'Plec']).head(1)
print(dataframe.groupby(['Rok', 'Plec']).head(1))
#2-7
nownow = nowadat.groupby(['Imie']).agg({'Liczba':['sum']})
nownow=nownow[1:3]
print(nownow)