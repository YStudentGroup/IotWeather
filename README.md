# IotWeather

## Description
IotWeather est une application qui simule un sytème IOT météorologique et envoie les données à une API.

## Prérequis

Avant d'exécuter l'application, assurez-vous d'avoir les éléments suivants installés :

- **Python** : Vous pouvez télécharger la dernière version de Python [ici](https://www.python.org/downloads/).
- **pip** : Gestionnaire de paquets Python, généralement inclus avec Python.

## Installation 

### 1. Installer Python
- Allez sur le site officiel de Python : [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Cliquez sur "Download Python" (la dernière version stable).
- Exécutez le fichier téléchargé.
- Cochez la case “Add Python to PATH” avant de cliquer sur “Install Now”.

### 2. Installer les dépendances
Après avoir installé Python, suivez les étapes suivantes pour installer les dépendances nécessaires à l'exécution du projet.

#### Création d'un environnement virtuel
Dans le dossier de votre projet, créez un environnement virtuel pour isoler les dépendances :

```bash
python -m venv venv
```

#### Activer l'environnement virtuel

- **Sur Windows :**

```bash
venv\Scripts\activate
```

- **Sur macOS/Linux :**

```bash
source venv/bin/activate
```

#### Installer les packages nécessaires

Une fois l'environnement virtuel activé, installez les packages requis :

```bash
pip install -r requirements.txt
```

### 3. Vérification de l'installation

Vous pouvez vérifier que tout fonctionne correctement en exécutant la commande suivante, qui vérifie l'installation de PyLint :

```bash
pylint --version
```

## Lancer l'application

Une fois l'environnement virtuel configuré, vous pouvez exécuter l'application avec la commande suivante :

```bash
python SimulateData.py
```

Cela va simuler la collecte des données météorologiques et les envoyer à l'API configurée.

## Structure du projet

Voici la structure du projet :

```
IotWeather/
│
├── SimulateData.py       # Le fichier principal pour simuler et envoyer les données météorologiques.
├── requirements.txt      # Liste des dépendances Python du projet.
├── venv/                 # Dossier contenant l'environnement virtuel.
├── git/                  # Continent les règles git et le changelog.md
├── README.md             # Ce fichier.
└── .gitignore            # Liste des fichiers et dossiers à ignorer par git.
```

## Tests

### Exécution des tests unitaires

Le projet utilise **pytest** pour les tests. Pour exécuter les tests, utilisez la commande suivante :

```bash
pytest
```

Cela exécutera tous les tests dans le dossier `tests/` et affichera les résultats.

## Lancer PyLint

Pour analyser la qualité du code avec PyLint, exécutez la commande suivante :

```bash
pylint SimulateData.py
```

Cela générera un rapport sur les bonnes pratiques de codage et les éventuelles erreurs.
