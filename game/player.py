from game.backpack import Backpack
from game.vehicle import Vehicle


class Player:

    def __init__(self, name, p_agi=1, p_str=1, p_health=10):
        self._name = name
        self._health = p_health
        self._agi = p_agi
        self._str = p_str
        self._experience = 0
        self._backpack = Backpack()
        self._vehicle = Vehicle.car()

    def get_health(self):
        '''test'''
        return self._health

    def _lose_health(self):
        if self._health > 0:
            self._health -= 1
        if self._health < 1:
            return True
        return False

    def get_xp(self):
        return self._experience

    def _xp_up(self):
        self._experience += 1

    def get_agi(self):
        return self._agi

    def attack(self, enemy):
        hit = False
        killed = False

        if self._agi > enemy.get_agi():
            if self._str > 0:
                killed = enemy._lose_health()
                if killed:
                    self._xp_up()
            hit = True
        return hit, killed

    def __repr__(self):
        params = f"('{self._name}', {self._agi}, {self._str}, {self._health})"
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
