#Visualisation des données pour l'application Movies

#%%
# Importation des librairies nécessaires
# Importation des librairies nécessaires
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from filmsdk import MovieClient, MovieConfig
import time
import json
from collections import Counter, defaultdict
from pathlib import Path
#%%
# URL de ton API Render (endpoint)
url = "https://movies-management-0ypw.onrender.com/movies"  # adapte le endpoint

# Requête GET
response = requests.get(url)

# Vérifie le statut
if response.status_code == 200:
    data = response.json()  # JSON → dict/list
    df = pd.DataFrame(data)  # Charger dans pandas
    print(df.head())
else:
    print("Erreur :", response.status_code)

# %%
# URL de l'API Render
url = "https://movies-management-0ypw.onrender.com"  # adapte le endpoint

# Requête GET
response = requests.get(url)

# Vérifie que tout s'est bien passé
if response.status_code == 200:
    data = response.json()  # données en JSON
    print(data)
else:
    print("Erreur :", response.status_code)
# %%
