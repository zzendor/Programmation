"""Ecrire un programme permettant de lire une valeur entière représentant une somme d’argent et
de décomposer cette somme en billets de 100, 50, 10 et en pièces de 2 et 1, en utilisant à chaque
fois la plus grande valeur pour chaque type de billet ou pièce. Afficher le résultat de cette
décomposition à l’écran."""

moneyinit = int(input("Entrez une somme d'agent : "))
money = moneyinit
b = []

b.append(int(money / 100))
money = money % 100

b.append(int(money / 50))
money = money % 50

b.append(int(money / 10))
money = money % 10

b.append(int(money / 2))
money = money % 2

b.append(money)
money = money % 1

print(f"{moneyinit} euros, c'est donc {b[0]} billet(s) de 100, {b[1]} de 50, {b[2]} de 10, {b[3]} pièce(s) de 2 et {b[1]} pièce(s) de 1.")