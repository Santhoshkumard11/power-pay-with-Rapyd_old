import logging
import json
from unittest import result
import requests
import os

from powerPayCheckout.helpers import get_request_header


def make_request(method: str, headers: dict, url_path: str, payload: dict):
    logging.info("Sending in POST request to Rapyd")

    if method == "POST":
        post_request_result = requests.post(url_path, data=payload, headers=headers)

    return json.loads(post_request_result.text)


def generate_checkout_id(price: str, invoice_number: str):
    logging.info(f"Starting to generate checkout ID for price - {price}")
    try:

        body = json.dumps(
            {
                "amount": price,
                "complete_checkout_url": "https://sandy-power-pay-rapyd.azurewebsites.net/api/powerPayCheckout",
                "country": "US",
                "currency": "USD",
                "requested_currency": "USD",
                "merchant_reference_id": "950ae8c6-76",
                "language": "en",
                "payment_method_types_include": [
                    "us_mastercard_card",
                ],
                "metadata": {"InvoiceNumber": invoice_number},
            }
        )

        results = make_request(
            method="POST",
            url_path=os.getenv("RAPYD_URL"),
            payload=body,
            headers=get_request_header("/v1/checkout", body),
        )
        if results.get("status").get("status") == "SUCCESS":
            logging.info(results)
            return results.get("data").get("id")

        return False

    except:
        logging.info("There is an error while requesting checkout ID from Rapyd")
        raise

    logging.info(f"Successfully generated checkout ID for price - {price}")
