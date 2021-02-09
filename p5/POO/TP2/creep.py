import random
import pygame
from pygame.math import Vector2, Vector3
from p5 import core

class Creep:
    def __init__ (self):
        self.position = Vector2 (random.randint(0, 400), random.randint(0, 400))
        self.couleur = Vector3 (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.taille = 2

    def mourir(self):
        pass

    def afficher(self, core):
        pygame.draw.circle(core.screen, (int(self.couleur.x), int(self.couleur.y), int(self.couleur.z)), (int(self.position.x), int(self.position.y)), self.taille)

