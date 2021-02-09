from pygame.math import Vector2, Vector3


class Creep:
    def __init__ (self):
        self.position = Vector2 ()
        self.couleur = Vector3 ()
        self.taille = 5

    def mourir(self):
        pass

    def