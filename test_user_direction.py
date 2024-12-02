from unittest import TestCase
import game
from unittest.mock import patch
from io import StringIO


class Test(TestCase):
    @patch('builtins.input', return_value='1')
    def test_user_direction_1(self, mock_input):
        color = {"BOLD": "\033[1m"}
        expected = '1'
        actual = game.user_direction(color)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='2')
    def test_user_direction_2(self, mock_input):
        color = {"BOLD": "\033[1m"}
        expected = '2'
        actual = game.user_direction(color)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='3')
    def test_user_direction_3(self, mock_input):
        color = {"BOLD": "\033[1m"}
        expected = '3'
        actual = game.user_direction(color)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='4')
    def test_user_direction_4(self, mock_input):
        color = {"BOLD": "\033[1m"}
        expected = '4'
        actual = game.user_direction(color)
        self.assertEqual(expected, actual)

