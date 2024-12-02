from unittest import TestCase
import game
from io import StringIO
from unittest.mock import patch

.
class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=StringIO)
    def test_tutorial_description(self, mock_stdout, mock_sleep):
        mock_color = {"YELLOW": "\033[93m"}
        expected = (f"\033[93mNow you are in dungeon. '💂' indicates your current location.\n"
                    f"For our next step, we are going to learn how to move.\nPlease move your character TEN times.\n"
                    f"Choose a direction below to move your character.\n\n")

        game.tutorial_description(mock_color)
        actual = mock_stdout.getvalue()

        self.assertEqual(expected, actual)
