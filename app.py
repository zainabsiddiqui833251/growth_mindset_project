import streamlit as st

st.set_page_config(page_title="Growth Mind Challenge", layout="wide")

st.title("Growth Mind Challenge")
st.write("Welcome to the Growth Mind Challenge App! 🎯")

# About section
st.subheader("About This App")
st.write(
    """
    This app helps users transform files between CSV and Excel formats while providing built-in **data cleaning** 
    and **visualization** features. You can:
    
    - Upload CSV or Excel files 📂
    - Clean and preprocess your data 🧹
    - Visualize your data 📊
    - Convert between CSV and Excel formats 🔄

    Use the **sidebar** to navigate between different features.
    """
)

st.sidebar.success("Select a page above ☝️")
