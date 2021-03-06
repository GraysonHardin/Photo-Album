import unittest
from Production.validator import validate_input


class TestValidator(unittest.TestCase):
    def test_validator_value_is_below_min_range(self):
        actual = validate_input(0)
        expected = False

        self.assertEqual(actual, expected)

    def test_validator_value_is_above_max_range(self):
        actual = validate_input(5001)
        expected = False

        self.assertEqual(actual, expected)

    def test_validator_within_min_range(self):
        actual = validate_input(1)
        expected = True

        self.assertEqual(actual, expected)

    def test_validator_within_max_range(self):
        actual = validate_input(5000)
        expected = True

        self.assertEqual(actual, expected)

    def test_validator_try_catch(self):
        actual = validate_input('invalid input')
        expected = 'Invalid input! Value must be an integer between 1 and 5000.'

        self.assertEqual(actual, expected)
