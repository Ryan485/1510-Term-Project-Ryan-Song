from unittest import TestCase
import game
from unittest.mock import patch
from io import StringIO


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=StringIO)
    def test_tutorial_monster(self, mock_stdout, mock_sleep):
        color = {"YELLOW": "\033[93m",
                 "RESET": "\033[0m"}
        expected = (f"\033[93m\nAs you wander through the dungeon, "
                    f"you'll encounter monsters looking like this '👹'\n"
                    f"\033[93mYour mission is to kill them.\n"
                    f"When you are low on HP, you can heal yourself at the hospital.\n"
                    f"Hospital looks like this: 🏥\n"
                    f"\033[93mNow, let's go and slay some monsters!\033[0m\n\n")
        game.tutorial_monster(color)
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)
