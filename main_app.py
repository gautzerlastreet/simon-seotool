import streamlit as st
from apps.occurus_rewrite import occurus_rewrite

# Titre principal de l'application
st.sidebar.title("Navigation")

# Menu latéral pour choisir une page
page = st.sidebar.selectbox(
    "Choisissez une page",
    ["Occurus Rewrite"]
)

# Logique pour charger la page sélectionnée
if page == "Occurus Rewrite":
    occurus_rewrite.app()
elif page == "Rankings Google Maps":
    google_maps.app()
elif page == "Bulk Semantic Analyzer":
    semantic_analyzer.app()
