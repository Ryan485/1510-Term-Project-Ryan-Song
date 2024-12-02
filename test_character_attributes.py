from unittest import TestCase
import game
.

class Test(TestCase):
    def test_character_attributes_1(self):
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "HP": 100, "Damage": 150, "Level": 1, "EXP": 0}
        actual = game.character_attributes("1")
        self.assertEqual(expected, actual)

    def test_character_attributes_2(self):
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "HP": 150, "Damage": 80, "Level": 1, "EXP": 0}
        actual = game.character_attributes("2")
        self.assertEqual(expected, actual)

    def test_character_attributes_3(self):
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "HP": 200, "Damage": 50, "Level": 1, "EXP": 0}
        actual = game.character_attributes("3")
        self.assertEqual(expected, actual)
