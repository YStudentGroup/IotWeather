import random
from datetime import datetime

def get_weather():
    conditions = ['ensoleillé', 'nuageux', 'pluvieux', 'orageux', 'neigeux',]
    temperatures = {
        'été': (20, 35),
        'hiver': (-5, 5),
        'printemps': (10, 20),
        'automne': (5, 15)
    }

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
    
    condition = random.choice(conditions)

    return {
        'temperature': f"{temperature}°C",
        'ressentie': f"{ressentie}°C",
        'condition': condition,
        'saison': saison,
        'vent': f"{vent} km/h",
        'humidite': f"{humidite}%",
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    weather_data = get_weather()
    print("Données météorologiques simulées : ", weather_data)