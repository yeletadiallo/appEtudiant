import streamlit as st

# Titre de l'application
st.title('Calculatrice de Somme')

# Créer un formulaire
with st.form(key='sum_form'):
    # Entrer les trois valeurs
    val1 = st.number_input('Valeur 1', value=0)
    val2 = st.number_input('Valeur 2', value=0)
    val3 = st.number_input('Valeur 3', value=0)
    
    # Soumettre le formulaire
    submit_button = st.form_submit_button('Calculer la Somme')

    if submit_button:
        # Calculer la somme des valeurs
        total = val1 + val2 + val3
        # Afficher la somme
        st.write(f'La somme des valeurs est : {total}')