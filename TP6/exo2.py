#fonction
def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

#a

lst1 = [0, 1, 2]

#b
lst2 = ajouter_elt(lst1, len(lst1))

#c

print(lst1) # [0, 1, 2, 3]
print(type(lst1)) # list
print(id(lst1)) # id of the list object
print("-------------------------------------")
print(lst2) # [0, 1, 2, 3]
print(type(lst2)) # list
print(id(lst2)) # id of the list object

"""Ils sont le même type (list)  et le même id"""