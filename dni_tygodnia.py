def dzientyg(a):
    my_list = ['poniedzialek', 'wtorek',
    'sroda','czwartek','piatek',
    'sobota', 'niedziela']
    return my_list[a-1]

def kwiecien(a):
    dzien_mies = {1:'czwartek',
    2:'piatek',
    3:'sobota',
    4:'niedziela',
    5:'poniedzialek',
    6:'wtorek',
    7:'sroda',
    8:'czwartek',
    9:'piatek',
    10:'sobota',
    11:'niedziela',
    12:'poniedzialek',
    13:'wtorek',
    14:'sroda',
    15:'czwartek',
    16:'piatek',
    17:'sobota',
    18:'niedziela',
    19:'poniedzialek',
    20:'wtorek',
    21:'sroda',
    22:'czwartek',
    23:'piatek',
    24:'sobota',
    25:'niedziela',
    26:'poniedzialek',
    27:'wtorek',
    28:'sroda',
    29:'czwartek',
    30:'piatek'}
    return dzien_mies.get(a)

