# Demande à l'utilisateur de saisir le nombre de minutes écoulées
minutes_ecoulees = int(input("Entrez le nombre de minutes écoulées depuis le début du mois: "))

# Calcule le jour du mois en utilisant les minutes écoulées
jour = (minutes_ecoulees // (24 * 60)) + 1

# Affiche le résultat
print("Le jour du mois est: ", jour)