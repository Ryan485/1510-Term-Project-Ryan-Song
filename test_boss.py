from unittest import TestCase
from io import StringIO
from unittest.mock import patch
import game


class Test(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['y', 'n'])  # First 'y' to fight, then 'n' to end the game after dying
    @patch('time.sleep', return_value=None)  # To skip actual sleeping during tests
    def test_boss(self, mock_sleep, mock_input, mock_stdout):
        color = {
            "RED": "\033[91m",
            "GREEN": "\033[92m",
            "BLUE": "\033[94m",
            "MAGENTA": "\033[95m",
            "RESET": "\033[0m"
        }
        final_boss = {"Damage": 200, "HP": 2000}
        attributes = {"Damage": 300, "HP": 200, "EXP": 700, "X-coordinate": 2, "Y-coordinate": 2}
        coordinates = {
            (2, 2): "👾",  # Coordinate for the boss fight
            (0, 0): "🌲",  # Adding other necessary keys to avoid KeyError
            (0, 1): "🌲",
            (0, 2): "🌲",
            (0, 3): "🌲",
            (1, 0): "🌲",
            (1, 1): "🌲",
            (1, 2): "🌲",
            (1, 3): "🌲",
            (2, 0): "🌲",
            (2, 1): "🌲",
            (2, 2): "🌲"
        }

        # Call the boss function without printing the initial game state
        game.boss(coordinates, 3, 3, attributes, final_boss, color)

        actual = mock_stdout.getvalue().strip()
        expected = (
            "🌲  🌲  🌲  \n🌲  🌲  🌲  \n🌲  🌲  🌲"
        )

        self.assertEqual(expected, actual)
