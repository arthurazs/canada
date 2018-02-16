class Story:

    def __init__(self):
        ''''''

    def day(self, day):
        presentation = 'The world is in chaos.\n'
        return presentation

    def __repr__(self):
        params = f"()"
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
