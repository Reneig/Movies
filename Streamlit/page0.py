import streamlit as st

# Page Configuration
st.set_page_config(
    layout="wide",
    page_title="Movie Management App",
    page_icon="🎬"
)

# --- CUSTOM CSS FOR PROFESSIONAL LOOK ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .author-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        text-align: center;
        margin-bottom: 10px;
        transition: transform 0.3s;
    }
    .author-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
    }
    .github-btn {
        background-color: #1E3A8A;
        color: white !important;
        padding: 12px 24px;
        text-decoration: none;
        border-radius: 8px;
        font-weight: bold;
        display: inline-block;
        margin-top: 10px;
    }
    h1, h2 {
        color: #1E3A8A;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 style='text-align: center;'>🎬 Movie Management App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.3em; color: #555;'>Academic Project: Data Science & Software</p>", unsafe_allow_html=True)
st.write("---")

# --- AUTHORS SECTION ---
st.subheader("👥 Project Authors")
auth_col1, auth_col2, auth_col3 = st.columns(3)

authors = [
    {
        "name": "GBODOGBE Zinsou René",
        "linkedin": "https://www.linkedin.com/in/gbodogberene",
        "github": "https://github.com/Reneig",
        "col": auth_col1
    },
    {
        "name": "COMLAN Cybelle",
        "linkedin": "https://www.linkedin.com/in/cybelle-comlan-283a62276",
        "github": "https://github.com/comlan25",
        "col": auth_col2
    },
    {
        "name": "DOMINGO Giovanni",
        "linkedin": "https://www.linkedin.com/in/charbel-domingo-marcellin",
        "github": "https://github.com/echo-charbel",
        "col": auth_col3
    }
]

for auth in authors:
    with auth["col"]:
        st.markdown(f"""
            <div class="author-card">
                <h5 style="margin-bottom: 10px;">{auth['name']}</h5>
                <a href="{auth['linkedin']}" target="_blank" style="text-decoration: none; color: #0077b5;">🔵 LinkedIn</a> | 
                <a href="{auth['github']}" target="_blank" style="text-decoration: none; color: #333;">⚫ GitHub</a>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")

# --- CENTRAL REPOSITORY ---
st.info("💡 **Centralized Codebase:** The entire source code (Backend, API, and Frontend) is hosted on a single GitHub repository.")
st.markdown("""
    <div style='text-align: center;'>
        <a class="github-btn" href="https://github.com/Reneig/Movies" target="_blank">
            📂 Access Full GitHub Repository
        </a>
    </div>
    """, unsafe_allow_html=True)

st.write(" ")

# --- PROJECT PHASES DETAIL ---

st.subheader("🚀 Project Scope & Implementation")

# Utilisation de colonnes pour l'alignement côte à côte
col1, col2 = st.columns(2)

with col1:
    # On utilise du HTML personnalisé pour réduire la taille (h4 ou h5 au lieu de h3)
    # et on force une marge nulle pour l'alignement
    st.markdown("""
    <div style="background-color: #dcfce7; padding: 20px; border-radius: 10px; height: 100%;">
        <h5 style="margin: 0; color: #166534;">🏗️ Phase 1: Backend & API</h5>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Core Infrastructure:**
    * **Database Design**: Structured SQL modeling using SQLite.
    * **API Development**: Robust REST API built with **FastAPI**.
    * **ORM**: Implementation of **SQLAlchemy** for efficient data querying.
    * **Containerization**: API deployment using **Docker** for scalability.
    * **Distribution**: Python SDK published on **PyPI** (`moviemanagement`).
    """)

with col2:
    st.markdown("""
    <div style="background-color: #dbeafe; padding: 20px; border-radius: 10px; height: 100%;">
        <h5 style="margin: 0; color: #1e40af;">📊 Phase 2: Analytics & Frontend</h5>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Data Insights:**
    * **Exploratory Data Analysis (EDA)**: Trend identification.
    * **Data Management**: Integration of **Pydantic** for validation.
    * **Interactive Dashboard**: Full management UI built with **Streamlit**.
    * **Visualizations**: Dynamic charts to monitor the movie ecosystem.
    """)

# --- FOOTER ---
st.write("---")
st.caption("© 2026 Academic Project - AMSE2 Formation. All rights reserved.")