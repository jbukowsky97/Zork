from monster import Monster

class Person(Monster):

    def __init__(self):
        Monster.__init__(self, 100)