# déclaration de la fonction ajouter_elt(lst=[0, 1, 2], elt=3)
def ajouter_elt(lst=[0,1,2], elt=3):
    lst.append(elt)
    return lst



#a
"""Le résultat de l'instruction print(ajouter_elt()) serait [0, 1, 2, 3], car elle rajoute 3 à la liste déjà existente"""

#b
"""Si on répète l'instruction print(ajouter_elt()), on remarque que le résultat est toujours [0, 1, 2, 3],
parce que la liste est fixe et on ne la change pas en fonction du temps"""

#c
def ajouter_carac(ch="abc", elt="d"):
    return ch + elt

#d
"""Le résultat de l'instruction print(ajouter_carac()) est abcd
"""

#e
"""Le résultat de l'instruction print(ajouter_carac()) est abcd car elle rajoute d à la liste déjà existente qui est a,b,c"""