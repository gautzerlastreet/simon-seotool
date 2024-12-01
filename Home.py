import streamlit as st

# Configuration de la page Streamlit
st.set_page_config(
    layout="wide",
    page_title="SEO Tools Box",
    page_icon="📌"
)

# Ajouter le menu latéral (sidemenu)
menu = st.sidebar.radio(
    "Navigation",
    ["Home", "similarity refine", "paa extractor", "occurus rewrite", "semrush-refine"]
)

# Afficher le contenu principal selon l'onglet sélectionné
if menu == "Home":
    st.header("Home")
    st.write("Bienvenue dans le SEO Tools Box.")
elif menu == "similarity refine":
    st.header("Similarity Refine")
elif menu == "paa extractor":
    st.header("PAA Extractor")
elif menu == "occurus rewrite":
    st.header("Occurus Rewrite")
elif menu == "semrush-refine":
    st.header("Semrush Refine")

# Ajouter l'icône Twitter et le texte en bas à gauche
st.sidebar.markdown(
    """
    <div style="position: fixed; bottom: 10px; left: 10px;">
        <a href="https://twitter.com/lekoz_simon" target="_blank" style="text-decoration: none;">
            <img src="https://upload.wikimedia.org/wikipedia/en/thumb/6/60/Twitter_Logo_as_of_2021.svg/1200px-Twitter_Logo_as_of_2021.svg.png" 
                 alt="Twitter" style="width:20px; vertical-align: middle; margin-right: 5px;">
            <span style="color: white; font-size: 14px;">@lekoz_simon</span>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)