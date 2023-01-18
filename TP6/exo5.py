import re
import unicodedata

def clean_text(text):
    # Enlever les accents
    text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    # Enlever les caractères spéciaux, les espaces et les signes de ponctuation
    text = re.sub(r'[^A-Za-z0-9]+', '', text)
    return text.lower()

def is_palindrome(text):
    cleaned_text = clean_text(text)
    return cleaned_text == cleaned_text[::-1]

chain = input("Entrez une chaine de caractères : ")
if is_palindrome(chain):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome !")