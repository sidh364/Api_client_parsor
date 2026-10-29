
import unittest
from unittest.mock import Mock, patch

from api_client import APIClient
from data_parser import UserParser


SAMPLE_USER = {
    "id": 1,
    "name": "Asha",
    "username": "asha",
    "email": "ASHA@EXAMPLE.COM"
}


class TestUserParser(unittest.TestCase):

    def setUp(self):
        self.parser = UserParser()

    def test_parse_valid_user(self):
        result = self.parser.parse(SAMPLE_USER)

        self.assertEqual(result["name"], "Asha")
        self.assertEqual(result["email"], "asha@example.com")

    def test_parse_strips_spaces(self):
        data = {
            "id": 2,
            "name": "  Rahul  ",
            "username": " rahul ",
            "email": " RAHUL@EXAMPLE.COM "
        }

        result = self.parser.parse(data)

        self.assertEqual(result["name"], "Rahul")
        self.assertEqual(result["username"], "rahul")
        self.assertEqual(result["email"], "rahul@example.com")

    def test_missing_field(self):
        data = {
            "id": 1,
            "name": "Asha",
            "username": "asha"
        }

        with self.assertRaisesRegex(ValueError, "Missing required field"):
            self.parser.parse(data)

    def test_empty_name(self):
        data = {
            "id": 1,
            "name": " ",
            "username": "asha",
            "email": "asha@example.com"
        }

        with self.assertRaisesRegex(ValueError, "Name must"):
            self.parser.parse(data)



class TestAPIClient(unittest.TestCase):

    def setUp(self):
        self.client = APIClient("https://example.com")
        self.client.session = Mock()

    def test_fetch_user_success(self):
        mock_response = Mock()
        mock_response.json.return_value = SAMPLE_USER
        self.client.session.get.return_value = mock_response

        result = self.client.fetch_user(1)

        self.assertEqual(result, SAMPLE_USER)
        self.client.session.get.assert_called_once_with(
            "https://example.com/users/1",
            timeout=10
        )
        mock_response.raise_for_status.assert_called_once()

    def test_fetch_user_http_error(self):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = Exception(
            "HTTP error"
        )
        self.client.session.get.return_value = mock_response

        with self.assertRaisesRegex(Exception, "HTTP error"):
            self.client.fetch_user(1)
