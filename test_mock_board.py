from unittest import TestCase
import game
from unittest.mock import patch
from io import StringIO


class Test(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_mock_board_2X2(self, mock_stdout):
        coordinates = {(0, 0): '🌲', (0, 1): '🌲', (1, 0): '🌲', (1, 1): '🌲'}
        expected_output = (
            "💂‍♂️  🌲  \n"
            "🌲  🌲  \n"
        )

        game.mock_board(coordinates, 2, 2)
        actual_output = mock_stdout.getvalue()

        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_mock_board_5X5(self, mock_stdout):
        coordinates = {(row, col): '🌲' for row in range(5) for col in range(5)}
        expected_output = (
            "💂‍♂️  🌲  🌲  🌲  🌲  \n"
            "🌲  🌲  🌲  🌲  🌲  \n"
            "🌲  🌲  🌲  🌲  🌲  \n"
            "🌲  🌲  🌲  🌲  🌲  \n"
            "🌲  🌲  🌲  🌲  🌲  \n"
        )

        game.mock_board(coordinates, 5, 5)
        actual_output = mock_stdout.getvalue()

        self.assertEqual(expected_output, actual_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_mock_board_10X10(self, mock_stdout):
        coordinates = {(row, col): '🌲' for row in range(10) for col in range(10)}
        expected_output = (
            "💂‍♂️  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  \n"
            "🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  \n"
            "🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  \n"
            "🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  \n"
            "🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  \n"
            "🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  \n"
            "🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  \n"
            "🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  \n"
            "🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  \n"
            "🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  🌲  \n"
        )

        game.mock_board(coordinates, 10, 10)
        actual_output = mock_stdout.getvalue()

        self.assertEqual(expected_output, actual_output)
