import random
import pygame
from pygame.math import Vector2, Vector3
from p5 import core

class Player:
    def __init__ (self):
        self.taille = 20
        self.direction = Vector2()
        self.position = Vector2(random.randint(0, 400), random.randint(0, 400))
        self.couleur = Vector3(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.forme = "rond"

    def manger(self):
        pass

    def mourir(self):
        pass

    def deplacer(self, position):
        self.position.x = position[0]
        self.position.y = position[1]

    def afficher(self, core):
        if self.forme == "rond":
            pygame.draw.circle(core.screen, (int(self.couleur.x), int(self.couleur.y), int(self.couleur.z)), (int(self.position.x), int(self.position.y)), self.taille)


