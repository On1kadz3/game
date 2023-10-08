from general_mob import Entity
import random as rd


class Skeleton:
    def attack(self):
        pass


Skeleton = Entity(Skeleton, 25, rd.randint(1, 4), 0, 1, 2, 6)
