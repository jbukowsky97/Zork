class Weapon:

    def __init__(self, name):
        self._name = name

class HersheyKiss(Weapon):

    def __init__(self):
        Weapon.__init__(self, "HersheyKiss")

class SourStraw(Weapon):

    def __init__(self):
        Weapon.__init__(self, "SourStraw")

class ChocolateBar(Weapon):

    def __init__(self):
        Weapon.__init__(self, "ChocolateBar")

class NerdBomb(Weapon):

    def __init__(self):
        Weapon.__init__(self, "NerdBomb")