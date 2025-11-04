# 10% test- sapt 7/8
# 20% proiect- sapt 13/14- individuale
# 70% EXAMEN- pe calculator
# def do_stuff():
#     x=2(poti returna oricate var vrei in python)
#     y=3
#     return x,y
# a,b=do_stuff()
#
#
# init-> echivalent cu constructor
# self cu this
#
# instantiez un obiect => p=Person
#
# Procedural
#
# OOP - mai multe var in constructor
#
# adnotari- decoratori in python - preia fumctia ta si o face in input
#
# STRUCTURILE DATELOR
# -LISTA un general-purpose, cu [], ex [1,3,5] sau list(1,3,5)
#   ->sa mod obiectele
# -SET elimina duplicatele \
# ->TUPLE la fel ca list, doar ca nu pot mod
#
# { k:v
#   k:v
#
#
# MAP(func, iterable)- ia fiecare elem din lista și aplica o transformare
# REDUCE(func, iterable) - intr-un singur rezulat, ex suma
# sorted(func, iterable) -> sa sortezi
# LAMBDA arguments:expression
#
#
# RESURSE
# use with open(..)as f" -> DE PREFERAT CU ASTA SA LUCRAM
# PYCHRAM SI PYTHON
#
# x[u": if:p]
# u- indice inceput
# if- final
# o- pas
# x[1:len(x)-1 ]  <=> x[1: ]
# x[0: len(x) -2] <=> x[:len(x)-2]
# x[-2: ]
# x[:-2]

# liste
temperaturi =[15,22, -3, 0, 7]
temperaturi =list([15,22, -3, 0, 7])
print("lista:" , temperaturi, type(temperaturi))
print("primul elem: " , temperaturi[0])
print("ultimele 2 elem", temperaturi[-2:])

#tupluri
coordonate= (21,45)
coordonate=tuple ((21,45))
#coordonate[0]= 33


#dictionare
student = {"nume": "Ana", "nota" : 10}
student = dict({"nume": "Ana", "nota" : 10})
print(student["nume "], student.get("nota"))

#seturi
litere = set("analiza datelor")
print(litere)
