
vowel=('a','ą','e','ę', 'i', 'y', 'o', 'u','A','E','O','I')
data = "mozeniedokoncaaledziala"


def samogloski(data, vowels):
    start = 0
    idx = 0
    for index in data:
        idx += 1
        if index in vowels:
            yield data[start:idx]
            start=idx

x = samogloski(data, vowel)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

