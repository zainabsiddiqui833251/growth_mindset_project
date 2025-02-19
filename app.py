import streamlit as st

# Set Page Configurations
st.set_page_config(page_title="Zainab's Portfolio", page_icon="✨", layout="wide")

# Apply Custom CSS
st.markdown("""
    <style>
        /* Custom Fonts and Styles */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        * {
            font-family: 'Poppins', sans-serif;
        }

        /* Page Layout */
        .main {
            background-color: #f9f9f9;
            padding: 20px;
        }

        /* Title Styling */
        .title {
            text-align: center;
            font-size: 3rem;
            color: #2b2c28;
        }

        /* Profile Section */
        .profile-container {
            text-align: center;
        }

        .profile-pic {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        }

        .about-text {
            text-align: center;
            font-size: 1.2rem;
            color: #339989;
            margin-top: 10px;
        }

        /* Skills Section */
        .skills-container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 20px;
            width: 100%;
        }

        .skill {
            background-color: #7DE2D1;
            padding: 10px 20px;
            border-radius: 20px;
            color: #131515;
            font-weight: bold;
        }

        /* Projects Section */
        .project-card {
            background: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
            margin: 10px;
        }

        /* Contact Section */
        .contact-info {
            text-align: center;
            font-size: 1.1rem;
            color: #2B2C28;
            margin-top: 20px;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .title {
                font-size: 2rem;
            }

            .profile-pic {
                width: 120px;
                height: 120px;
            }

            .about-text {
                font-size: 1rem;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Portfolio Content
st.markdown('<h1 class="title">Zainab Siddiqui</h1>', unsafe_allow_html=True)
st.markdown('<div class="profile-container"><img src="https://via.placeholder.com/150" class="profile-pic"></div>', unsafe_allow_html=True)
st.markdown('<p class="about-text">I am a passionate Frontend Developer with expertise in HTML, CSS, JavaScript, and TypeScript.</p>', unsafe_allow_html=True)

# Skills Section
st.subheader("🔹 Skills")
st.markdown('<div class="skills-container">', unsafe_allow_html=True)
skills = ["HTML", "CSS", "JavaScript", "Bootstrap", "TypeScript", "React", "GitHub"]
for skill in skills:
    st.markdown(f'<span class="skill">{skill}</span>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Projects Section
st.subheader("📌 Projects")
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.write("💻 **Recipe Website**")
    st.write("A fully responsive recipe website with user comments and ratings.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.write("🎵 **MelodyStream**")
    st.write("An interactive music streaming website with a song queue feature.")
    st.markdown('</div>', unsafe_allow_html=True)

# Contact Section
st.subheader("📞 Contact")
st.markdown('<p class="contact-info">📧 Email: zainab@example.com</p>', unsafe_allow_html=True)
st.markdown('<p class="contact-info">💼 LinkedIn: linkedin.com/in/zainab</p>', unsafe_allow_html=True)
st.markdown('<p class="contact-info">📍 Location: Karachi, Pakistan</p>', unsafe_allow_html=True)


