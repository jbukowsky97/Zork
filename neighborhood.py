from home import Home

#######################################################
# neighborhood class
#######################################################
class Neighborhood:

    #######################################################
    # constructor to initialize variables
    #
    # @param self current object
    # @param rows number of rows in neighborhood
    # @param cols number of cols in neighborhood
    #######################################################
    def __init__(self, rows, cols):
        self._homes = []
        self._rows = rows
        self._cols = cols
        for row in range(0, rows):
            self._homes.append([])
            for col in range(0, cols):
                self._homes[row].append(Home())

    #######################################################
    # returns number of rows
    #
    # @param self current object
    #
    # @return int number of rows
    #######################################################
    def get_rows(self):
        return self._rows

    #######################################################
    # returns number of cols
    #
    # @param self current object
    #
    # @return int number of cols
    #######################################################
    def get_cols(self):
        return self._cols

    #######################################################
    # returns home at row col specified
    #
    # @param self current object
    # @param row x index
    # @param col y index
    #
    # @return home home at row col
    #######################################################
    def get_home(self, row, col):
        return self._homes[row][col]