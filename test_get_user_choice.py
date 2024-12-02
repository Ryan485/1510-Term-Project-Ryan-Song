from unittest import TestCase
from unittest.mock import patch
import game

/
class Test(TestCase):
    @patch('builtins.input', return_value='1')
    def test_get_user_choice_1(self, mock_input):
        color = {'GREEN': '\033[92m', 'RED': '\033[91m'}
        expected = '1'
        actual = game.get_user_choice(color)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='2')
    def test_get_user_choice_2(self, mock_input):
        color = {'GREEN': '\033[92m', 'RED': '\033[91m'}
        expected = '2'
        actual = game.get_user_choice(color)
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='3')
    def test_get_user_choice_3(self, mock_input):
        color = {'GREEN': '\033[92m', 'RED': '\033[91m'}
        expected = '3'
        actual = game.get_user_choice(color)
        self.assertEqual(expected, actual)
