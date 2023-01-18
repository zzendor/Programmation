notes = []
nombreEtudiants = int(input("Donnez le nombre d'etudiants : ")) 
for i in range(nombreEtudiants):
    note = int(input(f"note pour l'étudiant {i + 1} : "))
    if note < 0:
        print("les notes négative ne sont pas permisent")
    elif note > 20:
        print("les notes au dessus de 20 ne sont pas permisent")
    else:
        notes.append(note)


moyenne = sum(notes)/ len(notes)
print(f"la moyenne de la classe est {moyenne}")

for i in range(nombreEtudiants):
    print(f"{i+1} | {notes[i]} | {notes[i] - moyenne}")

