import random

from monster import Monster

class Vampire(Monster):

    def __init__(self):
        Monster.__init__(self, random.nextint(0, 100) + 100)