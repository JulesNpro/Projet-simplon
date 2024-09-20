from modules import functions

functions.connexion()
while functions.connexion():
        print("Choisir un option : Créer = a, Voir = b, Quitter = exit")
        print("Ton option...")
        x = input()
        if x == "a":
            functions.create()
        if x == "b":
            functions.read()
        if x == "exit":
            break
