"""Affichage VTK de la carte des restaurants.

Association point <-> restaurant : le point n°i du vtkPolyData correspond
au restaurant n°i de la liste. Quand on clique sur un point, VTK renvoie son
numéro, donc on retrouve directement le restaurant.
"""

import vtk


def creer_points(restaurants):
    """Crée un vtkPolyData avec un point (x, y, 0) par restaurant + leurs noms."""
    points = vtk.vtkPoints()
    noms = vtk.vtkStringArray()
    noms.SetName("nom")
    for r in restaurants:
        points.InsertNextPoint(r.x, r.y, 0)
        noms.InsertNextValue(r.nom)

    polydata = vtk.vtkPolyData()
    polydata.SetPoints(points)
    polydata.GetPointData().AddArray(noms)
    return polydata


class Carte:
    def __init__(self, restaurants):
        self.restaurants = restaurants
        self.polydata = creer_points(restaurants)

        self.renderer = vtk.vtkRenderer()
        self.renderer.SetBackground(1, 1, 1)

        # 1) Les restaurants : un point rouge chacun
        sommets = vtk.vtkVertexGlyphFilter()  # transforme les points en éléments affichables
        sommets.SetInputData(self.polydata)
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(sommets.GetOutputPort())
        self.acteur_points = vtk.vtkActor()
        self.acteur_points.SetMapper(mapper)
        self.acteur_points.GetProperty().SetColor(0.85, 0.2, 0.2)
        self.acteur_points.GetProperty().SetPointSize(12)
        self.acteur_points.GetProperty().RenderPointsAsSpheresOn()
        self.renderer.AddActor(self.acteur_points)

        # 2) Le nom de chaque restaurant à côté de son point
        etiquettes = vtk.vtkLabeledDataMapper()
        etiquettes.SetInputData(self.polydata)
        etiquettes.SetLabelModeToLabelFieldData()
        etiquettes.SetFieldDataName("nom")
        etiquettes.GetLabelTextProperty().SetColor(0, 0, 0)
        etiquettes.GetLabelTextProperty().SetFontSize(12)
        acteur_etiquettes = vtk.vtkActor2D()
        acteur_etiquettes.SetMapper(etiquettes)
        self.renderer.AddActor(acteur_etiquettes)

        # 3) Zone de texte en haut à gauche (infos du restaurant cliqué)
        self.texte = vtk.vtkTextActor()
        self.texte.SetInput("Cliquez sur un restaurant")
        self.texte.GetTextProperty().SetColor(0, 0, 0)
        self.texte.GetTextProperty().SetFontSize(16)
        self.texte.SetPosition(10, 10)
        self.renderer.AddActor(self.texte)

        self.fenetre = vtk.vtkRenderWindow()
        self.fenetre.AddRenderer(self.renderer)
        self.fenetre.SetSize(1000, 750)
        self.fenetre.SetWindowName("Restaurants")

        # Vue 2D : projection parallèle, cadrée sur tous les restaurants
        self.renderer.GetActiveCamera().ParallelProjectionOn()
        self.renderer.ResetCamera()

    def clic(self, style, evenement):
        """Clic gauche : cherche le point sous la souris et affiche son restaurant."""
        x, y = self.interacteur.GetEventPosition()
        picker = vtk.vtkPointPicker()
        picker.SetTolerance(0.01)
        picker.Pick(x, y, 0, self.renderer)
        i = picker.GetPointId()  # numéro du point cliqué, -1 si aucun

        if i >= 0:
            self.texte.SetInput(self.restaurants[i].description())
        else:
            self.texte.SetInput("Aucun restaurant ici")
        self.fenetre.Render()

    def afficher(self):
        self.interacteur = vtk.vtkRenderWindowInteractor()
        self.interacteur.SetRenderWindow(self.fenetre)
        # Style "image" : zoom et déplacement, mais pas de rotation 3D
        style = vtk.vtkInteractorStyleImage()
        style.AddObserver("LeftButtonPressEvent", self.clic)
        self.interacteur.SetInteractorStyle(style)
        self.fenetre.Render()
        self.interacteur.Start()
