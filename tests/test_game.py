import unittest
from game.game import Game


class TestGame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''Sets up game'''
        cls.game = Game(new_seed=1)
        cls.same = eval(repr(cls.game))
        cls.other = Game(new_seed=2)

    def test_creation(self):
        '''Game Creation [#G1]'''
        self.assertEqual(self.game, self.same)

    def test_not_equal(self):
        '''Game not equal to other [#G2]'''
        self.assertNotEqual(self.game, self.other)

    def test_hash(self):
        '''Game hash [#G3]'''
        expected = hash(self.game)
        result = hash(self.same)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
