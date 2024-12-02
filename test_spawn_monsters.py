from unittest import TestCase
from unittest.mock import patch
import game

.
class Test(TestCase):
    @patch('random.choice', return_value=(1, 1))
    def test_spawn_monsters_2X2(self, mock_choice):
        expected = (1, 1)
        actual = game.spawn_monsters(2, 2)
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value=(3, 2))
    def test_spawn_monsters_5X5(self, mock_choice):
        expected = (3, 2)
        actual = game.spawn_monsters(5, 5)
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value=(8, 9))
    def test_spawn_monsters_8X12(self, mock_choice):
        expected = (8, 9)
        actual = game.spawn_monsters(8, 12)
        self.assertEqual(expected, actual)