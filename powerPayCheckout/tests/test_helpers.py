import unittest
from unittest.mock import MagicMock

from powerPayCheckout.helpers import (
    generate_invoice_number,
    get_params,
    get_request_header,
)


class HelperTest(unittest.TestCase):
    def setUp(self) -> None:
        self.general_mock = MagicMock()

        self.mock_request = self.general_mock.mock_request()

    def test_get_params_with_the_params(self):
        """Test if we have the value checkout for type params"""

        test_params, expected_result = "type", "checkout"

        self.mock_request.params.get.return_value = "checkout"

        test_result = get_params(test_params, self.mock_request)

        self.assertIsInstance(test_result, str)

        self.assertEqual(test_result, expected_result)

    def test_get_params_without_the_params(self):
        """Test if we have id params in the request body"""

        test_params = "id"

        self.mock_request.params.get.return_value = None

        self.mock_request.get_json.side_effect = Exception("id")

        with self.assertRaises(Exception):

            get_params(test_params, self.mock_request)

    def test_generate_invoice_number(self):
        """Test if we have the requested number of characters in the invoice number"""

        test_result = generate_invoice_number()

        self.assertIsInstance(test_result, str)

        self.assertEqual(test_result.__len__(), 8)

    def test_get_request_header_if_header_is_generated(self):
        """Test if we have generate the perfect header"""

        test_path, test_body = "/api/checkout", "{'amount':'230.49'}"
        test_result = get_request_header(test_path, test_body)
        header_keys = ["access_key", "signature", "salt", "timestamp", "Content-Type"]

        test_result_keys = test_result.keys()

        self.assertIsInstance(test_result, dict)

        self.assertEqual(test_result.keys().__len__(), 5)

        self.assertTrue(
            all([True if keys in test_result_keys else False for keys in header_keys])
        )
