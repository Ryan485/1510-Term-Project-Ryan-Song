from unittest import TestCase
from unittest.mock import patch
import game
from io import StringIO
import re


class Test(TestCase):
    @patch('sys.stdout', new_callable=StringIO)  # Capture stdout to check printed output
    def test_battle_field_1(self, mock_stdout):
        coordinates = {
            (0, 0): '🌲', (0, 1): '🌲', (0, 2): '🌲',
            (1, 0): '🌲', (1, 1): '💂‍', (1, 2): '🌲',
            (2, 0): '🌲', (2, 1): '🌲', (2, 2): '🌲'
        }
        color = {"RESET": "\033[0m"}
        monsters = (1, 0)

        expected = (
            "🌲  🌲  🌲  \n"
            "👹  💂‍  🌲  \n"
            "🌲  🌲  🌲  \n"
        )

        game.battle_field(coordinates, 3, 3, color, monsters)
        actual = mock_stdout.getvalue()
        actual = re.sub(r'\033\[[0-9;]*m', '', actual)

        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)  # Capture stdout to check printed output
    def test_battle_field_2(self, mock_stdout):
        coordinates = {
            (0, 0): '🌲', (0, 1): '🌲', (0, 2): '🌲',
            (1, 0): '🌲', (1, 1): '💂‍', (1, 2): '🌲',
            (2, 0): '🌲', (2, 1): '🌲', (2, 2): '🌲'
        }
        color = {"RESET": "\033[0m"}
        monsters = (0, 2)

        expected = (
            "🌲  🌲  👹  \n"
            "🌲  💂‍  🌲  \n"
            "🌲  🌲  🌲  \n"
        )

        game.battle_field(coordinates, 3, 3, color, monsters)
        actual = mock_stdout.getvalue()
        actual = re.sub(r'\033\[[0-9;]*m', '', actual)

        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)  # Capture stdout to check printed output
    def test_battle_field_3(self, mock_stdout):
        coordinates = {
            (0, 0): '🌲', (0, 1): '🌲', (0, 2): '🌲',
            (1, 0): '🌲', (1, 1): '💂‍', (1, 2): '🌲',
            (2, 0): '🌲', (2, 1): '🌲', (2, 2): '🌲'
        }
        color = {"RESET": "\033[0m"}
        monsters = (2, 2)

        expected = (
            "🌲  🌲  🌲  \n"
            "🌲  💂‍  🌲  \n"
            "🌲  🌲  👹  \n"
        )

        game.battle_field(coordinates, 3, 3, color, monsters)
        actual = mock_stdout.getvalue()
        actual = re.sub(r'\033\[[0-9;]*m', '', actual)

        self.assertEqual(expected, actual)
