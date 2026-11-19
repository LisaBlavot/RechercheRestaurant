"""Données : la classe Restaurant et la lecture du fichier CSV."""

import csv
from dataclasses import dataclass


@dataclass
class Restaurant:
    id: int
    nom: str
    x: float
    y: float
    type: str
    prix: str
    note: float

    def description(self):
        return (f"{self.nom}\n"
                f"Cuisine : {self.type}\n"
                f"Prix : {self.prix}   Note : {self.note}/5\n"
                f"Position : ({self.x:g}, {self.y:g})")


def charger_restaurants(chemin):
    """Lit le CSV (ID,nom,X,Y,type,prix,note) et renvoie une liste de Restaurant."""
    restaurants = []
    # "utf-8-sig" ignore le BOM placé au début du fichier par Excel
    with open(chemin, encoding="utf-8-sig") as f:
        for ligne in csv.DictReader(f):
            restaurants.append(Restaurant(
                id=int(ligne["ID"]),
                nom=ligne["nom"],
                x=float(ligne["X"]),
                y=float(ligne["Y"]),
                type=ligne["type"],
                prix=ligne["prix"],
                note=float(ligne["note"]),
            ))
    return restaurants
