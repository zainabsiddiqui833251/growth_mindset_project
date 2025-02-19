import streamlit as st
import pandas as pd

st.title("Data Cleaning")

uploaded_file = st.file_uploader("Upload your file", type=["csv", "xlsx"])

if uploaded_file:
    file_ext = uploaded_file.name.split(".")[-1].lower()
    
    if file_ext == "csv":
        df = pd.read_csv(uploaded_file)
    elif file_ext == "xlsx":
        df = pd.read_excel(uploaded_file)
    
    st.write("Preview of your file:")
    st.dataframe(df.head())

    if st.button("Remove Duplicates"):
        df.drop_duplicates(inplace=True)
        st.write("Duplicates removed!")

    if st.button("Handle Missing Values"):
        numeric_cols = df.select_dtypes(include=["number"]).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        st.write("Missing values filled with mean.")

    st.write("Cleaned Data:")
    st.dataframe(df)
