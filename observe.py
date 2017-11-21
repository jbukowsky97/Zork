#######################################################
# observer class
#######################################################
class Observer:

    #######################################################
    # process update from observable
    #
    # @param self current object
    # @param observable object calling update
    # @param msg message object is sending
    #######################################################
    def update(self, observable, msg):
        pass

#######################################################
# observable class
#######################################################
class Observable:

    #######################################################
    # constructor to initialize variables
    #
    # @param self current object
    #######################################################
    def __init__(self):
        #list of observers
        self._observers = []
        self._changed = False

    #######################################################
    # adds observer to list of observers
    #
    # @param self current object
    # @param observer object being added
    #######################################################
    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    #######################################################
    # removes observer from list of observers
    #
    # @param self current object
    # @param observer object being removed
    #######################################################
    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    #######################################################
    # notifies all observers of object
    #
    # @param self current object
    # @param msg message being sent
    #######################################################
    def notify_observers(self, msg):
        for observer in self._observers:
            observer.update(self, msg)