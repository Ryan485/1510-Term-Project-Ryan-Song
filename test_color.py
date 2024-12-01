from unittest import TestCase

import game


class Test(TestCase):
    def test_colours(self):
        result = game.colours()
        self.assertEqual(result["RED"], "\033[91m")
        self.assertEqual(result["GREEN"], "\033[92m")
        self.assertEqual(result["YELLOW"], "\033[93m")
        self.assertEqual(result["BLUE"], "\033[94m")
        self.assertEqual(result["MAGENTA"], "\033[95m")
        self.assertEqual(result["RESET"], "\033[0m")
        self.assertEqual(result["BOLD"], "\033[1m")
