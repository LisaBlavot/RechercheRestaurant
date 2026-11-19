"""Tests de la partie 1.  Lancer avec :  python -m pytest"""

from restaurant_app.models import charger_restaurants
from restaurant_app.visualization import creer_points

restaurants = charger_restaurants("data/restaurants.csv")


def test_lecture():
    assert len(restaurants) == 30
    assert restaurants[2].nom == "La Piazza"
    assert (restaurants[2].x, restaurants[2].y) == (520, 310)


def test_point_i_est_restaurant_i():
    polydata = creer_points(restaurants)
    assert polydata.GetNumberOfPoints() == len(restaurants)
    for i, r in enumerate(restaurants):
        assert polydata.GetPoint(i) == (r.x, r.y, 0)
