from random import choice, seed
from datetime import datetime as dt
from game.player import Player
from game.vehicle import Vehicle
from importlib import import_module


class Game:

    def __init__(self, new_seed=None, database='game.data.base'):
        self._base = import_module(database)

        name = 'flaae'
        self._player = Player(name, Vehicle.from_dic(self._base.foot))

        if not new_seed:
            new_seed = dt.now().microsecond
        seed(new_seed)
        self._seed = new_seed

        self._day = 0

        self._current_location = None

    def start(self):
        self._day += 1
        place = choice(self._base.places)
        print(self._current_location)
        self.change_location(place)
        print(self._current_location)

    def change_location(self, new_location):
        leave_vehicle = self._player.travel()
        if not leave_vehicle:
            self._current_location = new_location

    def next_day(self):
        self._day += 1
        self._story.day(self._day)

    def __repr__(self):
        params = f'({self._seed})'
        return self.__class__.__name__ + params

    def __eq__(self, other):
        if isinstance(self, type(other)):
            return vars(self) == vars(other)
        return NotImplemented

    def __ne__(self, other):
        equal = self == other
        if equal is not NotImplemented:
            return not equal
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(vars(self).items())))
