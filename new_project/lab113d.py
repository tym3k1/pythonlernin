import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np



def zad1():
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    t = np.linspace(0 , 2 * np.pi, 100)
    z = t
    x = np.sin(z)
    y = 2*(np.cos(z))
    ax.plot(x, y, z, label = 'zadanie 1')
    ax.legend()
    plt.show()



def randrange(n, vmin, vmax):
    '''
    Funkcja wspomagająca może tworzyć macierz losowych liczb o
    kształcie(n, )
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

def zad2():
    np.random.seed( 19680801 )
    fig = plt.figure()
    ax = fig.add_subplot(111 , projection = '3d')
    n = 100
    for c, m, zlow, zhigh in [('r', 'o', -55, -45), ( 'm', '^', -44, -35), ('b', '.', -34, -25)
    ,('c', '.', -24, -15),('y', '1', -14, -5)]:
        xs = randrange(n, 23, 32)
        ys = randrange(n, 0, 100)
        zs = randrange(n, zlow, zhigh)
        ax.scatter(xs, ys, zs, c=c, marker=m)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()

def zad3():
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    # generuj dane.
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)
    # rysuj powierzchnię.
    surf = ax.plot_surface(X, Y, Z, cmap =cm.terrain,
    linewidth = 0 , antialiased = False)
    ax.set_zlim(-1.01 , 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    # Dodanie paska kolorów.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

def zad4():
    fig = plt.figure(figsize=(8, 3))
    ax1 = fig.add_subplot(121, projection = '3d')
    ax2 = fig.add_subplot(122, projection = '3d')
    # fikcyjne dane
    _x = np.arange(4)
    _y = np.arange(5)
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    top = x + y
    bottom = np.zeros_like(top)
    width = depth = 1
    ax1.bar3d(x, y, bottom, width, depth, top, shade = True )
    ax1.set_title('Wykres zacieniony')
    ax2.bar3d(x, y, bottom, width, depth, top, shade = False )
    ax2.set_title('Wykres nie zacieniony')
    plt.show()

def zad5():
    # szerokość 2 razy większa niż wysokość
    fig = plt.figure(figsize =plt.figaspect(0.5))
    #===============
    # Pierwszy wykres
    #===============
    # osie dla pierwszego wykresu
    ax = fig.add_subplot(1, 2, 1, projection = '3d')
    # generuj dane.
    X = np.arange(-5, 5, 0.1)
    Y = np.arange(-5, 5, 0.1)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)
    # rysuj powierzchnię.
    surf = ax.plot_surface(X, Y, Z, cmap =cm.coolwarm,
    linewidth = 0 , antialiased = True)
    ax.set_zlim(-1.01 , 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    # Dodanie paska kolorów.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    #===============
    # Drugi wykres
    #===============
    ax = fig.add_subplot(1, 2, 2, projection = '3d')
    # generuj dane.
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)
    # rysuj powierzchnię.
    surf = ax.plot_surface(X, Y, Z, cmap =cm.coolwarm,
    linewidth = 0 , antialiased = False)
    ax.set_zlim(-1.01 , 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    # Dodanie paska kolorów.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

zad5()
