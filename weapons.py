import random

from observe import Observable

#######################################################
# weapon class 
#######################################################
class Weapon(Observable):

    #######################################################
    # constructor to initialize variables
    #
    # @param self current object
    # @param name name of weapon
    # @param attack_modifier attack modifier of weapon
    # @param uses number of uses for weapon
    #######################################################
    def __init__(self, name, attack_modifier, uses):
        Observable.__init__(self)
        self._name = name
        self._attack_modifier = attack_modifier
        self._uses = uses

    #######################################################
    # returns attack modifier
    #
    # @param self current object
    #
    # @return float attack modifier
    #######################################################
    def get_attack_modifier(self):
        return self._attack_modifier

    #######################################################
    # use weapon and check if out of uses
    #
    # @param self current object
    #######################################################
    def use(self):
        self._uses -= 1
        if self._uses <= 0:
            self.notify_observers("out_of_uses")

    #######################################################
    # returns weapon to string
    #
    # @param self current object
    #
    # @return string weapon to string
    #######################################################
    def to_string(self):
        return self._name + "\t\t\t" + str(self._uses)

    #######################################################
    # returns weapon name
    #
    # @param self current object
    #
    # @return string weapon name 
    #######################################################
    def get_name(self):
        return self._name

    #######################################################
    # returns weapon uses remaining
    #
    # @param self current object
    #
    # @return int number of uses
    #######################################################
    def get_uses(self):
        return self._uses

#######################################################
# hersheykiss class
#######################################################
class HersheyKiss(Weapon):

    #######################################################
    # constructor to initialize variables
    #
    # @param self current object
    #######################################################
    def __init__(self):
        Weapon.__init__(self, "HersheyKiss", 1.0, 1)

    #######################################################
    # use weapon
    #
    # @param self current object
    #######################################################
    def use(self):
        return

    #######################################################
    # returns weapon to string
    #
    # @param self current object
    #
    # @return string weapon to string
    #######################################################
    def to_string(self):
        return self._name + "\t\t\t∞"

#######################################################
# sourstraw class
#######################################################
class SourStraw(Weapon):

    #######################################################
    # constructor to initialize variables
    #
    # @param self current object
    #######################################################
    def __init__(self):
        Weapon.__init__(self, "SourStraw", random.random() * .75 + 1, 2)

#######################################################
# chocolatebar class
#######################################################
class ChocolateBar(Weapon):

    #######################################################
    # constructor to initialize variables
    #
    # @param self current object
    #######################################################
    def __init__(self):
        Weapon.__init__(self, "ChocolateBar", random.random() * .4 + 2, 4)

#######################################################
# nerdbomb class
#######################################################
class NerdBomb(Weapon):

    #######################################################
    # constructor to initialize variables
    #
    # @param self current object
    #######################################################
    def __init__(self):
        Weapon.__init__(self, "NerdBomb", random.random() * 1.5 + 3.5, 1)