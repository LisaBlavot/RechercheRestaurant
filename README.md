# Recherche de restaurants par Voronoï et Delaunay

Projet M1 – Algorithmique géométrique (Python + VTK).

## Installation

Utiliser le Python de Windows (python.org), pas celui de MSYS2 :

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Exécution

```powershell
python main.py          # ouvre la carte
python -m pytest        # lance les tests
```

Clic gauche sur un restaurant : affiche ses informations. Molette : zoom.

## Fichiers

```
main.py                       lance l'application
data/restaurants.csv          les restaurants (ID,nom,X,Y,type,prix,note)
restaurant_app/models.py      classe Restaurant + lecture du CSV
restaurant_app/visualization.py   affichage VTK et clic
tests/test_partie1.py         tests
```

Le point n°i affiché correspond au restaurant n°i de la liste : c'est ce qui
permet de retrouver le restaurant quand on clique sur un point.

## Avancement

- [x] Partie 1 – Représentation des données
- [ ] Partie 2 – Diagramme de Voronoï
- [ ] Partie 3 – Recherche à partir d'une position
- [ ] Partie 4 – Restaurants voisins (Delaunay)
- [ ] Partie 5 – Alternatives
