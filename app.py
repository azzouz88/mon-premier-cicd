import streamlit as st
from calcul import ajouter, soustraire

st.title("🧮 Ma super calculatrice automatisée")
st.write("Bienvenue sur mon application déployée en CI/CD !")

a = st.number_input("Entrez le premier nombre", value=0)
b = st.number_input("Entrez le deuxième nombre", value=0)

# On crée deux colonnes pour aligner les boutons
col1, col2 = st.columns(2)

with col1:
    if st.button("Calculer l'addition"):
        st.success(f"Le résultat est : {ajouter(a, b)}")

with col2:
    if st.button("Calculer la soustraction"):
        st.info(f"Le résultat est : {soustraire(a, b)}")