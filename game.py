import re

from neighborhood import Neighborhood
from home import Home
from monsters import *
from weapons import *
from player import Player

#######################################################
# class that creates and manages a Game object
#######################################################

class Game:

    #######################################################
    # constructor to initialize variables
    #
    # @param self current object
    #######################################################
    def __init__(self):
        self._player = Player(0, 0)
        self._neighborhood = Neighborhood(5, 5)
        self._game_active = True
        print("You wake up on Halloween and discover that the world")
        print("is not how you left it. Batches of bad candy have transformed")
        print("your friends and neighbors into all sorts of crazy monsters.")
        print("Somehow you missed the tainted candy; it is therefore up to")
        print("you to save your neighborhood and turn everyone back to normal.")
        print()
        print("type \"help\" for instructions")
        print()

    #######################################################
    # loop that executes during entire life-cycle of game
    #
    # @param self current object
    #######################################################
    def game_loop(self):
        while (self._game_active):
            print(">\t", end="")
            user_input = input().lower()
            move_pattern = re.compile("move ((north)|(south)|(east)|(west))")
            if move_pattern.fullmatch(user_input) != None:
                self.game_move(user_input)
            elif user_input == "attack":
                if self.game_attack():
                    self._game_active = False
                    break
            elif user_input == "map":
                self.game_map()
            elif user_input == "stats":
                self.game_stats()
            elif user_input == "help":
                self.game_help()
            elif user_input == "exit":
                if self.game_exit():
                    self._game_active = False
                    break
            else:
                self.game_unknown()

    #######################################################
    # sub-function to handle user entering move command
    #
    # regex on call prevents any errors here
    #
    # @param self current object
    # @param user_input string the user entered
    #######################################################
    def game_move(self, user_input):
        print("\n")
        if self._player.move(user_input, self._neighborhood.get_rows(), self._neighborhood.get_cols()):
            print("moved %s" % user_input[5:])
            self.game_map()
        else:
            print("could not move %s" % user_input[5:])
        print("\n")

    #######################################################
    # sub-function to handle user entering attack command
    #
    # @param self current object
    #
    # @return boolean True if player has died
    #######################################################
    def game_attack(self):
        print("\n")
        num_weapons = len(self._player.get_weapons())
        weapons_regex = None
        if num_weapons >= 10:
            weapons_regex = re.compile("(10)|[1-9]")
        else:
            weapons_regex = re.compile("[1-%d]" % num_weapons)    
        while True:
            print("choose weapon:")
            print()
            print("\tindex\tweapon\t\t\tatk_modifier\t\tuses")
            index = 1
            for weapon in self._player.get_weapons():
                print("\t%d.\t%s\t\t%f\t\t%d" % (index, weapon.get_name(), weapon.get_attack_modifier(), weapon.get_uses()))
                index += 1
            print("\n")
            print(">\t", end="")
            user_input = input().lower()
            if weapons_regex.fullmatch(user_input) != None:
                break
            else:
                print()
                print("choose a valid number corresponding to desired weapon")
                print()
        weapon = self._player.get_weapons()[int(user_input) - 1]
        self._player.attack(self._neighborhood.get_home(self._player.get_row(), self._player.get_col()), weapon)
        weapon.use()
        return self._player.is_dead()

    #######################################################
    # sub-function to handle user entering map command
    #
    # draws neighborhood to standard out
    #
    # @param self current object
    #######################################################
    def game_map(self):
        print("\n")
        for row in range(0, self._neighborhood.get_rows()):
            for col in range(0, self._neighborhood.get_cols()):
                print(" ------ \t", end="")
            print()
            for col in range(0, self._neighborhood.get_cols()):
                if self._player.get_row() == row and self._player.get_col() == col:
                    print("|  \\/  |\t", end="")
                else:
                    print("|      |\t", end="")
            print()
            for col in range(0, self._neighborhood.get_cols()):
                if self._player.get_row() == row and self._player.get_col() == col:
                    print("|  /\\  |\t", end="")
                else:
                    print("|      |\t", end="")
            print()
            for col in range(0, self._neighborhood.get_cols()):
                print(" ------ \t", end="")
            print()
            for col in range(0, self._neighborhood.get_cols()):
                print("People: %d\t" % self._neighborhood.get_home(row, col).get_people(), end="")
            print()
            for col in range(0, self._neighborhood.get_cols()):
                print("Zombies: %d\t" % self._neighborhood.get_home(row, col).get_zombies(), end="")
            print()
            for col in range(0, self._neighborhood.get_cols()):
                print("Vampires: %d\t" % self._neighborhood.get_home(row, col).get_vampires(), end="")
            print()
            for col in range(0, self._neighborhood.get_cols()):
                print("Ghouls: %d\t" % self._neighborhood.get_home(row, col).get_ghouls(), end="")
            print()
            for col in range(0, self._neighborhood.get_cols()):
                print("Werewolves: %d\t" % self._neighborhood.get_home(row, col).get_werewolves(), end="")
            print("\n")
        print("\\/")
        print("/\\ ---> (player location)")
        print("\n")

    #######################################################
    # sub-function to handle user entering stats command
    #
    # prints out current stats of character and surroundings
    #
    # @param self current object
    #######################################################
    def game_stats(self):
        print("\n")
        print("player:")
        print("\thp:\t\t\t\t" + str(self._player.get_hp()))
        print("\tattack:\t\t\t\t" + str(self._player.get_atk()))
        print("inventory:")
        print("\tweapon\t\t\t\tuses")
        print()
        for weapon in self._player.get_weapons():
            print("\t" + weapon.to_string())
        print("\n")

    #######################################################
    # sub-function to handle user entering help command
    #
    # prints out help page
    #
    # @param self current object
    #######################################################
    def game_help(self):
        print("\n")
        print("instructions:")
        print("\tmove [north|south|east|west]   move houses in direction")
        print("\tattack                         attack current house")
        print("\tmap                            print out map with stats")
        print("\tstats                          displays information about game and player")
        print("\thelp                           print help page")
        print("\texit                           exit game")
        print("\n")

    #######################################################
    # sub-function to handle user entering exit command
    #
    # exits game
    #
    # @param self current object
    #######################################################
    def game_exit(self):
        print("\n")
        print("exiting...")
        print("\n")
        return True

    #######################################################
    # sub-function to handle user entering an unkown command
    #
    # @param self current object
    #######################################################
    def game_unknown(self):
        print("\n")
        print("unknown command")
        print("\n")

#######################################################
# function to create and run a game object when ran
#######################################################
if __name__ == "__main__":
    game = Game()
    game.game_loop()