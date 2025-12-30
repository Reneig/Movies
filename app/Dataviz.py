#%%
# Importation des librairies nécessaires
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from moviemanagement import MovieClient, MovieConfig
import time
import json
from collections import Counter, defaultdict
from pathlib import Path

# %%
# Dossiers
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)
# %%
# Connexion à l'API via le package moviemanagement

config = MovieConfig(movie_base_url="https://movies-management-0ypw.onrender.com")
client = MovieClient(config=config)

# Vérification que l'API est opérationnelle
client.health_check()
# %%
