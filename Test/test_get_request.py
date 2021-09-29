import unittest
from unittest.mock import patch, Mock
import requests
from Production.get_request import get_album_id_request


class TestGetRequest(unittest.TestCase):
    @patch.object(requests, 'get')
    def test_get_request_method(self, mockget):
        expected = {'key': 'value'}
        mock_response = Mock()

        mockget.return_value = mock_response
        mock_response.json = lambda: expected

        actual = get_album_id_request(1)
        self.assertEqual(actual, expected)
