import json
import logging
import mimetypes
import azure.functions as func
from powerPayCheckout.rapyd_client import generate_checkout_id
from powerPayCheckout.helpers import get_params
from powerPayCheckout.webhook import update_sharepoint_list


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    checkout_page = "static/html/checkout.html"
    try:

        request_type = get_params("type", req)

        if request_type == "generate":
            logging.info("Received a generate request")
            price = get_params("price", req)
            if not price:
                return func.HttpResponse(
                    "Please pass in the price to generate a checkout ID"
                )

            result_checkout_id = generate_checkout_id(price)

            json_response_payload = {"checkout_id": result_checkout_id}

            return func.HttpResponse(json.dumps(json_response_payload), status_code=200)

        elif request_type == "webhook":
            logging.info("We got a callback from Rapyd")
            update_sharepoint_list(req)
            return func.HttpResponse(json.dumps({"status": 900}), status_code=200)

        elif request_type == "new_invoice":
            pass

        else:
            with open(checkout_page, "rb") as f:
                mimetype = mimetypes.guess_type(checkout_page)
                return func.HttpResponse(
                    f.read(), mimetype=mimetype[0], status_code=200
                )

    except:
        logging.exception("Error occurred while processing the request")
