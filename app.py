import streamlit as st
from calcul import ajouter

st.title("🧮 Ma super calculatrice automatisée")
st.write("Bienvenue sur mon application déployée en CI/CD !")

# Formulaire pour la calculatrice
a = st.number_input("Entrez le premier nombre", value=0)
b = st.number_input("Entrez le deuxième nombre", value=0)

if st.button("Calculer l'addition"):
    resultat = ajouter(a, b)
    st.success(f"Le résultat est : {resultat}")