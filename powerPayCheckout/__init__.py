import json
import logging
import mimetypes
import azure.functions as func

# from powerPayCheckout.rapyd_client import generate_checkout_id
from powerPayCheckout.helpers import get_params
from powerPayCheckout.handler import (
    create_sharepoint_list,
    update_list_item,
)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    checkout_page = "static/html/checkout.html"
    try:

        request_type = get_params("type", req)

        # if request_type == "generate":
        #     logging.info("Received a generate request")
        #     price = get_params("price", req)
        #     if not price:
        #         return func.HttpResponse(
        #             "Please pass in the price to generate a checkout ID"
        #         )

        #     result_checkout_id = generate_checkout_id(price)

        #     json_response_payload = {"checkout_id": result_checkout_id}

        #     return func.HttpResponse(json.dumps(json_response_payload), status_code=200)

        if request_type == "webhook":
            logging.info(f"We got a callback from Rapyd webhook - {req.get_json()}")
            # update_list_item(req)
            return func.HttpResponse(json.dumps({"status": 900}), status_code=200)

        elif request_type == "callback_from_checkout_page":
            logging.info("We got a callback from Rapyd Checkout page")
            return_message = update_list_item(req)
            return func.HttpResponse(
                json.dumps({"message": return_message}), status_code=200
            )

        elif request_type == "create_invoice":
            return_message = create_sharepoint_list(req)
            return func.HttpResponse(
                json.dumps({"message": return_message}), status_code=200
            )

        elif request_type == "checkout":
            # display the checkout page
            params_dict = req.params
            logging.info(
                f"Displaying checkout page for item id - {params_dict.get('item_id')}"
            )

            with open(checkout_page, "rb") as f:
                mimetype = mimetypes.guess_type(checkout_page)
                return func.HttpResponse(
                    f.read(), mimetype=mimetype[0], status_code=200
                )

    except:
        logging.exception("Error occurred while processing the request")

        # return something to the user when things go wrong
        return func.HttpResponse(
            json.dumps({"message": "There is a error while processing this request."})
        )

    return func.HttpResponse(
        json.dumps({"message": "This endpoint is working and active"}), status_code=200
    )
