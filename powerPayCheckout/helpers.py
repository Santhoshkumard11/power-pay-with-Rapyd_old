import hashlib
import base64
from datetime import datetime
import calendar
import string
from random import choice, randint, choices
import hmac
import os
import logging
import azure.functions as func

ALL_CHARACTERS = string.ascii_letters + string.punctuation + string.digits


def get_params(params_name: str, req: func.HttpRequest):
    """Retrieve the param from the request

    Args:
        params_name (str): name of the params to retrieve
        req (func.HttpRequest): request object

    Returns:
        str: value of the params passed
    """

    # try to get it if it's a GET request
    params: str = req.params.get(params_name)
    if not params:
        try:
            # try getting the body of the request
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            # get the value from the request body
            params: str = req_body.get(params_name)

    return params


def generate_invoice_number(n=8) -> str:
    """Generate a random number for invoice

    Args:
        path (str): _description_

    Returns:
        str: number in string format
    """

    return "".join(choices(string.digits, k=n))


def get_request_header(path: str, body: str, method="post") -> dict:
    """Generate the Rapyd APIs header

    Args:
        path (str): URL path of the API
        body (str): the content of the request
        method (str, optional): request method type. Defaults to "post".

    Returns:
        dict: the complete header to be used
    """

    logging.info("Started generating the request header")

    min_char, max_char = 8, 12
    try:
        salt = "".join(
            choice(ALL_CHARACTERS) for _ in range(randint(min_char, max_char))
        )

        d = datetime.utcnow()
        timestamp = calendar.timegm(d.utctimetuple())

        access_key = os.getenv("RAPYD_ACCESS_KEY")
        secret_key = os.getenv("RAPYD_SECRET_KEY")

        # adding everything together to sign with the secret
        to_sign = (
            method
            + path
            + salt
            + str(timestamp)
            + access_key
            + secret_key
            + body.replace(" ", "")
        )

        h = hmac.new(
            bytes(secret_key, "utf-8"), bytes(to_sign, "utf-8"), hashlib.sha256
        )

        signature = base64.urlsafe_b64encode(str.encode(h.hexdigest()))

    except:
        logging.info("There is an error while assembling the header")
        raise

    # this is the final header assembly
    headers = {
        "access_key": access_key,
        "signature": signature,
        "salt": salt,
        "timestamp": str(timestamp),
        "Content-Type": "application/json",
    }

    logging.info("Successfully generated the request header")

    return headers
