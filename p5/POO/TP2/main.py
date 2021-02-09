from p5 import core
from p5.POO.TP2.bille import Bille
from p5.POO.TP2.creep import Creep
from p5.POO.TP2.player import Player

player1 = None
creeps = []
bille1 = Bille()

def setup():
    print("Setup start----")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]
    global player1, creeps
    player1 = Player()

    for i in range(0, 1000):
        creeps.append(Creep())
    print("Setup stop----")

def run():
    print("Run----")
    for c in creeps:
        c.afficher(core)

    player1.afficher(core)

    if core.getMouseLeftClick() is not None:
        player1.deplacer(core.getMouseLeftClick())



core.main(setup, run)


