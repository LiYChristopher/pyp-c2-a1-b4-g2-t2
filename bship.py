''' implementing battleship
'''
from collections import OrderedDict
from random import randint


class Grid(object):
    ''' setting up the grid for the game
    '''
    def __init__(self):
        self._inputs = [i+str(j) for i in map(chr, range(65, 75))
                        for j in range(1, 11)]
        self.grid = OrderedDict(zip(self._inputs, [' ']*len(self._inputs)))

    def __repr__(self):
        return 'Grid({})'.format(self.grid)

    def __str__(self):
        ''' Need to implement a way to show the grid in a good format
        '''
        return str(self.grid)

    def _allocator(self, orientation_id, px, py, ship):
        ''' helper method to allocate ships in the grid
        '''
        if orientation_id in ['h', 'horizontal']:
            allocation = [py + str(i) for i in range(px, px + ship.size)]
        elif orientation_id in ['v', 'vertical']:
            allocation = [chr(i) + str(px) for i in
                          range(ord(py), ord(py) + ship.size)]
        else:
            raise OrientationError("That's not proper orientation")
        for loc in allocation:
            self.grid[loc] = ship.marker

    def place(self, ships):
        ''' takes in a list of ships and places them on the grid if ships fit
            otherwise throws and OutOfBoundsError.
            #TODO: Need to implement this
        '''
        for ship in ships:
            place_y = ship.position[0].capitalize()
            place_x = int(ship.position[1])
            self._allocator(ship.orientation.lower(), place_x, place_y, ship)
        return self.grid


class OrientationError(Exception):
    ''' raise orientation error if ships placed weirdly
    '''
    pass


class OutOfBoundsError(Exception):
    ''' if ship size exceeds the bounds raise this error
    '''
    pass


class Ship(object):
    ''' Base ship class
    '''
    def __init__(self, count, position, orientation):
        self.count = count
        self.position = position
        self.orientation = orientation

    def __repr__(self):
        # nice to have a repr which shows the actual subclass names
        return '{cls}({c}, {p}, {o})'.format(cls=self.__class__.__name__,
                                             c=self.count, p=self.position,
                                             o=self.orientation)


class Aircraft(Ship):
    ''' Aircraft class
    '''
    def __init__(self, count, position, orientation):
        super(Aircraft, self).__init__(count, position, orientation)
        self.marker = 'A'
        self.size = 5


class Submarine(Ship):
    ''' Submarine class
    '''
    def __init__(self, count, position, orientation):
        super(Submarine, self).__init__(count, position, orientation)
        self.marker = 'S'
        self.size = 3


class PatrolBoat(Ship):
    ''' PatrolBoat class
    '''
    def __init__(self, count, position, orientation):
        super(PatrolBoat, self).__init__(count, position, orientation)
        self.marker = 'P'
        self.size = 2


def show_available_ships():
    ''' creates random number of aircrafts, submarines and patrol boats
    '''
    max_ships = 5
    num_a, num_s, num_pb = 0, 0, 0
    while (num_a + num_s + num_pb) != max_ships:
        num_a = randint(1, 2)       # max aircrafts = 2
        num_s = randint(1, 3)       # max submarines = 3
        num_pb = randint(1, 4)      # max patrolboats = 4
    print 'You have:'
    print '{} Aircraft (size = 5)'.format(num_a)
    print '{} Submarine (size = 3)'.format(num_s)
    print '{} Patrol Boat (size = 2)'.format(num_pb)
    # offsetting numbers with +1 for correct values as range starts at 1
    return num_a+1, num_s+1, num_pb+1


def choose_ships(numa, nums, numpb):
    ship_list = []
    for i in range(1, numa):
        aircraft_input = raw_input('Pos, Orient for Aircraft #{}: '.
                                   format(i))
        a_pos, a_orient = map(str.strip, aircraft_input.split(','))
        ship_list.append(Aircraft(i, a_pos, a_orient))

    for j in range(1, nums):
        submarines_input = raw_input('Pos, Orient for Sub #{}: '.
                                     format(j))
        s_pos, s_orient = map(str.strip, submarines_input.split(','))
        ship_list.append(Submarine(j, s_pos, s_orient))

    for k in range(1, numpb):
        patrol_input = raw_input('Pos, Orient for Patrol Boat #{}: '.
                                 format(k))
        pb_pos, pb_orient = map(str.strip, patrol_input.split(','))
        ship_list.append(PatrolBoat(k, pb_pos, pb_orient))

    return ship_list


def initialize():
    g = Grid()
    numa, nums, numpb = show_available_ships()
    print g.grid
    g.place(choose_ships(numa, nums, numpb))
    print g.grid

if __name__ == '__main__':
    initialize()
