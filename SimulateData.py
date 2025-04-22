import random
from datetime import datetime

def get_weather():
    conditions = ['ensoleillé', 'nuageux', 'pluvieux', 'orageux', 'neigeux', 'brumeux']
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

    temp_min, temp_max = temperatures[saison]
    temperature = round(random.uniform(temp_min, temp_max), 1)
    
    condition = random.choice(conditions)

    return {
        'temperature': f"{temperature}°C",
        'condition': condition,
        'saison': saison,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


if __name__ == "__main__":
    meteo = get_weather()
    print("Météo simulée :", meteo)