T = input("Entrez une chaîne de caractères : ")

#on calcul la taille de la chaine sans length
taille = 0
for i in T:
    taille += 1

#c'est le pourcnetage de voyelles
voyelles = "aeiouyAEIOUY"
nb_voyelles = 0
for c in T[:taille]:
    if c in voyelles:
        nb_voyelles += 1
pourcentage_voyelles = nb_voyelles / taille * 100

print("il y a ",pourcentage_voyelles, "pourcent de voyelle")

#recherche de la première occurence de wagon
sous_chaine = "wagon"
l_sous_chaine = 0
for i in sous_chaine:
    l_sous_chaine += 1

indice_occurence = -1

for i in range(taille - l_sous_chaine + 1):
    if T[i:i+l_sous_chaine] == sous_chaine:
        indice_occurence = i
        break
if indice_occurence != -1:
    print(f"La sous-chaîne '{sous_chaine}' a été trouvée à l'indice {indice_occurence}.")
else:
    print(f"La sous-chaîne '{sous_chaine}' n'a pas été trouvée.")

#ici c'est le nombre d'occurences de wagon.
nombre_occurrences = 0
i = 0


for i in range(taille - l_sous_chaine + 1):
    if T[i:i+l_sous_chaine] == sous_chaine:
        nombre_occurrences += 1
print(f"La sous-chaîne '{sous_chaine}' est présente {nombre_occurrences} fois dans la chaîne.")