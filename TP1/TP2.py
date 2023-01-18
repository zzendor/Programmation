from random import *
from math import *
#Exercice 1
x=int(input("Valeur de x"))
y=int(input("Valeur de y"))

tmp = x
x=y
y=tmp

print(x,y)

#exercice 2

age = int(input("Age"))
age_utilisateur = 2022 - age 
print(" Votre anée de naissance est",age_utilisateur)

#Exercice 3

a = int(input("Valeur 1"))
b = int(input("Valeur 2"))
c = int(input("Valeur 3"))

tmp1 = a
tmp2 = b
tmp3 = c

a=tmp2
b=tmp3
c=tmp1

print(a,b,c)

#Exercice 4

BASE = 4
fromage = 800
eau = 2
ail = 2
pain = 400

convive = int(input("Nombre de convive"))
fromage = (800 * convive)/BASE
eau = (2* convive)/BASE
ail = (2* convive)/BASE
pain = (400* convive)/BASE

print("pour",convive,"personne il faut ",fromage,"g de fromage",eau,"litre d'eau",ail,"gousse d'ail",pain,"gramme de pain")

#Exercice 5 


x = int(input("Chiffre"))
if x == 0:
    print(x ,"est nul" )
else :
    if x>0 and x%2 == 0:
        print(x , "est postive est pair")
    else :
        if x>0 and x%2 != 0:
            print(x , "est postive est impair")
        else :
            if x<0 and x%2 == 0:
                print(x , "est negatif est pair")
            else:
                print(x , "est negatif est impair")


 

#Exercice 6

pièce=randint(0,100)
print(pièce)
if pièce < 50 :
    print('Pile')
else :
    print('Face')

#Exercice 7

total1 = 0
total2 = 0
for i in range(1000):
    piece_fake = random()<0.66
    False
    print(piece_fake)
    if piece_fake == True:
        total1 = total1 + 1
    else:
        total2 = total2 + 1

print(total1,total2)

#Exercice 8

x= float(input("Chiffre"))
if x > 2.3:
    print(" NON")
else:
    if x == 0.1:
        print("oui")
    else :
        if x <= -2 and x >= -10 :
            print("oui")
        else :
            x <-10
            print("non")

  




    