from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import game


class Test(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_level_3_user_choice_1(self, mock_stdout):
        color = {"RESET": "\033[0m", "YELLOW": "\033[93m"}
        attributes = {"Level": 2, "EXP": 700, "Damage": 200, "HP": 150}
        game.level_3(attributes, "1", color)

        expected = (
            f"\n{color['YELLOW']}Congratulations! You are now Level 3!\n"
            f"At Level 3, your character's stat is: "
            f"Damage | 300 | HP | 200{color['RESET']}\n\n"
        )

        actual = mock_stdout.getvalue()

        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_level_3_user_choice_2(self, mock_stdout):
        color = {"RESET": "\033[0m", "YELLOW": "\033[93m"}
        attributes = {"Level": 2, "EXP": 700, "Damage": 100, "HP": 200}
        game.level_3(attributes, "2", color)

        expected = (
            f"\n{color['YELLOW']}Congratulations! You are now Level 3!\n"
            f"At Level 3, your character's stat is: "
            f"Damage | 140 | HP | 400{color['RESET']}\n\n"
        )

        actual = mock_stdout.getvalue()

        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_level_3_user_choice_3(self, mock_stdout):
        color = {"RESET": "\033[0m", "YELLOW": "\033[93m"}
        attributes = {"Level": 2, "EXP": 700, "Damage": 70, "HP": 300}
        game.level_3(attributes, "3", color)

        expected = (
            f"\n{color['YELLOW']}Congratulations! You are now Level 3!\n"
            f"At Level 3, your character's stat is: "
            f"Damage | 110 | HP | 500{color['RESET']}\n\n"
        )

        actual = mock_stdout.getvalue()

        self.assertEqual(expected, actual)