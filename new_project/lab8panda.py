#SERIE DANYCH
#RAMKA DANYCH

import pandas as pd
import numpy as np

import xlrd
import openpyxl

xlsx = pd.ExcelFile('new_project/imiona.xlsx')
dataframe = pd.read_excel(xlsx)
#print(dataframe)
#2-1
#print(dataframe[dataframe['Liczba']>1000])
#2-2
#print(dataframe[dataframe['Imie']=='TYMOTEUSZ'])
#2-3
#print(dataframe.agg({'Liczba':['sum']}))
#2-4
#print(dataframe[((dataframe['Rok']<=2005) & (dataframe['Rok']>=2000))].agg({'Liczba':['sum']}))
#2-5
#print(dataframe.groupby(['Plec']).agg({'Liczba':['sum']}))
#2-6

#print(dataframe.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0))
#2-7

#print(dataframe[dataframe['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'),ascending=False).iloc[0])
#print(dataframe[dataframe['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'),ascending=False).iloc[0])
#print(dataframe.groupby(['Plec', 'Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'), ascending=False).iloc[[0,1]])

df = pd.read_csv('new_project\kotlecik.csv', delimiter=';')
print(df)
# print(df.dtypes)
#3-1
#print(df['Sprzedawca'].unique())
print(set(df['Sprzedawca']))
#3-2
print(df.sort_values('Utarg', ascending=False).head())
#3-3
print(df.groupby(['Sprzedawca']).agg({'idZamowienia':['count']}))
#3-4
print(df.groupby(['Kraj']).size())
#3-5
print(df[(df['Data zamowienia'].str[0:4]=='2005') & (df['Kraj']=='Polska')].agg({'idZamowienia':['count']}))
#3-6
print(df[(df['Data zamowienia'].str[0:4]=='2005')].agg({'Utarg':['mean']}))
#3-7
zamowienia_2004 = df[(df['Data zamowienia'].str[0:4]=='2004')]
zamowienia_2005 = df[(df['Data zamowienia'].str[0:4]=='2005')]

zamowienia_2004.to_csv("zamowienia_2004.csv", index=False)
zamowienia_2005.to_csv("zamowienia_2004.csv",sep='@', index=False)