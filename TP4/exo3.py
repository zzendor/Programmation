
nMax = int(input("taille max du vecteurs ")) 
v1 = []
v2 = []

n = int(input("Quelle est la taille de vos vecteurs  ? "))

while n < 1 or n > nMax:
    print("La taille doit être comprise entre 1 et", nMax)
    n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))

print("Saisie du premier vecteur :")
for i in range(n):
    v1.append(int(input("v1[{}] = ".format(i))))

print("Saisie du second vecteur :")
for i in range(n):
    v2.append(int(input("v2[{}] = ".format(i))))


scalaire = 0
for i in range(n):
    scalaire += v1[i] * v2[i]


print("Le produit scalaire de v1 et v2 est :", scalaire)




