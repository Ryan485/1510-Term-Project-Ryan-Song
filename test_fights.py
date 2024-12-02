from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import game

.
class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('random.random', return_value=0.1)
    @patch('sys.stdout', new_callable=StringIO)
    @patch('game.monster_list', new_callable=lambda: [(2, 3)])
    @patch('builtins.input', return_value="y")
    def test_fights_answer_yes(self, mock_input, mock_monster_list, mock_stdout, mock_sleep, mock_random):
        color = {
            "RED": "\033[91m",
            "YELLOW": "\033[93m",
            "BLUE": "\033[94m",
            "MAGENTA": "\033[95m",
            "RESET": "\033[0m",
        }
        attributes = {"X-coordinate": 2, "Y-coordinate": 3, "HP": 200, "Damage": 50, "EXP": 0}
        monster_info = {"HP": 200, "Damage": 20}

        game.fights(color, attributes, monster_info)

        actual = mock_stdout.getvalue()

        expected = (
            f"\n{color['RED']}You encountered a monster! Prepare for battle!\n\n"
            f"{color['MAGENTA']}You've attacked the monster! Their HP is now 150.\n"
            f"{color['RED']}You've got attacked by the monster! Your HP is now 180!\n"
            f"{color['MAGENTA']}You've attacked the monster! Their HP is now 100.\n"
            f"{color['RED']}You've got attacked by the monster! Your HP is now 160!\n"
            f"{color['MAGENTA']}You've attacked the monster! Their HP is now 50.\n"
            f"{color['RED']}You've got attacked by the monster! Your HP is now 140!\n"
            f"{color['MAGENTA']}You've attacked the monster! Their HP is now 0.\n"
            f"\n{color['YELLOW']}You've defeated the monster!\n\n"
            f"You've earned 100 EXP! Your total EXP is: 100EXP.\n"
        )

        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="n")
    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=StringIO)
    def test_fights_answer_no(self, mock_stdout, mock_sleep, mock_input):
        color = {"BLUE": "\033[94m", "RESET": "\033[0m", "RED": "\033[91m"}
        attributes = {"X-coordinate": 2, "Y-coordinate": 3, "HP": 200, "Damage": 50, "EXP": 0}
        monster_info = {"HP": 200, "Damage": 20}

        game.monster_list = [(2, 3)]

        game.fights(color, attributes, monster_info)

        actual = mock_stdout.getvalue()

        expected = (
            f"\n{color['RED']}You encountered a monster! Prepare for battle!\n\n"
            f"{color['BLUE']}You've just passed the monster!{color['RESET']}\n\n"
            )

        self.assertEqual(expected, actual)