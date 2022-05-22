import hashlib
import base64
from datetime import datetime
import calendar
import string
from random import choice, randint, choices
import hmac
import os
import logging

ALL_CHARACTERS = string.ascii_letters + string.punctuation + string.digits


def get_params(params_name: str, req: object):
    params = req.params.get(params_name)
    if not params:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            params = req_body.get(params_name)

    return params


def generate_invoice_number():

    return "".join(choices(string.digits, k=8))


def get_request_header(path: str, body: str, method="post"):
    logging.info("Started generating the request header")

    min_char = 8
    max_char = 12
    salt = "".join(choice(ALL_CHARACTERS) for _ in range(randint(min_char, max_char)))

    d = datetime.utcnow()
    timestamp = calendar.timegm(d.utctimetuple())

    access_key = os.getenv("RAPYD_ACCESS_KEY")
    secret_key = os.getenv("RAPYD_SECRET_KEY")

    to_sign = method + path + salt + str(timestamp) + access_key + secret_key + body

    h = hmac.new(bytes(secret_key, "utf-8"), bytes(to_sign, "utf-8"), hashlib.sha256)

    signature = base64.urlsafe_b64encode(str.encode(h.hexdigest()))

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
