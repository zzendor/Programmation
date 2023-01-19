nom = input("Entrez le nom de l'étudiant: ")
prenom = input("Entrez le prénom de l'étudiant: ")
math = float(input("Entrez la note en mathématiques: "))
anglais = float(input("Entrez la note en anglais: "))
info = float(input("Entrez la note en informatique: "))
promotion = int(input("Entrez l'année de première inscription à l'IUT: "))
moy = (math + anglais + info) / 3

print("L'étudiant {} {} de la promotion {} a une moyenne de {:.1f}".format(prenom, nom, promotion, moy))