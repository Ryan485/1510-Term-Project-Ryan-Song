from unittest import TestCase
import game


class Test(TestCase):
    def test_monster_attributes(self):
        expected = {"HP": 500, "Damage": 20}
        actual = game.monster_attributes()
        self.assertEqual(expected, actual)
