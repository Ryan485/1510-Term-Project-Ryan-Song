from unittest import TestCase
import game


class Test(TestCase):
    def test_monster_list(self):
        expected = []
        actual = game.monster_list()
        self.assertEqual(expected, actual)
