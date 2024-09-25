from modules import functions

functions.connexion()
while True:
        print("Choisir un option : Créer = a, Voir = b, switch user = user, update = update, quitter = exit")
        print("Ton option...")
        x = input()
        if x == "a":
            functions.create()
        if x == "b":
            functions.read()
        if x == "user":
            functions.connexion()
        if x == "update":
            functions.actualiser()
        if x == "exit":
            break
