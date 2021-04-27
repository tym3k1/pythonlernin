''' import numpy as np


a = np.arange(2)
print(a)
print(type(a))

lista = [[1,2,3],[4,5,6]]
print(lista)
a = np.arange(6)
a = a.reshape((2,3))
print(a) '''

import numpy as np

''' zera = np.zeros((5,5), dtype='int64')
print(zera.dtype)
print(zera[1,1]) '''

''' z = np.indices((5,3))
print(z)
print(z.ndim)
print(z.shape)

x,y=np.mgrid[0:5, 0:5]
print(y)
print(x) '''

A = np.arange(1, 26).reshape((5, 5))

print(A)
