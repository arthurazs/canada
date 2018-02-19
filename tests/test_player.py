import unittest
from game.player import Player, Vehicle  # NOQA


class TestPlayer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''Sets up player'''
        cls.player = Player.template('Arthur')
        cls.same = eval(repr(cls.player))
        cls.other = Player.template()

    def test_creation(self):
        '''Player Creation [#P1]'''
        self.assertEqual(self.player, self.same)

    def test_not_equal(self):
        '''Player not equal to other [#P2]'''
        self.assertNotEqual(self.player, self.other)

    def test_hash(self):
        '''Player hash [#P3]'''
        expected = hash(self.player)
        result = hash(self.same)
        self.assertEqual(expected, result)

    def test_travel(self):
        '''Player hash [#P4]'''
        another = Player.template(initial_energy=1, energy_usage=10)
        before = another.get_health()
        another.travel()
        after = another.get_health()
        self.assertTrue(before > after)


if __name__ == '__main__':
    unittest.main()
