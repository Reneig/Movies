# Utilise une image légère de Python 3.10 comme base
FROM python:3.10-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie uniquement le fichier des dépendances pour profiter du cache Docker
COPY requirements.txt .

# Installe les dépendances Python sans mise en cache
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copie le reste des fichiers (code Python et base de données)
COPY . .

# Expose le port utilisé par l'API
EXPOSE 80

# Lance le serveur Uvicorn pour exécuter l'API FastAPI
CMD ["uvicorn", "fastapi_app:app", "--host", "0.0.0.0", "--port", "80"]
