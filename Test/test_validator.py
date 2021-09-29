import unittest

from Production.validator import validate_input


class TestValidator(unittest.TestCase):
    def test_validator_value_under_range(self):
        actual = validate_input(0)
        expected = "Error, value must be above 1"

        self.assertEqual(actual, expected)

    def test_validator_value_above_range(self):
        actual = validate_input(50001)
        expected = "Error, value must be less than 5000"

        self.assertEqual(actual, expected)
