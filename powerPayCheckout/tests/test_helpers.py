import unittest
from unittest.mock import MagicMock

from powerPayCheckout.helpers import generate_invoice_number, get_params


class HelperTest(unittest.TestCase):
    def setUp(self) -> None:
        self.general_mock = MagicMock()

        self.mock_request = self.general_mock.mock_request()

    def test_get_params_with_the_params(self):
        test_params, expected_result = "type", "checkout"

        self.mock_request.params.get.return_value = "checkout"

        test_result = get_params(test_params, self.mock_request)

        self.assertIsInstance(test_result, str)

        self.assertEqual(test_result, expected_result)

    def test_get_params_without_the_params(self):
        test_params = "id"

        self.mock_request.params.get.return_value = None

        self.mock_request.get_json.side_effect = Exception("id")

        with self.assertRaises(Exception):

            get_params(test_params, self.mock_request)

    def test_generate_invoice_number(self):

        test_result = generate_invoice_number()

        self.assertIsInstance(test_result, str)

        self.assertEqual(test_result.__len__(), 8)
