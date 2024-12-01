from unittest import TestCase
from unittest.mock import patch
from io import StringIO

import game


class Test(TestCase):
    @patch("time.sleep", return_value=None)
    @patch("sys.stdout", new_callable=StringIO)
    def test_description_output(self, mock_stdout, mock_sleep):
        mock_color = {
            "YELLOW": "\033[93m",
            "BLUE": "\033[94m",
            "MAGENTA": "\033[95m",
            "RESET": "\033[0m",
        }

        game.description(mock_color)

        actual = mock_stdout.getvalue()

        expected = (
            "\033[93mWelcome to our Dungeon! Your mission is to kill monsters as many as possible!\n"
            "Before we continue, you have to choose a character.\n"
            "Each character has their own unique skills. Choose the character that matches your play style!\n\n"
            "\033[94mPlease choose your character.\n"
            "\033[95m1. Ranger - Damage: 150 | HP: 100\n"
            "2. Wolverine - Damage: 80 | HP: 150\n"
            "3. Axeman - Damage: 50 | HP: 200\n\n"
        )

        self.assertEqual(actual, expected)
