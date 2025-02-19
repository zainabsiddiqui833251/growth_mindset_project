import streamlit as st
import pandas as pd
from io import BytesIO

st.title("File Conversion")

uploaded_file = st.file_uploader("Upload your file", type=["csv", "xlsx"])

if uploaded_file:
    file_ext = uploaded_file.name.split(".")[-1].lower()
    
    if file_ext == "csv":
        df = pd.read_csv(uploaded_file)
    elif file_ext == "xlsx":
        df = pd.read_excel(uploaded_file)

    st.write("Preview of your file:")
    st.dataframe(df.head())

    conversion_type = st.radio("Convert to:", ["CSV", "EXCEL"])

    if st.button("Convert"):
        buffer = BytesIO()

        if conversion_type == "CSV":
            df.to_csv(buffer, index=False)
            file_name = uploaded_file.name.replace(file_ext, "csv")
            mime_type = "text/csv"
        else:
            df.to_excel(buffer, index=False, engine="openpyxl")
            file_name = uploaded_file.name.replace(file_ext, "xlsx")
            mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        buffer.seek(0)

        st.download_button(
            label=f"Download {file_name}",
            data=buffer,
            file_name=file_name,
            mime=mime_type,
        )
