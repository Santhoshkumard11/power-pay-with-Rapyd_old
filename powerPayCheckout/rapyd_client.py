import logging
import json
import requests
import os

from powerPayCheckout.helpers import get_request_header


def make_request(method: str, headers: dict, url_path: str, payload: dict) -> dict:
    """Send request to Rapyd client

    Args:
        method (str): method type
        headers (dict): request header
        url_path (str): request URL
        payload (dict): request body

    Returns:
        dict: request response
    """

    logging.info("Sending in POST request to Rapyd")

    if method == "POST":
        post_request_result = requests.post(url_path, data=payload, headers=headers)

    return json.loads(post_request_result.text)


def generate_checkout_id(price: str, invoice_number: str) -> str:
    """Generate checkout ID for the given price

    Args:
        price (str): price for which the checkout ID has to be created
        invoice_number (str): invoice number used to track the checkout ID and payment status

    Returns:
        str: checkout ID
    """

    logging.info(f"Starting to generate checkout ID for price - {price}")
    try:
        checkout_id = ""

        body = json.dumps(
            {
                "amount": price,
                "complete_checkout_url": "https://sandy-power-pay-rapyd.azurewebsites.net/api/powerPayCheckout",
                "country": "US",
                "currency": "USD",
                "requested_currency": "USD",
                "merchant_reference_id": "950ae8c6-76",
                "language": "en",
                "payment_method_type_categories": ["card"],
                "metadata": {"InvoiceNumber": invoice_number},
            }
        )

        # send a request to the Rapyd APi to generate the checkout ID
        results = make_request(
            method="POST",
            url_path=os.getenv("RAPYD_URL"),
            payload=body,
            headers=get_request_header("/v1/checkout", body),
        )

        logging.info(results)
        if results.get("status").get("status") == "SUCCESS":
            checkout_id = results.get("data").get("id")
        else:
            logging.info("Error in creating the checkout id")

    except:
        logging.info("There is an error while requesting checkout ID from Rapyd")
        raise

    logging.info(f"Successfully generated checkout ID - {checkout_id} for price - {price}")

    return checkout_id
