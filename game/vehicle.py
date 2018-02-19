class Vehicle:

    def __init__(self, gas, food, energy):
        self._gas = gas
        self._food = food
        self._energy = energy

    @classmethod
    def template(cls, energy=0):
        return cls(0, 0, energy)

    @classmethod
    def from_dic(cls, dictionary):
        usage = dictionary['usage']
        gas = usage['gas']
        food = usage['food']
        energy = usage['energy']
        return cls(gas, food, energy)

    def get_usage(self):
        return self._gas, self._food, self._energy

    def __repr__(self):
        params = f'({self._gas}, {self._food}, {self._energy})'
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
