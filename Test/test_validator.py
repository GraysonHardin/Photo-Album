import unittest

from Production.validator import validate_input


class TestValidator(unittest.TestCase):
    def test_validator_value_under_range(self):
        actual = validate_input(-1)
        expected = "Error, value must be above 1"

        self.assertEqual(actual, expected)
