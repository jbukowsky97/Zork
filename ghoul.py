import random

from monster import Monster

class Ghoul(Monster):
    
    def __init__(self):
        Monster.__init__(self, random.nextint(0, 40) + 40)