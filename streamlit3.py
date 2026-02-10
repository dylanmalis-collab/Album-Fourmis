import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import pandas as pd

# Nos données utilisateurs doivent respecter ce format
df = pd.read_csv("https://github.com/dylanmalis-collab/Album-Fourmis/blob/main/compte.csv",sep=';')
lesDonneesDesComptes = {"usernames" : {}}

for index, row in df.iterrows():
    lesDonneesDesComptes['usernames'][row['username']] = {
        'name': row['name'],
        'password': row['password'],  # Assurez-vous que c'est haché !
        'email': row['email'],
        'failed_login_attemps': 0,
        'logged_in': False,
        'role': row['role']}
    
authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)
authenticator.login()

def accueil():
    username = st.session_state["username"]
    with st.sidebar:
          st.title(f"Bienvenue {username} !")
          selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Les Photos de mes fourmis"]
        )
    if selection == "Accueil":
        st.title("Bienvenue sur la page d'accueil !")
    elif selection == "Les Photos de mes fourmis":
        st.title("Bienvenue dans l'album de mes fourmis !")
        col1, col2, col3 = st.columns(3)
        # Contenu de la première colonne : 
        with col1:
            st.header("Formica sanguinea")
            st.image("D:/Utilisateurs/Dylan Malis/Téléchargements/6aeb62c8-5791-4e58-8fb3-a9878a71d8cf.jpg")
            st.image("D:/Utilisateurs/Dylan Malis/Téléchargements/3f4eb70b-f8ad-487b-bb9e-e8c86fb465d6.jpg")
            st.image("D:/Utilisateurs/Dylan Malis/Téléchargements/90493b36-304a-4072-aee3-babb5d20c94d.jpg")

        # Contenu de la deuxième colonne :
        with col2:
            st.header("Camponotus cruentatus")
            st.image("D:/Utilisateurs/Dylan Malis/Téléchargements/0786ea7a-29d9-4f8d-9e9b-f42bf6469532.jpg")

        # Contenu de la troisième colonne : 
        with col3:
            st.header("Lasius umbratus")
            st.image("D:/Utilisateurs/Dylan Malis/Téléchargements/ee5f0094-7ec1-43fa-955f-f19cffd3ec77.jpg")

if st.session_state["authentication_status"]:
  accueil()
  # Le bouton de déconnexion
  authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:

    st.warning('Les champs username et mot de passe doivent être remplie')
