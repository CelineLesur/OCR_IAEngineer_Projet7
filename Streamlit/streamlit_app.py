import streamlit as st
import requests
import time
from insight import log_feedback

# Initialiser les états
if 'prediction_done' not in st.session_state:
    st.session_state.prediction_done = False
if 'feedback_given' not in st.session_state:
    st.session_state.feedback_given = False

st.title("Prédiction de sentiment d'un tweet avec ModernBERT")

# Vérification de l'API
response = requests.get("https://webapp-ocr-p7-b2d0cuafdhgyf8fx.canadacentral-01.azurewebsites.net/")  
if response.status_code == 200:
    st.success(f"L'API est fonctionnelle")
else:
    st.error("L'API ne répond pas.")

# Formulaire pour tester un endpoint
user_input = st.text_input("Entrez un texte pour tester l'API:")
if st.button("Envoyer"):
    api_url = "https://webapp-ocr-p7-b2d0cuafdhgyf8fx.canadacentral-01.azurewebsites.net/predict"
    data = {"tweet": user_input}
    res = requests.post(api_url, params=data)

    if res.status_code == 200:
        prediction = res.json().get("prediction")
        prob = res.json().get("probabilité")

        if prediction == 1:
            st.write(f'😊 Positif ({prob}%)')
        else:
            st.write(f'😞 Négatif ({prob}%)')

        st.session_state.prediction_done = True
        st.session_state.feedback_given = False  # Réinitialiser le feedback

    else:
        st.error(f'Erreur {res.status_code} : {res.text}')

# Affichage des boutons de feedback si aucun feedback n'a encore été donné
if st.session_state.prediction_done and not st.session_state.feedback_given:
    st.write("Êtes-vous satisfait de cette prédiction ?")
    col1, col2 = st.columns(2)

    if col1.button("👍 Oui", key="thumbs_up"):
        log_feedback("positive", user_input)
        st.success("Merci pour votre feedback positif!")
        st.session_state.feedback_given = True
        time.sleep(2)
        st.session_state.prediction_done = False  # Masquer les boutons après clic
        st.rerun()  # Forcer le rechargement de la page pour masquer les boutons

    if col2.button("👎 Non", key="thumbs_down"):
        log_feedback("negative", user_input)
        st.error("Merci pour votre feedback négatif. Nous allons nous améliorer!")
        st.session_state.feedback_given = True
        time.sleep(2)
        st.session_state.prediction_done = False  # Masquer les boutons après clic
        st.rerun()  # Forcer le rechargement de la page pour masquer les boutons