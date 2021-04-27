import numpy as np

m = np.array([np.arange(2,41,2)])
#print(m)


d = np.arange(1,10,0.5)
#print(d)
b = d.astype('float')
#print(b)

def arrayek(n):
    x = np.arange(n**2)
    x = x.reshape((n, n))
    return x

def zad4(p, n):
    x = np.logspace(1, 4, n, base=p).astype(int)
    return x

def zad5(n):
    x = np.arange(n,0,-1)
    x_diag = np.diag(x)
    return x_diag

#6

""" #def zad7():
    x = np.diag([2,2,2])
    x1 = np.diag([4,4], 1)
    x2 = np.diag([4,4], -1)
    x3 = np.diag([6], 2)
    x4 = np.diag([6],-2)
    return x+x1+x2+x3+x4 """



def zad7(n):
    x = np.diag([mat_diag])
    return x;
    
#mat_diag = np.array([a for a in range(4)])

    



#zad9 

def fib(a, b):
    x = [0, 1]
    for i in range(a * b - 2):
        x.append(sum(x[-2:]))
    return np.array(x).reshape((a,b))


#zad8
def dzi(np.dot(a, b)):
    a = np.dot(a, b)
    return a;


x=fib(5,5)
print(dzi(fib))