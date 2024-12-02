from unittest import TestCase
import game


class Test(TestCase):
    def test_boss_attributes(self):
        expected = {"Damage": 200, "HP": 2000}
        actual = game.boss_attributes()
        self.assertEqual(expected, actual)/
