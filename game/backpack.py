class Backpack:

    def __init__(self):
        pass

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
