from random import choice
from game.player import Player
from game.story import Story


class Game:

    def __init__(self):
        # name = input('Name: ')
        name = 'flaae'
        self._player = Player(name)
        friend_name = ['Miranda', 'Bartolomeu']
        self._friend = [choice(friend_name)]
        self._day = 0
        self._story = Story()

    def next_day(self):
        print(self._friend)
        self._day += 1
        self._story.day(self._day)
