from random import choice, seed
from datetime import datetime as dt
from game.player import Player
from game.story import Story


class Game:

    def __init__(self, new_seed=None):
        # name = input('Name: ')
        name = 'flaae'
        self._player = Player(name)
        friend_name = ['Miranda', 'Bartolomeu']

        if not new_seed:
            new_seed = dt.now().microsecond
        seed(new_seed)
        self._seed = new_seed

        self._friend = choice(friend_name)  # enable more friends in the future
        self._day = 0
        self._story = Story()

    def next_day(self):
        print(self._friend)
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
        x = self == other
        if x is not NotImplemented:
            return not x
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(vars(self).items())))
