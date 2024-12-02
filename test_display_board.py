from unittest import TestCase
import game
from unittest.mock import patch
from io import StringIO

.
class Test(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_board_2X2(self, mock_stdout):
        coordinates = {(0, 0): '🌲', (0, 1): '💂‍', (1, 0): '🌲', (1, 1): '🌲'}
        expected = ("🌲  💂‍  \n"
                    "🌲  🌲  \n")
        game.display_board(coordinates, 2, 2)
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_board_3X3(self, mock_stdout):
        coordinates = {
            (0, 0): '🌲', (0, 1): '🌲', (0, 2): '🌲',
            (1, 0): '🌲', (1, 1): '💂‍', (1, 2): '🌲',
            (2, 0): '🌲', (2, 1): '🌲', (2, 2): '🌲'
        }
        expected = (
            "🌲  🌲  🌲  \n"
            "🌲  💂‍  🌲  \n"
            "🌲  🌲  🌲  \n"
        )
        game.display_board(coordinates, 3, 3)
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_board_5X5(self, mock_stdout):
        coordinates = {
            (0, 0): '🌲', (0, 1): '🌲', (0, 2): '🌲', (0, 3): '🌲', (0, 4): '🌲',
            (1, 0): '🌲', (1, 1): '🌲', (1, 2): '🌲', (1, 3): '🌲', (1, 4): '🌲',
            (2, 0): '🌲', (2, 1): '🌲', (2, 2): '💂‍', (2, 3): '🌲', (2, 4): '🌲',
            (3, 0): '🌲', (3, 1): '🌲', (3, 2): '🌲', (3, 3): '🌲', (3, 4): '🌲',
            (4, 0): '🌲', (4, 1): '🌲', (4, 2): '🌲', (4, 3): '🌲', (4, 4): '🌲'
        }
        expected = (
            "🌲  🌲  🌲  🌲  🌲  \n"
            "🌲  🌲  🌲  🌲  🌲  \n"
            "🌲  🌲  💂‍  🌲  🌲  \n"
            "🌲  🌲  🌲  🌲  🌲  \n"
            "🌲  🌲  🌲  🌲  🌲  \n"
        )
        game.display_board(coordinates, 5, 5)
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)
