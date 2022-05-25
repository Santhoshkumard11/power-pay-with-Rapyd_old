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
    logging.info("Triggered powerPayCheckout API!")

    checkout_page = "static/html/checkout.html"
    try:

        request_type = get_params("type", req)

        # Receive the callback from Rapyd service
        if request_type == "webhook":
            # as of now we don't do anything with the webhook except putting it in the logs for further reference
            logging.info(f"We got a callback from Rapyd webhook - {req.get_json()}")
            # update_list_item(req)
            return func.HttpResponse(
                json.dumps({"message": "success"}), status_code=200
            )

        # Receive the actual payment success just after the payment is complete from the toolkit integrated page
        elif request_type == "callback_from_checkout_page":
            logging.info("We got a callback from Rapyd Checkout page")
            return_message = update_list_item(req)
            return func.HttpResponse(
                json.dumps({"message": return_message}), status_code=200
            )

        # generate the checkout ID for the given amount and upload it to SharePoint
        elif request_type == "create_invoice":
            return_message = create_sharepoint_list(req)
            return func.HttpResponse(
                json.dumps({"message": return_message}), status_code=200
            )

        # render the checkout toolkit page
        elif request_type == "checkout":
            # display the checkout page
            params_dict = req.params
            logging.info(
                f"Displaying checkout page for item id - {params_dict.get('item_id')}"
            )

            # load the html page and return it to the browser
            with open(checkout_page, "rb") as f:
                mimetype = mimetypes.guess_type(checkout_page)
                return func.HttpResponse(
                    f.read(), mimetype=mimetype[0], status_code=200
                )

    except:
        logging.exception("Error occurred while processing the request")

        # return something to the user when things go wrong
        return func.HttpResponse(
            json.dumps({"message": "There is a error while processing this request."}),
            status_code=200,
        )

    # a default return message to show that endpoint is active
    return func.HttpResponse(
        json.dumps({"message": "This endpoint is working and active"}), status_code=200
    )
