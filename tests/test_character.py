import unittest
from game.character import Character


class TestCharacter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''Sets up character'''
        cls.character = Character('Arthur')
        cls.same = eval(repr(cls.character))
        cls.other = Character('Other')

    def test_creation(self):
        '''Character Creation [#P1]'''
        self.assertEqual(self.character, self.same)

    def test_not_equal(self):
        '''Character not equal to other [#P2]'''
        self.assertNotEqual(self.character, self.other)

    def test_hash(self):
        '''Character hash [#P3]'''
        expected = hash(self.character)
        result = hash(self.same)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
