from game.vehicle import Vehicle


class Player:

    def __init__(
            self, name, vehicle, p_agi=1, p_str=1, p_health=10,
            gas=0, energy=100, food=10):
        self._name = name
        self._health = p_health
        self._agi = p_agi
        self._str = p_str
        self._experience = 0
        self._vehicle = vehicle

        # will later be a class
        self._gas = gas
        self._food = food
        self._energy = energy

    @classmethod
    def template(
            cls, name=None, energy_usage=None, initial_energy=100):
        resources = {'energy': initial_energy}
        if energy_usage is None:
            return cls(name, Vehicle.template(), **resources)
        return cls(name, Vehicle.template(energy_usage), **resources)

    # TODO If there's 5 gas left but needs to use 10, increase misfortune
    def travel(self):
        gas, food, energy = self._vehicle.get_usage()
        leave_vehicle = False
        died = False
        if gas:
            self._gas -= gas
            if self._gas < 0:
                leave_vehicle = True
                self._gas = 0
        self._food -= food
        if self._food < 0:
            energy += - self._food
            self._food = 0
        self._energy -= energy
        if self._energy < 0:
            died = self._lose_health(self._energy)
            self._energy = 0
        return leave_vehicle, died

    def get_health(self):
        '''test'''
        return self._health

    def _lose_health(self, amount):
        amount = abs(amount)
        self._health -= amount
        if self._health < 1:
            self._health = 0
            return True
        return False

    def get_xp(self):
        return self._experience

    def _xp_up(self):
        self._experience += 1

    def get_agi(self):
        return self._agi

    def __repr__(self):
        params = \
            f"('{self._name}', {self._vehicle}, {self._agi}, " + \
            f"{self._str}, {self._health}, {self._gas}, " + \
            f"{self._energy}, {self._food})"
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
