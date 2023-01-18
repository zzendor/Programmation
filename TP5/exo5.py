"""Ecrire un programme permettant de calculer le salaire d’un ouvrier en fournissant le nombre
d’heures travaillées et le salaire horaire"""

def calculer_salaire(heures_travaillees, salaire_horaire):
    if heures_travaillees <= 160:
        return heures_travaillees * salaire_horaire
    elif heures_travaillees <= 200:
        return 160 * salaire_horaire + (heures_travaillees - 160) * salaire_horaire * 1.25
    else:
        return 160 * salaire_horaire + 40 * salaire_horaire * 1.25 + (heures_travaillees - 200) * salaire_horaire * 1.5


print(calculer_salaire(180, 10))


