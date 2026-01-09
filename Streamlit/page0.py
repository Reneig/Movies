import streamlit as st

# Configuration de la page
st.set_page_config(
    layout="wide",
    page_title="MovieLens Analytics - Projet Académique",
    page_icon="🎬"
)

# --- STYLE CSS PERSONNALISÉ ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .author-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    .phase-container {
        border-left: 5px solid #28a745;
        padding-left: 20px;
        margin-top: 30px;
    }
    .github-btn {
        background-color: #24292e;
        color: white !important;
        padding: 10px 20px;
        text-decoration: none;
        border-radius: 5px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- EN-TÊTE ---
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🎬 Application of movies management</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em;'>Projet Académique en Science des Données et Architecture Logicielle</p>", unsafe_allow_html=True)
st.divider()

# --- SECTION ÉQUIPE (AUTEURS) ---
st.markdown("### 👥 L'Équipe du Projet")
auth_col1, auth_col2, auth_col3 = st.columns(3)

authors = [
    {
        "name": "GBODOGBE Zinsou René",
        "linkedin": "https://www.linkedin.com/in/rene-gbodogbe",
        "github": "https://github.com/Reneig",
        "col": auth_col1
    },
    {
        "name": "COMLAN Cybelle",
        "linkedin": "https://www.linkedin.com/in/cybelle-comlan",
        "github": "https://github.com/cybelle-c",
        "col": auth_col2
    },
    {
        "name": "DOMINGO Giovani",
        "linkedin": "https://www.linkedin.com/in/giovani-domingo",
        "github": "https://github.com/giovani-d",
        "col": auth_col3
    }
]

for auth in authors:
    with auth["col"]:
        st.markdown(f"""
            <div class="author-card">
                <h4>{auth['name']}</h4>
                <a href="{auth['linkedin']}" target="_blank">🔵 LinkedIn</a> | 
                <a href="{auth['github']}" target="_blank">⚫ GitHub</a>
            </div>
            """, unsafe_allow_html=True)

st.write(" ")
st.write(" ")

# --- SECTION CODE SOURCE UNIQUE ---
st.info("💡 **Note :** L'intégralité du code source (Backend, API et Frontend) est centralisée sur un seul dépôt GitHub.")
st.markdown(f"""
    <div style='text-align: center;'>
        <a class="github-btn" href="https://github.com/Reneig/Movies" target="_blank">
            📂 Accéder au Dépôt GitHub Complet
        </a>
    </div>
    """, unsafe_allow_html=True)

st.write(" ")
st.divider()

# --- DÉTAILS DES PHASES DU PROJET ---

# PHASE 1
st.markdown("## 🏗️ Phase 1 : Architecture Backend & API")
col_p1_img, col_p1_text = st.columns([2, 1])

with col_p1_img:
    st.image("https://raw.githubusercontent.com/JosueAfouda/films-analytics/main/streamlit_app/architecture.png", 
             caption="Architecture de l'API et gestion des données", use_container_width=True)

with col_p1_text:
    st.markdown("""
    **Objectifs :**
    * Développement d'un client Python robuste.
    * Configuration d'une API REST pour la gestion des films.
    * Mise en place des modèles de données.
    * Health check et gestion des erreurs de connexion.
    """)

st.write(" ")

# PHASE 2
st.markdown("## 📊 Phase 2 : Data Analytics & Visualisation")
col_p2_img, col_p2_text = st.columns([2, 1])

with col_p2_img:
    st.image("https://raw.githubusercontent.com/JosueAfouda/films-analytics/main/streamlit_app/architecturephase.png", 
             caption="Pipeline d'analyse et Dashboard Streamlit", use_container_width=True)

with col_p2_text:
    st.markdown("""
    **Objectifs :**
    * Extraction et nettoyage des données MovieLens.
    * Transformation vers le format Parquet pour la performance.
    * Analyse exploratoire des genres et des évaluations.
    * Création d'un dashboard interactif (Streamlit).
    """)

# --- PIED DE PAGE ---
st.divider()
st.caption("Projet réalisé dans le cadre de la formation AMSE2 - 2026")