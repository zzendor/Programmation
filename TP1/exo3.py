# Demande à l'utilisateur de saisir les valeurs
jour = int(input("Entrez le jour du mois: "))
heure = int(input("Entrez l'heure (entre 0 et 23): "))
minute = int(input("Entrez les minutes (entre 0 et 59): "))

# Calcule le nombre de minutes écoulées depuis le début du mois
minutes_ecoulees = (jour - 1) * 24 * 60 + heure * 60 + minute

# Affiche le résultat
print("Le nombre de minutes écoulées depuis le début du mois est: ", minutes_ecoulees)
