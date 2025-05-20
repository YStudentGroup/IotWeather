# Utilise une image Python légère
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY SimulateData.py .

# Lancer le script automatiquement au démarrage du conteneur
CMD ["python", "SimulateData.py"]
