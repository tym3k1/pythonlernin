print('{:10}'.format('wonsz'))
print('{:_<10}'.format('żeczny'))
print('{:^10}'.format('jest'))
print('{:^15}'.format('niebezpieczny'))

lorem = """"Wonsz żeczny Tududu tududu Jest niebezpieczny 
Tududu tududu Jak cię chapnął Tududu tududu
 Żeczny Wonsz Tududu tududu 
 To ci zadek Tududu tududu 
 Puchnie wciąż Tududu tududu 
 Raz mnie taki Tududu tududu 
 Wonszyk użar Tududu tududu 
 Pupa mi u- Tududu tududu -rosła 
 duża Tududu tududu Teraz siedzieć
  tududu tududu Muszę wciąż Tududu 
  tududu Bo mnie użar Tududu tudud
  u Żeczny Wonsz
"""

ilosc_W = lorem.count('W')
ilosc_s = lorem.count('s')
print(f"w tekscie jest tyle s: {ilosc_s} tyle W: {ilosc_W}")