import streamlit as st
my_var = "This a variable from Home.py"


# Configuration de la page Streamlit
st.set_page_config(
    layout="wide",
    page_title="SEO Tools Box",
    page_icon="📌"
)


def main():
    st.header("SEO Tools Box")
    st.title("Simon's Tools Box")
    st.write(my_var)
   
    choix = st.sidebar.radio("Navigation", ["Home", "Similarity Refine", "PAA Extractor"])
    if choix == "Home":
        st.subheader("subheader")
    elif choix == "Similarity Refine":
        st.subheader("subheader SR")
    elif choix == "PAA Extractor":
        st.subheader("subheader PA")
    else:
        st.subheader("Please select an option from the sidebar")
        

if __name__ == '__main__':
    main()