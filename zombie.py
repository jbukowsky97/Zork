import random

from monster import Monster

class Zombie(Monster):

    def __init__(self):
        Monster.__init__(self, random.randint(0, 50) + 50)