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
#valorile standardizate au valori in intervalul - inf: +inf si ca procedeu, standardizarea se foloseste atunvi vand
#modele de analiza a datelor pornesc cu premisa ca datele respecta o distributie normala: ACP, regresiile
df["Salary_std"] = (df["Salary"] - df["Salary"].mean()) / df["Salary"].std()

#normalizarea datelor = aducerea valorilor unei variabile intr-un interval, adesea [0:1]
#normalizarea se face urmarind formula (xi-xmin)/ (xmax - min)
#se intalneste in pratica in retele neuoronale sau in aplicatii cu date de intrare cu domeniu finit de definitie(procesarea de imagini)


#statisctici descriptive
df["Salary"].mean()
df["Salary"].median() #valoarea care imparte setul de date in 2 jumatati egale
df["Salary"].mode() #in romana: modul, valoarea cea mai frecvent intalnita




# dispersia datelor
df["Salary"].std()
df["Salary"].var()

# cum se influenteaza reciproc
df[["Age", "Salary"]].corr()

#daca valoarea e pozitiva: exista o relatie directa intre cele 2 var - daca una creste si cealalta creste, respectiv invers
#daca valoarea e negativa: exista o relatie intre cele 2 var - daca una creste, cealalta scade si invers
#daca valoarea e in jurul lui 0: variabilele sunt independente


df["Salary"].hist(bins= 15, edgecolor="orange")
plt.show()


#merge + groupby
df1=pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Alice", "Bob" , "Carol"]
})


df2=pd.DataFrame({
    "ID":[4,5,6],
    "Name":["Mark", "Eva" , "Ivy"]
})


df3=pd.DataFrame({
    "ID":[1,2,3],
    "Departament":["IT", "HR" , "Finance"]
})


#merge by key
#exemplu de merge folsind o coloana - acest tip de operatie functioneaza doar in cazurile in care valoarea paramtrului
#on exista in ambele data frames ca si variabila(df.columns, nu df.index!!!)
merged= df1.merge(df3, on="ID")
print(merged)

#concatenare
concat = pd.concat([df1, df2])
print(concat)

# merge functioneaza similar cu un join in SQL . Plecam de la ipoteze a 2 DF: df1 si df2,
#iar operatie de merge este de forma: df1.merge(df2)
#inner - randurile comune intre cele 2 DF
#left - toate rnadurile din DF1
#right- toate randurile din DF2
#outer - DF1 si DF2

employees = pd.read_csv('res/employees,csv')
departments = pd.read_csv('res/departments.csv')

#inner join ( merge) - doar randurile pt care avem acelasi DepartamentID
inner = employees.merge(departments, on="DepartamentID", how ="inner")
print(inner)


#felt join ( merge) - toti employees, chiar daca nu avem acelasi DepartamentID
left = employees.merge(departments, on="DepartamentID", how ="left")
print(left)

#right join ( merge) - toti employees, chiar daca nu avem acelasi DepartamentID
right = employees.merge(departments, on="DepartamentID", how ="right")
print(right)


#outer join ( merge) - toate departamentele cu ID din ambele tabele
outer = employees.merge(departments, on="DepartamentID", how ="outer")
print(outer)

#cazuri de merge atunci cand criteriul de merge va fi indexul si nu o coloana anume
tabele_etnii = pd.read_csv('res/Ethnicity.csv', index_col=0)
#nan-replace()

variabile_etnii= list(tabele_etnii.columns)[1:]


#calcul populatie pe etnii la nivel de judet
localitati = pd.read_excel('res/CoduriRomania.xlsx', index_col=0)

t1= tabele_etnii.merge(right=localitati, right_index=True, left_index=True)
print(t1)

g1= t1[variabile_etnii + ["Country"]].groupby(by="County").agg(sum)
print(g1)


#calcul populatie pe etnii la nivel de regiune
judete= pd.read_excel('res/CoduriRomania.xlsx', index_col=0, sheet_name="Judete")
t2= g1.merge(right= judete, right_index= True, left_index= True)
print(t2)

g2 = t2[variabile_etnii + ["Regiune"]].groupby(by="Regiune").agg(sum)
print(g2)

#calcul populatie pe etnii la niovel de macroregiune
regiuni = pd.read_excel('res/CoduriRomania.xlsx',index_col=0, sheet_name="Regiuni")

t3= g2.merge(right= regiuni, right_index= True, left_index=True)
print(t3)

g3= t3.groupby(by="MacroRegiune").agg(sum)
print(g3)



g1.to_csv('res/output_etnii_judet.csv')
g2.to_csv('res/output_etnii_regiuni.csv')
g3.to_csv('res/output_etnii_macroregiuni.csv')

#indici de diversitate


