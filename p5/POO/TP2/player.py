import random

from pygame.math import Vector2, Vector3


class Player:
    def __init__ (self):
        self.taille = 5
        self.vitesse = 5
        self.direction = Vector2()
        self.position = Vector2()
        self.couleur = Vector3()
        self.forme = "rond"

    def manger(self):
        pass

    def mourir(self):
        pass

    def deplacer(self):
        pass

    def afficher(self):
        pass

