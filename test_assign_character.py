from io import StringIO
from unittest import TestCase
from unittest.mock import patch

import game


class Test(TestCase):
    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=StringIO)
    def test_assign_character_1(self, mock_stdout, mock_time):
        selected_character = "1"
        color = {"MAGENTA": "\033[95m"}
        expected = "\033[95mYour character is Ranger! Let's go kill monsters!\n\n"

        game.assign_character(selected_character, color)

        actual = mock_stdout.getvalue()

        self.assertEqual(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=StringIO)
    def test_assign_character_2(self, mock_stdout, mock_time):
        selected_character = "2"
        color = {"MAGENTA": "\033[95m"}
        expected = "\033[95mYour character is Wolverine! Let's go kill monsters!\n\n"

        game.assign_character(selected_character, color)

        actual = mock_stdout.getvalue()

        self.assertEqual(expected, actual)

    @patch('time.sleep', return_value=None)
    @patch('sys.stdout', new_callable=StringIO)
    def test_assign_character_3(self, mock_stdout, mock_time):
        selected_character = "3"
        color = {"MAGENTA": "\033[95m"}
        expected = "\033[95mYour character is Axeman! Let's go kill monsters!\n\n"

        game.assign_character(selected_character, color)

        actual = mock_stdout.getvalue()

        self.assertEqual(expected, actual).

