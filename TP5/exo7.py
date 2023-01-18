import os
from datetime import datetime

file1 = input("nom du prmeier fichier: ")
file2 = input("nom du deuxième fichier: ")

file1 = os.path.join(__file__.replace("\exo7.py",""),file1)
file2 =os.path.join(__file__.replace("\exo7.py",""),file2)

if os.path.isfile(file1):
    file1_size = os.path.getsize(file1)
    file1_mod_time = os.path.getmtime(file1)
    file1_mod_time = datetime.fromtimestamp(file1_mod_time)
    print(f"{file1} existe est à {file1_size} bytes. il à était modifier pour la dernière fois le{file1_mod_time}")
else:
    print(f"{file1} n'existe pas")

if os.path.isfile(file2):
    file2_size = os.path.getsize(file2)
    file2_mod_time = os.path.getmtime(file2)
    file2_mod_time = datetime.fromtimestamp(file2_mod_time)
    print(f"{file2} existe est à {file2_size} bytes. il à était modifier pour la dernière fois le{file2_mod_time}")
else:
    print(f"{file2} n'existe pas")

