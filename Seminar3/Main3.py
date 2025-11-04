# matplotlib color values- PT CULORI SITE
# SEMINAR 2 CONTINUARE:
from functools import reduce
import numpy as np
import time

# comprehensions
numere_pare_p = []
for each in range(20):
    if each % 2 == 0:
        numere_pare_p.append(each ** 2)
        # echivalent:
        # numere_pare = numere_pare + [each]
print(numere_pare_p)

# rezultat echivalent cu blocul de mai sus folosind list comprehenshions
numere_pp = [x ** 2 for x in range(20) if x % 2 == 0]
print(numere_pp)

# dict comprehensions
nume = ["Ana", "Andrei", "Alina"]
note = [10, 9.5, 9]
catalog = {k: v for k, v in zip(nume, note)}
print(catalog, type(catalog),
      catalog.keys(), type(catalog.keys()),
      catalog.values(), type(catalog.values()),
      catalog.items(), type(catalog.items()))

celsius = [10, -5, 0, -3, 22, 17]
# f = 9/5 * c + 32
fahrenheit = [ round(9/5 * c + 32, 1) for c in celsius ]
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)

secventa = (1, 2, 3, 4)
# map(func, iterable)
# [x ** 3 for x in secventa]
result = map(lambda x: x**3, secventa)
print(result, type(result), list(result))

# filter(func, iterable)
result = filter(lambda x: x>=0, celsius)
print(result, type(result), list(result))

note = [3, 7, 10, 5, 7, 2, 4, 9]
promovat = [n for n in note if n >= 5]
status = ["promovat" if n >= 5 else "restant" for n in note]
print("note:", note)
print("promovat:", promovat)
print("status:", status)

emails = ["user@gmail.com", "user@yahoo.com", "user@ase.ro"]
valid_emails = list(
    filter(lambda e: e.endswith("ase.ro"), emails))
print(valid_emails)

# reduce
suma = reduce(lambda a,b: a+b, note)
print(suma, type(suma))
print("Media notelor:", suma / len(note))
print("Media notelor:", sum(note) / len(note))

# numpy
# numpy ofera obiectul de tip ndarray
# care spre deosebire de listele built-in, are reprezentare continua in memorie
# forteaza un tip unic de date si permite operatii de tip SIMD
l1 = [1, 2, True, [6,5], None, "ana"]

a = np.array([1,2,3], dtype='int16')
b = np.array([ [3.2, 6.7], [3.1, 1.5], [5.0, 7.4] ])
print("a: \n", a)
print("b: \n", b)

# proprietati
print("Forma: ", b.shape, a.shape)
print("Numar dimensiuni:", b.ndim, a.ndim)
print("Tip de data:", b.dtype)
print("Dim element in bytes:", b.itemsize)
print("Numar elemente:", b.size)
print("Dimensiune totala:", b.nbytes)

# indexing si slicing

# corectie S1 => in slicing pentru parcurge totala c[0 : len(c)], nu c[0 : len(c)-1]
c = [1, 2, 3, 4, 5]
print(c[0], len(c), c[len(c) - 1]) # indexare
print(c[0: len(c) - 1], c[0: len(c)]) # slicing

a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(a[1,2], a[1][2]) # 8 8
a[1, 2] = 20
print(a[1,2], a[1][2])

print(a[0, 1:-1]) # 2, 3, 4
print(a[0, 1:-1:2]) # 2, 4
print(a[0, ::2]) # 1, 3, 5
print(a[0, :]) # 1,2,3,4,5
print(a[:, 3]) # 4, 9
print(a[:-1, 3]) # 4

#repeat(repeta de n ori fiecare element) vs tile (copy paste cum il stim) \
a = np.array([1,2,3])
print("Tile:", np.tile(a,3));
print("Repeat:", np.repeat(a, 3))

# shawllow vs deep copy
b =a
c= a.copy()

b[0] = 10
c[0]= 20
print("A:", a)
print("B:", b)
print("C:", c)

#performanta
start = time.time()
a = np.arange(1, 1_000_001)   # 1_000_001 <=> la nivel conceptual 1.000.001  <=> 1000001
ap = a ** 2 #il ridicam la patrat
durata = time.time() - start

start_lst = time.time()
lst= [i for i in range(1_000_001)]
lst_p= [i ** 2 for i in lst]
durata_lst = time.time() - start_lst

print("Performance comparison:")
print(f"Numpy: {durata:.5f} | Python: {durata_lst:.5f}" ) #ultimele 5 zecimale

#string
#s1 = ("abc"
      #"def")

#s2 = 'abc\' def'


# broadcasting
# broadcasting simplu - distribui o valoare unui array - inmultirea unei matrice cu un scalar
#broadcasting complex - inmultire elem cu elem intre arrays diferite

a = np.array([
    [1,2,3],
    [4,5,6]
])
print("Broadcast:\n", a * 2)

b= np.array([
    [1,2],
    [3,4]
])
c = np.array([
    [10,20],
    [30,40]
])

print("Element wise:\n" , b*c)
print("Inmultire matematica:\n", b@c )

x = np.array([
    [1,2],
    [3,4],
    [5,6]
])
y= np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

#EXAMNE!!!!!
# @ -> inmultire matematica
# *-> elem cu elem

z = np.array([1,2,3])
print( z * y)