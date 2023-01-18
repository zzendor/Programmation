"""Ecrire le script nomprenom.py permettant d’entrer le nom puis le prénom de deux
personnes successivement. Le script affichera ensuite sur deux lignes « Prenom NOM » avec
le nom en majuscules et la première lettre du prénom en majuscule et les deux lignes seront
dans l’ordre alphabétique des noms et éventuellement des prénoms en cas de noms
identiques."""

nom = str(input("Votre nom :")) 
prenom = str(input("Votre prenom :"))  

nom1 = str(input("Votre nom :")) 
prenom1 = str(input("Votre prenom :")) 


if nom > nom1 :
    print(str.capitalize(nom1), str.upper(prenom1))
    print(str.capitalize(nom), str.upper(prenom))
else :
    if nom == nom1 and prenom > prenom1 :
        print(str.capitalize(nom1), str.upper(prenom1))
        print(str.capitalize(nom), str.upper(prenom))
    else:
        if nom < nom1 :
            print(str.capitalize(nom), str.upper(prenom))
            print(str.capitalize(nom1), str.upper(prenom1))
        else :
            if nom == nom1 and prenom < prenom1 :
                print(str.capitalize(nom), str.upper(prenom))
                print(str.capitalize(nom1), str.upper(prenom1))

            


