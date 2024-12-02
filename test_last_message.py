from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import time
import game
.

class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=StringIO)
    def test_last_message(self, mock_stdout, mock_time):
        color = {"YELLOW": "\033[93m"}

        expected = (f"\n{color['YELLOW']}You have successfully completed this game!\n"
                    f"You will be remembered as a legend in this dungeon....")

        game.last_message(color)
        actual = mock_stdout.getvalue()

        self.assertEqual(expected, actual)
