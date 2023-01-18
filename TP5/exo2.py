"""Ecrivez le programme Notes.py qui demande à l’utilisateur de rentrer 5 valeurs de type
réel représentant les notes finales avec 5 valeurs de type entier représentant les coefficients de
chacune des notes. Votre programme doit permettre la récupération de ces valeurs comme
dans l’exemple suivant :"""

notes = []
coefficients = []

for i in range(5):
    note_coeff = input(f"Veuillez entrer la note du module {i+1} et le coefficient correspondant : ")
    note, coeff = note_coeff.split(" ")
    notes.append(float(note))
    coefficients.append(int(coeff))

moyenne = sum([notes[i] * coefficients[i] for i in range(5)]) / sum(coefficients)

if moyenne > 10 and all(note >= 8 for note in notes):
    print("Admis avec une moyenne de", moyenne)
else:
    print("Refusé avec une moyenne de", moyenne)