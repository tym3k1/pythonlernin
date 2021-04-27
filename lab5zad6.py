''' """ class Wspak:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

kotlet = Wspak("kajak")
print(kotlet.__next__())
print(kotlet.__next__())
print(kotlet.__next__())
print(kotlet.__next__())
print(kotlet.__next__()) """

class Codrugie:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.index:
            self.idx += 2
            return self.data[self.idx-1]
        else:
            raise StopIteration()
        

kotlet = Codrugie("kotlet")

print(kotlet.__next__())
print(kotlet.__next__())
print(kotlet.__next__()) '''