import unittest
from game.story import Story


class TestStory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''Sets up story'''
        cls.story = Story()
        cls.same = eval(repr(cls.story))

    def test_creation(self):
        '''Story Creation [#S1]'''
        self.assertEqual(self.story, self.same)

    def test_hash(self):
        '''Story hash [#S2]'''
        expected = hash(self.story)
        result = hash(self.same)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
