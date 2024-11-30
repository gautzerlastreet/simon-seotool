import streamlit as st

# Définir une fonction pour chaque page
def page_ranking_everywhere():
    st.title("Rankings Everywhere 🎯")
    st.subheader("Configuration")
    
    # Charger un fichier
    st.write("1. Mots-clés et pages")
    uploaded_file = st.file_uploader("Chargez votre fichier Excel avec une colonne 'Query'", type=["xlsx"])
    if uploaded_file:
        st.write("Fichier téléchargé :", uploaded_file.name)
    
    # Sélection de la langue et du pays
    st.write("2. Langue et pays")
    language = st.selectbox("Langue", ["French", "English", "Spanish"], index=0)
    country = st.selectbox("Pays", ["France", "Germany", "USA"], index=0)
    st.write(f"Langue : {language}, Pays : {country}")

def page_google_maps():
    st.title("Rankings Google Maps")
    st.write("Cette page est dédiée à Google Maps Ranking.")
    # Ajoutez d'autres éléments spécifiques à cette page

def page_semantic_analyzer():
    st.title("Bulk Semantic Analyzer")
    st.write("Analyse sémantique en masse.")
    # Ajoutez des composants ici

# Structure de navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choisissez une page",
    ["Rankings Everywhere", "Rankings Google Maps", "Bulk Semantic Analyzer"]
)

# Logique pour afficher la page sélectionnée
if page == "Rankings Everywhere":
    page_ranking_everywhere()
elif page == "Rankings Google Maps":
    page_google_maps()
elif page == "Bulk Semantic Analyzer":
    page_semantic_analyzer()
