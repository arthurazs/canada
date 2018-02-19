import unittest
from game.vehicle import Vehicle
import game.data.base as base


class TestVehicle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''Sets up vehicle'''
        cls.vehicle = Vehicle.from_dic(base.car)
        cls.same = eval(repr(cls.vehicle))
        cls.other = Vehicle(0, 4, 8)

    def test_creation(self):
        '''Vehicle Creation [#V1]'''
        self.assertEqual(self.vehicle, self.same)

    def test_not_equal(self):
        '''Vehicle not equal to other [#V2]'''
        self.assertNotEqual(self.vehicle, self.other)

    def test_hash(self):
        '''Vehicle hash [#V3]'''
        expected = hash(self.vehicle)
        result = hash(self.same)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
