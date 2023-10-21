from general_weapon import weapon
import random as rd

class Spear:
    def __init__(self):
        weapon.name = Spear
        weapon.range = 4
        weapon.damage = rd.randint(2,6)