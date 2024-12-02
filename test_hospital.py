from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import game


class Test(TestCase):
    @patch('builtins.input', return_value="n")
    @patch('sys.stdout', new_callable=StringIO)
    def test_hospital_answer_no(self, mock_stdout, mock_input):
        attributes = {"X-coordinate": 3, "Y-coordinate": 5, "Level": 1, "HP": 40}
        color = {"BLUE": "\033[94m"}
        game.hospital(attributes, "1", color)
        expected = f"You are passing the hospital! Come back when you are injured 🙂\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="y")
    @patch('sys.stdout', new_callable=StringIO)
    def test_hospital_ranger_level_1(self, mock_stdout, mock_input):
        attributes = {"X-coordinate": 3, "Y-coordinate": 5, "Level": 1, "HP": 20}
        color = {"BLUE": "\033[94m"}
        game.hospital(attributes, "1", color)
        expected = f"Your HP is fully healed! Your HP is back to 100!\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="y")
    @patch('sys.stdout', new_callable=StringIO)
    def test_hospital_ranger_level_2(self, mock_stdout, mock_input):
        attributes = {"X-coordinate": 3, "Y-coordinate": 5, "Level": 2, "HP": 20}
        color = {"BLUE": "\033[94m"}
        game.hospital(attributes, "1", color)
        expected = f"Your HP is fully healed! Your HP is back to 150!\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="y")
    @patch('sys.stdout', new_callable=StringIO)
    def test_hospital_ranger_level_3(self, mock_stdout, mock_input):
        attributes = {"X-coordinate": 3, "Y-coordinate": 5, "Level": 3, "HP": 20}
        color = {"BLUE": "\033[94m"}
        game.hospital(attributes, "1", color)
        expected = f"Your HP is fully healed! Your HP is back to 200!\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="y")
    @patch('sys.stdout', new_callable=StringIO)
    def test_hospital_wolverine_level_1(self, mock_stdout, mock_input):
        attributes = {"X-coordinate": 3, "Y-coordinate": 5, "Level": 1, "HP": 20}
        color = {"BLUE": "\033[94m"}
        game.hospital(attributes, "2", color)
        expected = f"Your HP is fully healed! Your HP is back to 150!\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="y")
    @patch('sys.stdout', new_callable=StringIO)
    def test_hospital_wolverine_level_2(self, mock_stdout, mock_input):
        attributes = {"X-coordinate": 3, "Y-coordinate": 5, "Level": 2, "HP": 20}
        color = {"BLUE": "\033[94m"}
        game.hospital(attributes, "2", color)
        expected = f"Your HP is fully healed! Your HP is back to 200!\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="y")
    @patch('sys.stdout', new_callable=StringIO)
    def test_hospital_wolverine_level_3(self, mock_stdout, mock_input):
        attributes = {"X-coordinate": 3, "Y-coordinate": 5, "Level": 3, "HP": 20}
        color = {"BLUE": "\033[94m"}
        game.hospital(attributes, "2", color)
        expected = f"Your HP is fully healed! Your HP is back to 400!\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="y")
    @patch('sys.stdout', new_callable=StringIO)
    def test_hospital_axeman_level_1(self, mock_stdout, mock_input):
        attributes = {"X-coordinate": 3, "Y-coordinate": 5, "Level": 1, "HP": 20}
        color = {"BLUE": "\033[94m"}
        game.hospital(attributes, "3", color)
        expected = f"Your HP is fully healed! Your HP is back to 200!\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="y")
    @patch('sys.stdout', new_callable=StringIO)
    def test_hospital_axeman_level_2(self, mock_stdout, mock_input):
        attributes = {"X-coordinate": 3, "Y-coordinate": 5, "Level": 2, "HP": 20}
        color = {"BLUE": "\033[94m"}
        game.hospital(attributes, "3", color)
        expected = f"Your HP is fully healed! Your HP is back to 300!\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="y")
    @patch('sys.stdout', new_callable=StringIO)
    def test_hospital_axeman_level_3(self, mock_stdout, mock_input):
        attributes = {"X-coordinate": 3, "Y-coordinate": 5, "Level": 3, "HP": 20}
        color = {"BLUE": "\033[94m"}
        game.hospital(attributes, "3", color)
        expected = f"Your HP is fully healed! Your HP is back to 500!\n"
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)