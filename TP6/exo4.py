import random
"""Fonction generer(nbr, vmin, vmax) pour générer un tableau de 'nbr'
valeurs comprises entre 'vmin' et 'vmax'"""
...
"""Fonction combienInferieur(table, vseuil) pour compter le nombre de
valeurs d'un tableau 'table' inférieures à la valeur 'vseuil'"""
...
def generer(nbr, vmin, vmax):
    return [random.randint(vmin, vmax) for i in range(nbr)]

def combienInferieur(table, vseuil):
    return len([x for x in table if x < vseuil])

""""nb = 100
print(f"Générer {nb} nombres entiers entre 0 et 100")
tab = generer(nb, 0, 100)
tab.sort()
print(tab)
total = combienInferieur(tab, 25)
print(f"Il y en a {total} inférieurs à 25")
"""


nb = int(input("Combien de valeurs voulez-vous générer ? "))
vmin = int(input("Valeur minimale ? "))
vmax = int(input("Valeur maximale ? "))
seuil_input = input("Voulez-vous préciser le seuil ? (O/N) ")
if seuil_input in ["Oui", "O"]:
    seuil = int(input("Préciser le seuil : "))
else:
    seuil = 30

print(f"Générer {nb} nombres entiers entre {vmin} et {vmax}")
tab = generer(nb, vmin, vmax)
tab.sort()
print(tab)
total = combienInferieur(tab, seuil)
print(f"Il y en a {total} inférieurs à {seuil}")