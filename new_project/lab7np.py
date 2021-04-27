import numpy as np
#
a = np.array([20,30,40,50])
b = np.arange(1,5)
print(a*b)
#
d = np.arange(1,10).reshape(3,3)
e = np.arange(11,27).reshape(4,4)
print(d.min(axis=1))
print(d.max(axis=0))
print(e.min(axis=1))
print(e.max(axis=0))
#
print(np.dot(a,b))
#
f = np.linspace(0,np.pi,3)
g = np.arange(1,4)
print(f*g)
h=np.dot(f,g)
print(h.dtype.name)
#
zmiennaa = np.sin(np.arange(1,7).reshape(2,3)*np.pi/180.)
zmiennab = np.cos(np.arange(1,7).reshape(2,3)*np.pi/180.)
print(zmiennaa)
print(zmiennab)
#
def dodmac(a, b):
    c = a+b
    return c

print(dodmac(zmiennaa,zmiennab))
#
nowma = np.arange(1,10).reshape(3,3)

for x in nowma:
    print(x)

for x in nowma.flat:
    print(x)
#
dxd = np.arange(1,82).reshape(9,9)
print(dxd)
""" dzielniki	1, 3, 9, 27, 81 """
#
vek = np.arange(1,13)
vek1 = vek.reshape(3,4)
vek2 = vek.reshape(4,3)
vek3 = vek.reshape(2,6)
print(vek)
print(vek1.flatten())
print(vek2.flatten())
print(vek3.flatten())