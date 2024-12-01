import streamlit as st

# Configuration de la page Streamlit
st.set_page_config(
    layout="wide",
    page_title="SEO Tools Box",
    page_icon="📌"
)

# Ajouter l'icône Twitter et le texte en bas à gauche
st.sidebar.markdown(
    """
    <div style="position: fixed; bottom: 10px; left: 10px;">
        <a href="https://twitter.com/lekoz_simon" target="_blank" style="text-decoration: none;">
            <img src="https://abs.twimg.com/favicons/twitter.3.ico" 
                 alt="Twitter" style="width:20px; vertical-align: middle; margin-right: 5px;">
            <span style="color: white; font-size: 14px;">@lekoz_simon</span>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)