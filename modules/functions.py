import pandas as pd
import csv
from werkzeug.security import generate_password_hash 
from werkzeug.security import check_password_hash
import random
from pathlib import Path
bdd = pd.read_csv("bdd.csv")

FILE_PATH = Path('bdd.csv')
#hashed_password = 'scrypt:32768:8:1$F3XsEFqOikiQr56T$614e64d91b7bcc6802eafdba3e7d00a0187f9c45273621bb838da53943245c5a071d4624495895eede3877c2a4e84955314ba0efaede927a8ec7c7a0a73917b1'
if not FILE_PATH.exists():
    with open("bdd.csv", "w") as csvfile:
            fieldnames = ["username","password","email","nbr_logins"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerow({'username': "admin", 'password': "scrypt:32768:8:1$F3XsEFqOikiQr56T$614e64d91b7bcc6802eafdba3e7d00a0187f9c45273621bb838da53943245c5a071d4624495895eede3877c2a4e84955314ba0efaede927a8ec7c7a0a73917b1", 'email' : "admin@admin.com", 'nbr_logins': 12})


def connexion() :
        df_username = 'admin'
        print("Connection...")
        username =  input("Nom d'utilisateur : " )
        password =  input("mot de passe: " )

        if username == df_username and bdd['username'][0] :
            a = bdd['password'][0]
            verif = check_password_hash(a,password)
            if verif : 
                print("Connexion établie.")
            else:
                print("Mot de passe incorrect.")
                return False
def create():
    print("Création d'un nouvel utilisateur : ")
    username = input("Username : ")
    password = input("Mot de passe : ")
    email = input("Email : ")
    nbr_connection = random.randint(1,100)
    with open("bdd.csv", "a") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = ["username","password","email","nbr_logins"])
        writer.writerow({'username': username, 'password': generate_password_hash(password), 'email' : email, 'nbr_logins': nbr_connection})
    print("Utilisateur : ",username," a bien été ajouté.")
    return True
def read():
    print("----- Base de données -----")
    bdd_df = pd.DataFrame(bdd)
    print(bdd_df.tail())
    return True