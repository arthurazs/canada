import unittest
from game.player import Player


class TestPlayer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''Sets up player'''
        cls.player = Player('Arthur')
        cls.same = eval(repr(cls.player))
        cls.other = Player('Other')

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


class TestBattle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''Sets up player'''
        cls.player = Player('Hero', 2)
        cls.weak = Player('Weak', 2, 0)
        cls.enemy = Player('Villain')
        cls.dying = Player('Dying', p_health=1)

    def test_hit(self):
        '''Player hits enemy [#B1]'''
        enemy_health_before = self.enemy.get_health()
        enemy_hit, enemy_killed = self.player.attack(self.enemy)
        enemy_lost_health = enemy_health_before > self.enemy.get_health()
        result = enemy_hit & enemy_lost_health & (not enemy_killed)
        self.assertTrue(result)

    def test_miss(self):
        '''Player misses enemy [#B2]'''
        enemy_health_before = self.player.get_health()
        enemy_hit, _ = self.enemy.attack(self.player)
        enemy_lost_health = enemy_health_before > self.enemy.get_health()
        result = not enemy_hit & (not enemy_lost_health)
        self.assertTrue(result)

    def test_no_damage(self):
        '''Player hits but doesn't do damage [#B3]'''
        enemy_health_before = self.enemy.get_health()
        enemy_hit, _ = self.weak.attack(self.enemy)
        enemy_lost_health = enemy_health_before > self.enemy.get_health()
        result = enemy_hit & (not enemy_lost_health)
        self.assertTrue(result)

    def test_kill(self):
        '''Player kills enemy [#B4]'''
        player_xp = self.player.get_xp()
        enemy_hit, enemy_killed = self.player.attack(self.dying)
        xped_up = player_xp < self.player.get_xp()
        result = enemy_hit & enemy_killed & xped_up
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
