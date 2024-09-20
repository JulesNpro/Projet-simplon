import pandas as pd
from werkzeug.security import generate_password_hash 
from werkzeug.security import check_password_hash
import getpass

hashed_password = 'scrypt:32768:8:1$F3XsEFqOikiQr56T$614e64d91b7bcc6802eafdba3e7d00a0187f9c45273621bb838da53943245c5a071d4624495895eede3877c2a4e84955314ba0efaede927a8ec7c7a0a73917b1'

admin = {
    'username': ['admin', ],
    'password': [('scrypt:32768:8:1$F3XsEFqOikiQr56T$614e64d91b7bcc6802eafdba3e7d00a0187f9c45273621bb838da53943245c5a071d4624495895eede3877c2a4e84955314ba0efaede927a8ec7c7a0a73917b1'), 
                 ]
}

admin_df = pd.DataFrame(admin) 

data = {
    'nom_utilisateur': ['alice', 'bob', 'charlie'],
    'mot_de_passe': [hashed_password, hashed_password, hashed_password],
    'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com'],
    'nombre_logins': [10, 5, 15]  # Données fictives pour visualisation
}

# connexion

def connexion() :
    df_username = 'admin'
    username =  input("Nom d'utilisateur : " )
    password =  input("mot de passe: " )
    # password =  getpass.getpass("mot de passe: " )

    if username == df_username and admin_df['username'][0] :
        a = admin_df['password'][0]
        verif = check_password_hash(a,password)
        print(verif)
        if verif : 
            print("Success :D")
            return True
    
connexion()



