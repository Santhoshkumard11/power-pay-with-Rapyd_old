import logging
import json
import os
from powerPayCheckout.constants import SHAREPOINT_URLS
from powerPayCheckout.helpers import generate_invoice_number
from powerPayCheckout.microsoft_graph_api import GraphClient
from powerPayCheckout.rapyd_client import generate_checkout_id


class SharePointClient:
    def __init__(self, msft_graph_client: GraphClient) -> None:
        self.site_id = os.getenv("SITE_ID")
        self.msft_graph_client = msft_graph_client

    def get_all_lists(self):
        url = f"https://graph.microsoft.com/v1.0/sites/{self.site_id}/lists/c2402b9b-a65b-490a-9bca-b0a4ce953c7d/items"

        graph_result = self.msft_graph_client.send_msft_graph_request(url)

        logging.info(graph_result)

    def create_list_item(self, invoice_details):
        created_success = "Successfully created a new item with id - "
        url = SHAREPOINT_URLS.get("create_url").format(**{"site_id": self.site_id})

        invoice_cost = invoice_details.get("Cost").strip()

        invoice_number = generate_invoice_number().strip()

        checkout_id = generate_checkout_id(invoice_cost, invoice_number)

        assert checkout_id

        payload = {
            "fields": {
                "Title": invoice_details.get("Title"),
                "Customer": invoice_details.get("Customer"),
                "Cost": invoice_cost,
                "DueBy": invoice_details.get("DueBy"),
                "InvoiceNumber": invoice_number,
                "CheckoutID": checkout_id,
            }
        }

        graph_result = self.msft_graph_client.send_msft_graph_request(
            url, "POST", json.dumps(payload)
        )

        new_item_id = graph_result.get("id")

        if new_item_id:
            logging.info("Successfully created the item")
            created_success += new_item_id
        else:
            logging.info(f"Error while creating the list item {graph_result}")
            logging.info("Successfully processed the callback from Rapyd")
            created_success = "Failed to create a new item"

        return created_success

    def update_list_item(self, body):

        # TODO: validate the checkout id and item id before proceeding with the update
        # checkout_id = body.get("checkout_id")
        status: str = body.get("status")
        item_id = body.get("item_id")
        item_status = ""
        processed_by = body.get("processed_by")

        assert item_id and status

        if status.lower() == "success":
            item_status = "Payment Successful"
        else:
            item_status = "Payment Failed"

        created_success = f"Successfully updated the item with id - {item_id}"
        url = SHAREPOINT_URLS.get("update_url").format(
            **{"site_id": self.site_id, "item_id": item_id}
        )

        payload = {"Status": item_status, "ProcessedBy": processed_by}

        logging.info(f"Payload to update - {payload}")

        graph_result = self.msft_graph_client.send_msft_graph_request(
            url, "PATCH", json.dumps(payload)
        )

        logging.info(graph_result)

        if graph_result.get("id"):
            logging.info(f"Successfully updated the item with id {item_id}")

        else:
            logging.info(f"Error while creating the list item {graph_result}")
            logging.info("Successfully processed the callback from Rapyd")
            created_success = f"Failed to update the item with id {item_id}"

        return created_success
