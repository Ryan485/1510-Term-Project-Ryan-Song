from unittest import TestCase
import game


class Test(TestCase):
    def test_valid_move_1(self):
        attributes = {"X-coordinate": 0, "Y-coordinate": 0, "HP": 100, "Damage": 150, "Level": 1, "EXP": 0}
        result = game.valid_move(attributes, 5, 5, "1")
        self.assertFalse(result)

    def test_valid_move_2(self):
        attributes = {"X-coordinate": 0, "Y-coordinate": 0, "HP": 200, "Damage": 50, "Level": 1, "EXP": 0}
        result = game.valid_move(attributes, 5, 5, "2")
        self.assertTrue(result)

    def test_valid_move_3(self):
        attributes = {"X-coordinate": 0, "Y-coordinate": 0, "HP": 150, "Damage": 80, "Level": 1, "EXP": 0}
        result = game.valid_move(attributes, 5, 5, "3")
        self.assertFalse(result)

    def test_valid_move_4(self):
        attributes = {"X-coordinate": 0, "Y-coordinate": 0, "HP": 150, "Damage": 80, "Level": 1, "EXP": 0}
        result = game.valid_move(attributes, 5, 5, "4")
        self.assertTrue(result)
