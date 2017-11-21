import random

from observe import Observable

from weapons import Weapon, HersheyKiss, SourStraw, ChocolateBar, NerdBomb

#######################################################
# monster class that outlines requirements for a monster
#######################################################
class Monster(Observable):

    #######################################################
    # constructor to initialize varaibles
    #
    # @param self current object
    # @param hp monster health
    #######################################################
    def __init__(self, hp):
        Observable.__init__(self)
        self._hp = hp
        self._type = "monster"

    #######################################################
    # determine if monster is dead, if is, updates observers
    #
    # @param self current object
    #######################################################
    def _check_dead(self):
        if self._hp <= 0:
            self.notify_observers("died")

    #######################################################
    # generates an attack
    #
    # @param self current object
    #
    # @return int damage of attack
    #######################################################
    def generate_attack(self):
        pass

    #######################################################
    # calculates damage taken and also checks if died
    #
    # @param self current object
    # @param player_atk player attack
    # @param weapon weaopn used to attack
    #
    # @return int damage monster took
    #######################################################
    def calculate_damage_taken(self, player_atk, weapon):
        pass
    
    #######################################################
    # returns monsters health
    #
    # @param self current object
    #
    # @return int monsters health
    #######################################################
    def get_hp(self):
        return self._hp

    #######################################################
    # returns monsters type
    #
    # @param self current object
    #
    # @type string type of monster
    #######################################################
    def get_type(self):
        return self._type

#######################################################
# sub-class of a monster
#######################################################
class Person(Monster):

    #######################################################
    # constructor to initialize varaibles
    #
    # @param self current object
    #######################################################
    def __init__(self):
        Monster.__init__(self, 100)
        self._type = "person"
    
    #######################################################
    # generates an attack
    #
    # @param self current object
    #
    # @return int damage of attack
    #######################################################
    def generate_attack(self):
        return -1

    def calculate_damage_taken(self, player_atk, weapon):
        return 0

#######################################################
# sub-class of a monster
#######################################################
class Zombie(Monster):

    #######################################################
    # constructor to initialize varaibles
    #
    # @param self current object
    #######################################################
    def __init__(self):
        Monster.__init__(self, random.randint(50, 100))
        self._type = "zombie"

    #######################################################
    # generates an attack
    #
    # @param self current object
    #
    # @return int damage of attack
    #######################################################
    def generate_attack(self):
        return random.randint(0, 10)

    #######################################################
    # calculates damage taken and also checks if died
    #
    # @param self current object
    # @param player_atk player attack
    # @param weapon weaopn used to attack
    #
    # @return int damage monster took
    #######################################################
    def calculate_damage_taken(self, player_atk, weapon):
        calculated_atk = player_atk * weapon.get_attack_modifier()
        if type(weapon) is SourStraw:
            calculated_atk *= 2
        self._hp -= calculated_atk
        self._check_dead()
        return calculated_atk

#######################################################
# sub-class of a monster
#######################################################
class Vampire(Monster):

    #######################################################
    # constructor to initialize varaibles
    #
    # @param self current object
    #######################################################
    def __init__(self):
        Monster.__init__(self, random.randint(100, 200))
        self._type = "vampire"
    
    #######################################################
    # generates an attack
    #
    # @param self current object
    #
    # @return int damage of attack
    #######################################################
    def generate_attack(self):
        return random.randint(10, 20)

    #######################################################
    # calculates damage taken and also checks if died
    #
    # @param self current object
    # @param player_atk player attack
    # @param weapon weaopn used to attack
    #
    # @return int damage monster took
    #######################################################
    def calculate_damage_taken(self, player_atk, weapon):
        if type(weapon) is ChocolateBar:
            return 0
        else:
            calculated_atk = player_atk * weapon.get_attack_modifier()
            self._hp -= calculated_atk
            self._check_dead()
            return calculated_atk

#######################################################
# sub-class of a monster
#######################################################
class Ghoul(Monster):

    #######################################################
    # constructor to initialize varaibles
    #
    # @param self current object
    #######################################################
    def __init__(self):
        Monster.__init__(self, random.randint(40, 80))
        self._type = "ghoul"

    #######################################################
    # generates an attack
    #
    # @param self current object
    #
    # @return int damage of attack
    #######################################################
    def generate_attack(self):
        return random.randint(15, 30)

    #######################################################
    # calculates damage taken and also checks if died
    #
    # @param self current object
    # @param player_atk player attack
    # @param weapon weaopn used to attack
    #
    # @return int damage monster took
    #######################################################
    def calculate_damage_taken(self, player_atk, weapon):
        calculated_atk = player_atk * weapon.get_attack_modifier()
        if type(weapon) is NerdBomb:
            calculated_atk *= 5
        self._hp -= calculated_atk
        self._check_dead()
        return calculated_atk

#######################################################
# sub-class of a monster
#######################################################
class Werewolve(Monster):

    #######################################################
    # constructor to initialize varaibles
    #
    # @param self current object
    #######################################################
    def __init__(self):
        Monster.__init__(self, 200)
        self._type = "werewolve"

    #######################################################
    # generates an attack
    #
    # @param self current object
    #
    # @return int damage of attack
    #######################################################
    def generate_attack(self):
        return random.randint(0, 40)

    #######################################################
    # calculates damage taken and also checks if died
    #
    # @param self current object
    # @param player_atk player attack
    # @param weapon weaopn used to attack
    #
    # @return int damage monster took
    #######################################################
    def calculate_damage_taken(self, player_atk, weapon):
        if type(weapon) is ChocolateBar or type(weapon) is SourStraw:
            return 0
        else:
            calculated_atk = player_atk * weapon.get_attack_modifier()
            self._hp -= calculated_atk
            self._check_dead()
            return calculated_atk