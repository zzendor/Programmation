from random import *
from math import *
#Exercice 1
x=int(input("Valeur de x"))
y=int(input("Valeur de y"))

print("Avant permutation")
print("x:", x)
print("y:", y)


tmp = x
x=y
y=tmp
print("Après permutation")
print("x:", x)
print("y:", y)
