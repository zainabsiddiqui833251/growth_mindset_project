import streamlit as st
import pandas as pd

st.title("Data Visualization")

uploaded_file = st.file_uploader("Upload your file", type=["csv", "xlsx"])

if uploaded_file:
    file_ext = uploaded_file.name.split(".")[-1].lower()
    
    if file_ext == "csv":
        df = pd.read_csv(uploaded_file)
    elif file_ext == "xlsx":
        df = pd.read_excel(uploaded_file)

    st.write("Preview of your file:")
    st.dataframe(df.head())

    numeric_cols = df.select_dtypes(include="number")

    if not numeric_cols.empty:
        st.subheader("Bar Chart")
        st.bar_chart(numeric_cols)
    else:
        st.write("No numerical data found for visualization.")
