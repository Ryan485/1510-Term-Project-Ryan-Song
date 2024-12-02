from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import time
import game.


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=StringIO)
    def test_boss_description(self, mock_stdout, mock_time):
        color = {"GREEN": "\033[92m",
                 "YELLOW": "\033[93m",
                 "BLUE": "\033[94m",
                 "MAGENTA": "\033[95m",
                 "RESET": "\033[0m"}

        expected = (f"{color['GREEN']}Now that you have reached our MAX Level, "
                    f"you need to defeat our final boss to finish this game.\n\n"
                    f"{color['MAGENTA']}The stats for final boss are: Damage: 200 | HP: 2000\n\n"
                    f"{color['YELLOW']}The final boss will look like this: 👾\n\n"
                    f"{color['GREEN']}Since you are fighting the boss, extra HP will be given when you visit the "
                    f"hospital.\n"
                    f"Make sure you take advantage of this before fighting the boss!\n\n"
                    f"{color['BLUE']}The final boss has absorbed all the monsters' energy, leaving them static.\n"
                    f"You can pass through monsters without fighting.\n\n"
                    f"Good luck!\n{color['RESET']}\n")

        game.boss_description(color)
        actual = mock_stdout.getvalue()

        self.assertEqual(expected, actual)
