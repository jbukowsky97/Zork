import random

from monsters import Monster, Person, Zombie, Vampire, Ghoul, Werewolve
from observe import Observer, Observable

#######################################################
# home class
#######################################################
class Home(Observer, Observable):
    
    #######################################################
    # constructor to initialize variables
    #
    # @param self current object
    #######################################################
    def __init__(self):
        #list of 0-10 monsters
        Observable.__init__(self)
        self._monsters = []
        monster_types = "PZVGW"
        for i in range(0, 10):
            rand_monster = random.choice(monster_types)
            monster = None
            if rand_monster == "P":
                monster = Person()
            elif rand_monster == "Z":
                monster = Zombie()
            elif rand_monster == "V":
                monster = Vampire()
            elif rand_monster == "G":
                monster = Ghoul()
            elif rand_monster == "W":
                monster = Werewolve()
            monster.add_observer(self)
            self._monsters.append(monster)

    #######################################################
    # removes monster and adds a person
    #
    # @param self current object
    # @param observable monster being removed
    # @param msg message sent by monster
    #######################################################
    def update(self, observable, msg):
        observable.remove_observer(self)
        self._monsters.remove(observable)
        self._monsters.append(Person())
        self.notify_observers("died")

    #######################################################
    # returns monsters list
    #
    # @param self current object
    #
    # @return list(Monster) list of monsters
    #######################################################
    def get_monsters(self):
        return self._monsters

    #######################################################
    # returns number of people in house
    #
    # @param self current object
    #
    # @return int number of people
    #######################################################
    def get_people(self):
        num_people = 0
        for monster in self._monsters:
            if type(monster) is Person:
                num_people += 1
        return num_people

    #######################################################
    # returns number of zombies in house
    #
    # @param self current object
    #
    # @return int number of zombies
    #######################################################
    def get_zombies(self):
        num_zombies = 0
        for monster in self._monsters:
            if type(monster) is Zombie:
                num_zombies += 1
        return num_zombies

    #######################################################
    # returns number of vampires in house
    #
    # @param self current object
    #
    # @return int number of vampires
    #######################################################
    def get_vampires(self):
        num_vampires = 0
        for monster in self._monsters:
            if type(monster) is Vampire:
                num_vampires += 1
        return num_vampires

    #######################################################
    # returns number of ghouls in house
    #
    # @param self current object
    #
    # @return int number of ghouls
    #######################################################
    def get_ghouls(self):
        num_ghouls = 0
        for monster in self._monsters:
            if type(monster) is Ghoul:
                num_ghouls += 1
        return num_ghouls

    #######################################################
    # returns number of werewolves in house
    #
    # @param self current object
    #
    # @return int number of werewolves
    #######################################################
    def get_werewolves(self):
        num_werewolves = 0
        for monster in self._monsters:
            if type(monster) is Werewolve:
                num_werewolves += 1
        return num_werewolves