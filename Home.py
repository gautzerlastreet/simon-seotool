import streamlit as st
my_var = "This a variable from Home.py"

def main():
    st.header("SEO Tools Box")
    st.title("Simon's Tools Box")
    st.write(my_var)
   
    choix = st.sidebar.radio("Navigation", ["Home", "Similarity Refine", "PAA Extractor"])
    if choix == "Home":
        st.subheader("subheader")
    if choix == "Similarity Refine":
        st.subheader("subheader SR")
    if choix == "PAA Extractor":
        st.subheader("subheader PA")
                   
        

if __name__ == '__main__':
  main