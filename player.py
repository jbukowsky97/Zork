import random

from observe import Observer

from weapons import Weapon, HersheyKiss, SourStraw, ChocolateBar, NerdBomb

#######################################################
# class to hold instance of player in game
#
# @parent Observer
#######################################################
class Player(Observer):

    #######################################################
    # constructor to initialize player
    #
    # @param self current object
    # @param row row loc of the player in the neighborhood
    # @param col col loc of the player in the neighborhood
    #######################################################
    def __init__(self, row, col):
        self._hp = random.randint(0, 50) + 300
        self._atk = random.randint(0, 10) + 10
        self._row = row
        self._col = col
        #list of 0-10 weapons
        self._weapons = []
        weapon_types = "SCN"
        self._weapons.append(HersheyKiss())
        for i in range(0, 9):
            weapon = None
            rand_weapon = random.choice(weapon_types)
            if rand_weapon == "S":
                weapon = SourStraw()
            elif rand_weapon == "C":
                weapon = ChocolateBar()
            elif rand_weapon == "N":
                weapon = NerdBomb()
            weapon.add_observer(self)
            self._weapons.append(weapon)
    
    #######################################################
    # removes weapon from list of observers
    #
    # @param self current object
    # @param observable object calling update
    # @param msg message being sent by the observable object
    #######################################################
    def update(self, observable, msg):
        observable.remove_observer(self)
        self._weapons.remove(observable)
    
    #######################################################
    # moves player in the direction specified, if
    # 0 <= new_row < rows && 0 <= new_col < cols
    #
    # @param self current object
    # @param move_str string containing direction to move
    # @param rows number of rows in neighborhood
    # @param cols number of cols in neighborhood
    #
    # @return boolean True if move was successful
    #######################################################
    def move(self, move_str, rows, cols):
        if move_str == "move north":
            if self._row <= 0:
                return False
            else:
                self._row -= 1
        elif move_str == "move south":
            if self._row >= rows - 1:
                return False
            else:
                self._row += 1
        elif move_str == "move east":
            if self._col >= cols - 1:
                return False
            else:
                self._col += 1
        elif move_str == "move west":
            if self._col <= 0:
                return False
            else:
                self._col -= 1
        return True

    #######################################################
    # attacks current home
    #
    # attack consists of:
    #   for every monster in home
    #     player attack monster, if monster is still alive,
    #     monster attack player back
    #     (if player dies during fight, fight stops)
    #
    # @param self current object
    # @param home home object being attacked
    # @param weapon being used to attack
    #######################################################
    def attack(self, home, weapon):
        monsters_home = list(home.get_monsters())
        for monster in monsters_home:
            dmg_given_turn = monster.calculate_damage_taken(self._atk, weapon)
            if monster.get_hp() <= 0:
                print("You did %d damage, killing the %s" % (dmg_given_turn, monster.get_type()))
            else:
                print("You did %d damage to the %s, leaving it wth %d health" % (dmg_given_turn, monster.get_type(), monster.get_hp()))
                dmg_taken_turn = monster.generate_attack()
                self._hp -= dmg_taken_turn
                if self._hp <= 0:
                    print("%s hit you for %d damage, killing you" % (monster.get_type(), dmg_taken_turn))
                    return
                else:
                    print("%s hit you for %d damage, you have %d health remaining" % (monster.get_type(), dmg_taken_turn, self._hp))
            print("\n")
        return

    #######################################################
    # return if player is dead
    #
    # @param self current object
    #
    # @return boolean True if player is dead
    #######################################################
    def is_dead(self):
        return (self._hp <= 0)

    #######################################################
    # return player row
    #
    # @param self current object
    #
    # @return int player row
    #######################################################
    def get_row(self):
        return self._row

    #######################################################
    # return player col
    #
    # @param self current object
    #
    # @return int player col
    #######################################################
    def get_col(self):
        return self._col

    #######################################################
    # return player hp
    #
    # @param self current object
    #
    # @return int player hp
    #######################################################
    def get_hp(self):
        return self._hp

    #######################################################
    # return player attack
    #
    # @param self current object
    #
    # @return float player attack
    #######################################################
    def get_atk(self):
        return self._atk

    #######################################################
    # return player weapons
    #
    # @param self current object
    #
    # @return list(Weapon) player weapons
    #######################################################
    def get_weapons(self):
        return self._weapons