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
