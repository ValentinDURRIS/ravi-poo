from p5 import core
from p5.POO.Drop import Drop

drops = []


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    for i in range(0, 1000):
        drops.append(Drop(400))
    print("Setup END-----------")


def run():
    print("Run")
    for d in drops:
        d.tomber(400)
        d.affichage(core)


core.main(setup, run)
