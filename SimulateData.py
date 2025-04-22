import random
from datetime import datetime
import time
import requests # type: ignore

def get_weather():
    conditions = ['ensoleillé', 'nuageux', 'pluvieux', 'orageux', 'neigeux',]
    temperatures = {
        'été': (20, 35),
        'hiver': (-5, 5),
        'printemps': (10, 20),
        'automne': (5, 15)
    }

    locationList = [
        'Paris', 'Lyon', 'Marseille', 'Toulouse', 'Nice',
        'Nantes', 'Strasbourg', 'Montpellier', 'Bordeaux', 'Lille',
        'Rennes', 'Reims', 'Saint-Étienne', 'Le Havre', 'Grenoble',
        'Dijon', 'Nîmes', 'Aix-en-Provence', 'Angers', 'Villeurbanne',
        'Saint-Denis', 'Clermont-Ferrand', 'La Rochelle', 'Saint-Paul',
        'Saint-Pierre', 'Amiens', 'Tours', 'Limoges', 'Annecy',
        'Perpignan', 'Metz', 'Besançon', 'Boulogne-Billancourt',
        'Rouen', 'Mulhouse', 'Caen', 'Nancy', 'Argenteuil',
        'Saint-Maur-des-Fossés', 'Montreuil', 'Avignon', 'Nanterre',
        'Créteil', 'Poitiers', 'Versailles', 'La Seyne-sur-Mer',
        'Colombes', 'Asnières-sur-Seine', 'Aubervilliers', 'Rueil-Malmaison',
        'Antibes', 'Saint-Nazaire', 'Cannes', 'Saint-Denis', 'Colmar',
        'La Rochelle', 'Calais', 'Ajaccio', 'Béziers', 'Cayenne',
        'Fort-de-France', 'Pau', 'Saint-Étienne-du-Rouvray', 'Le Tampon',
    ]

    month = datetime.now().month
    if month in [12, 1, 2]:
        saison = 'hiver'
    elif month in [3, 4, 5]:
        saison = 'printemps'
    elif month in [6, 7, 8]:
        saison = 'été'
    else:
        saison = 'automne'

    vent_min, vent_max = (0, 80)
    vent = round(random.uniform(vent_min, vent_max), 1)
    humidite = round(random.uniform(0, 100), 1)
    temp_min, temp_max = temperatures[saison]
    temperature = round(random.uniform(temp_min, temp_max), 1)
    ressentie = round(random.uniform(temperature - 3, temperature + 3), 1)
    location = random.choice(locationList)
    
    condition = random.choice(conditions)

    return {
        'temperature': temperature,
        'felt': ressentie,
        'condition': condition,
        'season': saison,
        'wind': vent,
        'humidity': humidite,
        'location': location,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def send_weather_to_api(api_url):
    while True:
        data = get_weather()
        try:
            response = requests.post(api_url, json=data)
            if response.status_code >= 200 and response.status_code < 300:
                print(data)
                print(f"[{datetime.now()}] Données envoyées avec succès.")
            else:
                print(f"[{datetime.now()}] Erreur {response.status_code} lors de l'envoi.")
        except Exception as e:
            print(f"[{datetime.now()}] Exception lors de l'envoi : {e}")

        time.sleep(10)

if __name__ == "__main__":
    API_URL = "http://192.168.137.1:3001/api/weather"
    send_weather_to_api(API_URL)