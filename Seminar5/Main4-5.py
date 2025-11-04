# spider chart si area chart SA LE LASAM ULTIMELE PT EXXAMEN PT CA TEORETIC NU AR INTRA
# descarcam folderul res si dupa adaugam main, oprin debug cu print()- >L e un gandac si in console
#
# Asta e codul din main:

from unittest.mock import inplace #??? cred ca ar trebui sters asta - Da

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#pandas = biblioteca pt procesarea datelor tabelare(randuri si coloane)
#pandas pune la dispozitie 2 obiecte:
#1. Series = date unidimensionale ( coloane din csv)
#2. DataFrame= date bidimensionale( foaia de calcul)

s= pd.Series([10, 20, 30] , index = ['a', 'b', 'c'])

df= pd.DataFrame({
    'Name':['Alice', 'Bob', 'Carol'],
    'Age':[25, 27, 29],
    'Salary': [3000, 4500, 6000]
})


df = pd.read_csv('res/employees.csv', index_col=0)  #a cat colaoan este din index


#proprietati pe df
print("df head\n",df.head())#primele 5 randuri din df
print("df tail\n",df.tail()) #ultimele 5 randuri din df
print("df info\n", df.info()) #informatii despre structura df: tipuri de date, valori null
print("df describe\n",df.describe()) # statistici descriptive despre colaane
print("df shape", df.shape ) #(rows, cols)
print("df columns",df.columns) # lista cu coloanele din df
print("df index", df.index) #lista dcu referintele randurilor din df


#accesul datelor
#citirea- se realizeaza folosind operatorul de indexare []
#citirea pe coloane
ages = df["Age"]
coloane= ["Name", "Salary"]
subset= df[coloane]
#echivalent : df[coloane] = df["Name", "Salary"]]

#citire pe randuri in fc de index | iloc = index location
fr= df.iloc[0] # primul rand
ftr= df.iloc[0:3] # primele 3 randuri

#citire in fc de label/eticheta |loc
l1= df.loc["Alice"] #strict !!!! in cazul acesta 1 se refera la eticheta 1, la stringul 1 din coloana ID
l2= df.loc[1:3, ["Name", "Salary"]]

#loc si iloc
#cand citim randuri iloc, nu stim indicele folosim eticheta


#filtare boolean
f1 = df[df["Ages"]> 30]
f2 = df[(df["Salary"]> 6000) & (df["Ages"]< 40 )]

# modificari in df
# adaugarea unei coloane noi
df["TaxedSalary"] = df["Salary"] * 0.9

df.rename(columns={"Salary": "GrossSalary"}, inplace=True) # true se aplcuia pe setul de date
df.rename(columns={"GrossSalary": "Salary"}, inplace=True)

df.drop(columns=["TaxedSalary"], inplace=True)
df.drop(index=[1], inplace=True ) # drop randului care are ID  1

#data sanitization / curatarea datelor


# in general avem de a face cu una din urm situatii:
# - operam cu date numerice
# - operam cu date categorice
#cand vrei sa faci data sanitization ai 2 abordari: fie faci drop randurilor/coloanelor cu valori lipsa ,
#fie le inlocuiesti cu valori convenabil alese
#- date numerice: media pe coloana sau o valoare utila in scenariul respectiv
# - date categorice : modulul( valoarea cea mai frecvent intalnita) sau o valoarea utila in scenariul respectiv

#depistarea valorilor lipsa
missing = df.insa().sum()

#drop
df.dropna() # drop fiecarui rand care contine NaN
df.dropna(axis=1) # drop fiecarei coloane care contine NaN
# 0 se refera la randuri si 1 la coloane


#replace
df.fillna(0)
sbst= df["Salary"].mean()
df["Salary"].fillna(df["Salary"].mean(), inplace=True)


#transformari
#vectorizate
df["AgeInMonths"]= df["Age"]* 12

#lambda si aply

df["IncomeBracket"]= df["Salary"].apply(lambda  x : "High" if x> 6000 else "Low")

# functii string
df["Name"] = df["Name"].str.upper()


#statisctici
#centrare = repozitionarea setului de date i  jurul unei valori referinta ( valoarea care va sta in c..)
df["Salary_centered"] = df["Salary"] - df["Salary"].mean()
#scalare = aducerea termenilor la acelasi de marime

#standardizare = centrare + scalare
df["Salary_std"] = (df["Salary"] - df["Salary"].mean()) / df["Salary"].std()

