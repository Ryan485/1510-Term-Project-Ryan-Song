from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import game
.

class Test(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_level_2_user_choice_1(self, mock_stdout):
        color = {"RESET": "\033[0m", "YELLOW": "\033[93m"}
        attributes = {"Level": 1, "EXP": 300, "Damage": 150, "HP": 100}
        game.level_2(attributes, "1", color)

        expected = (
            f"{color['YELLOW']}Congratulations! You are now Level 2!\n"
            f"At Level 2, Your character's stat is: "
            f"Damage | 200 | HP | 150{color['RESET']}\n\n"
        )

        actual = mock_stdout.getvalue()

        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_level_2_user_choice_2(self, mock_stdout):
        color = {"RESET": "\033[0m", "YELLOW": "\033[93m"}
        attributes = {"Level": 1, "EXP": 300, "Damage": 80, "HP": 150}
        game.level_2(attributes, "2", color)

        expected = (
            f"{color['YELLOW']}Congratulations! You are now Level 2!\n"
            f"At Level 2, Your character's stat is: "
            f"Damage | 100 | HP | 200{color['RESET']}\n\n"
        )

        actual = mock_stdout.getvalue()

        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_level_2_user_choice_3(self, mock_stdout):
        color = {"RESET": "\033[0m", "YELLOW": "\033[93m"}
        attributes = {"Level": 1, "EXP": 300, "Damage": 50, "HP": 200}
        game.level_2(attributes, "3", color)

        expected = (
            f"{color['YELLOW']}Congratulations! You are now Level 2!\n"
            f"At Level 2, Your character's stat is: "
            f"Damage | 70 | HP | 300{color['RESET']}\n\n"
        )

        actual = mock_stdout.getvalue()

        self.assertEqual(expected, actual)
