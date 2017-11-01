import random

class Monster:

    def __init__(self, hp):
        self._hp = hp

class Person(Monster):

    def __init__(self):
        Monster.__init__(self, 100)
        
class Zombie(Monster):

    def __init__(self):
        Monster.__init__(self, random.randint(0, 50) + 50)

class Vampire(Monster):

    def __init__(self):
        Monster.__init__(self, random.nextint(0, 100) + 100)

class Ghoul(Monster):
    
    def __init__(self):
        Monster.__init__(self, random.nextint(0, 40) + 40)

class Werewolve(Monster):
    
    def __init__(self):
        Monster.__init__(self, 200)