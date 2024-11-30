import streamlit as st
from apps import ranking_everywhere, google_maps, semantic_analyzer

# Titre principal de l'application
st.sidebar.title("Navigation")

# Menu latéral pour choisir une page
page = st.sidebar.selectbox(
    "Choisissez une page",
    ["Similarity Refine", "PAA Checker", "Bulk Semantic Analyzer"]
)

# Logique pour charger la page sélectionnée
if page == "Rankings Everywhere":
    ranking_everywhere.app()
elif page == "Rankings Google Maps":
    google_maps.app()
elif page == "Bulk Semantic Analyzer":
    semantic_analyzer.app()
