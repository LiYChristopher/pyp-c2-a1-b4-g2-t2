'''
Build a battleship game. It has to work in the console. You don"t need any
external libraries, you can make it work just using plain python. Youd play
against the console. The game will have 2 play modes: attack and defence.
'''


class Grid(object):
    ''' Grid class, our ocean where our fleet will reside:
        it will be a 10 by 10 square grid
        A1 B1 C1 D1 E1 F1 G1 H1 I1 J1
        A2 etc..
        A3 etc
        ...
        A10 B10 C10 D10 E10 F10 G10 H10 I10 J10
    '''
    def __init__(self, humanPlayer, computerPlayer):
        self._inputs = [i + str(j) for i in map(chr, range(65, 75)) for j in range(1, 11)]
        self.board = {i: ' ' for i in self._inputs}

        print self._inputs


class Ship(object):

    total_ships = 0

    def __init__(self, orientation, count):
        self.orientation = orientation
        self.count = count
        super(Ship, self).__init__()

class Aircraft(Ship):
    def __init__(self, orientation, count):
        self.size = 5
        self.orientation = orientation
        self.count = count

class Submarine(Ship):
    def __init__(self, orientation, count):
        self.size = 3
        self.orientation = orientation
        self.count = count

class Player(object):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':

    test = Aircraft()
    print test.orientation
    print test.count
