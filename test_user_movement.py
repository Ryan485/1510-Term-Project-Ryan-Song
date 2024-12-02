from unittest import TestCase
import game
.

class Test(TestCase):
    def test_user_movement_1(self):
        attributes = {"X-coordinate": 1, "Y-coordinate": 1}
        coordinates = {(1, 1): "💂‍♂️", (1, 0): "🌲", (0, 1): "🌲", (2, 1): "🌲"}

        game.user_movement(attributes, coordinates, True, "1")

        expected_attributes = {"X-coordinate": 1, "Y-coordinate": 0}
        expected_coordinates = {(1, 1): "🌲", (1, 0): "💂‍♂️", (0, 1): "🌲", (2, 1): "🌲"}

        self.assertEqual(attributes, expected_attributes)
        self.assertEqual(coordinates, expected_coordinates)

    def test_user_movement_2(self):
        attributes = {"X-coordinate": 1, "Y-coordinate": 1}
        coordinates = {(1, 1): "💂‍♂️", (1, 0): "🌲", (0, 1): "🌲", (1, 2): "🌲"}

        game.user_movement(attributes, coordinates, True, "2")

        expected_attributes = {"X-coordinate": 1, "Y-coordinate": 2}
        expected_coordinates = {(1, 1): "🌲", (1, 0): "🌲", (0, 1): "🌲", (1, 2): "💂‍♂️"}

        self.assertEqual(attributes, expected_attributes)
        self.assertEqual(coordinates, expected_coordinates)

    def test_user_movement_3(self):
        attributes = {"X-coordinate": 1, "Y-coordinate": 1}
        coordinates = {(1, 1): "💂‍♂️", (1, 0): "🌲", (0, 1): "🌲", (1, 2): "🌲"}

        game.user_movement(attributes, coordinates, True, "3")

        expected_attributes = {"X-coordinate": 0, "Y-coordinate": 1}
        expected_coordinates = {(1, 1): "🌲", (1, 0): "🌲", (0, 1): "💂‍♂️", (1, 2): "🌲"}

        self.assertEqual(attributes, expected_attributes)
        self.assertEqual(coordinates, expected_coordinates)

    def test_user_movement_4(self):
        attributes = {"X-coordinate": 1, "Y-coordinate": 1}
        coordinates = {(1, 1): "💂‍♂️", (1, 0): "🌲", (0, 1): "🌲", (2, 1): "🌲"}

        game.user_movement(attributes, coordinates, True, "4")

        expected_attributes = {"X-coordinate": 2, "Y-coordinate": 1}
        expected_coordinates = {(1, 1): "🌲", (1, 0): "🌲", (0, 1): "🌲", (2, 1): "💂‍♂️"}

        self.assertEqual(attributes, expected_attributes)
        self.assertEqual(coordinates, expected_coordinates)