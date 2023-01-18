print("A--------------------------------------")
#a
L1 = [0]*3
print(L1) # [0, 0, 0]
print(type(L1)) # list
print(id(L1)) # id of the list object


print("B--------------------------------------")
#b


for i in L1:
    print(type(i)) # int
    print(id(i)) # id of the int object

"""On remarque que tous les éléments de la liste ont le même type (int) et le même identifiant,
 ce qui signifie qu'ils sont des références au même objet int (0) stocké en mémoire."""

print("C--------------------------------------")

#c
L1[1] += 1
print(L1) # [0, 1, 0]
print(type(L1)) # list
print(id(L1)) # id of the list object

"""L'id de la liste n'a pas changé car c'est toujours le même objet list en mémoire qui est modifié."""

print("D--------------------------------------")
#d
for i in L1:
    print(type(i)) # int
    print(id(i)) # id of the int object

"""Les identifiants de chaque élément de la liste sont toujours les mêmes,  
e.
"""