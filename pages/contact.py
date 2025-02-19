import streamlit as st

st.title("Contact Us 📩")

st.write("If you have any questions or suggestions, feel free to reach out!")

# Contact Information
st.subheader("📞 Contact Information")
st.write("""
- 📍 **Location:** Karachi, Pakistan  
- 📧 **Email:** support@growthmindchallenge.com  
- 🌐 **Website:** [www.growthmindchallenge.com](#)  
- 📱 **Phone:** +92 300 1234567  
""")

# Social Media Links
st.subheader("🌍 Connect with Us")
st.write("""
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github)](https://github.com/)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/)  
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter)](https://twitter.com/)  
""", unsafe_allow_html=True)

# Contact Form
st.subheader("✉️ Send Us a Message")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Send")

    if submitted:
        if name and email and message:
            st.success("Thank you for your message! We will get back to you soon.")
        else:
            st.error("Please fill in all fields before submitting.")

