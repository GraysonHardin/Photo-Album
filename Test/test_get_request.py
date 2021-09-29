import unittest
from Production.get_request import get_album_id_request


class TestGetRequest(unittest.TestCase):
    def test_get_request_method(self):
        actual = get_album_id_request()
        expected = None
        self.assertEqual(actual, expected)


