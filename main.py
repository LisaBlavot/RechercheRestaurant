"""Lance l'application :  python main.py"""

from restaurant_app.models import charger_restaurants
from restaurant_app.visualization import Carte

restaurants = charger_restaurants("data/restaurants.csv")
print(len(restaurants), "restaurants chargés")

Carte(restaurants).afficher()
