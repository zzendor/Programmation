L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6, 6, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""

amount = 0

for i in L1:
    counter = L1.count(i)
    if counter > amount:
        amount = counter
        high = i

print(f"Le nombre le plus frequent dans la liste est le : {high} ({amount} x)")

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""


