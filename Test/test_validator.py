import unittest

from Production.validator import validate_input


class TestValidator(unittest.TestCase):
    def test_validator_value_is_below_min_range(self):
        actual = validate_input(0)
        expected = "Error, value must be between 1 and 5000"

        self.assertEqual(actual, expected)

    def test_validator_value_is_above_max_range(self):
        actual = validate_input(50001)
        expected = "Error, value must be between 1 and 5000"

        self.assertEqual(actual, expected)

    def test_validator_within_min_range(self):
        actual = validate_input(1)
        expected = None

        self.assertEqual(actual, expected)