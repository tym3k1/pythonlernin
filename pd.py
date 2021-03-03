import math 

def throot(num, root):
    ans = num**(1/root)
    return ans

print(math.exp(10))
print(math.floor(3.55))
print(math.ceil(4.80))
print(throot((math.log((5+(math.pow(math.sin(8),2))))),6))

imie = "TYMOTEUSZ"
nazwisko = "LUCZKO"

print(imie.capitalize(), nazwisko.capitalize())


tekst = """La la, la la la la la na na na na na,
La la na na, la la la la la na na na na na
La la, la la la la la na na na na na,
La la na na, la la la la la na na na na na"""

print(tekst.count("na"))
print(nazwisko[1],nazwisko[-1])