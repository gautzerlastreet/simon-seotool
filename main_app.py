import streamlit as st
from apps.occurus_rewrite import occurus_rewrite
from apps.similarity_refine import similarity_refine


st.set_page_config(
    layout="wide",
    page_title="Simon's Tools Box",
    page_icon="🛠"
)

# Titre principal de l'application
st.sidebar.title("More tools, More Fun.")

# Menu latéral pour choisir une page
page = st.sidebar.selectbox(
    "Choisissez une application",
    ["Occurus Rewrite", "Similarity Refine"]
)

# Logique pour charger la page sélectionnée
if page == "Similarity Refine":
    similarity_refine.main()
elif page == "Occurus Rewrite":
    occurus_rewrite.app()
