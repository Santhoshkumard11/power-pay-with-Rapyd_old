import logging
import json
from powerPayCheckout.microsoft_graph_api import GraphClient


class SharePointClient:
    def __init__(self, msft_graph_client: GraphClient) -> None:
        # self.site_id = os.getenv("SITE_ID")
        self.site_id = "z3dr3.sharepoint.com,0d7d104c-d415-49ec-b2a4-ace5a6ac04ba,87a496e5-1b7d-4eea-ad53-fc761125916a"
        self.msft_graph_client = msft_graph_client

    def get_all_lists(self):
        url = f"https://graph.microsoft.com/v1.0/sites/{self.site_id}/lists/c2402b9b-a65b-490a-9bca-b0a4ce953c7d/items"

        graph_result = self.msft_graph_client.send_msft_graph_request(url)

        logging.info(graph_result)

    def create_list_item(self, invoice_details):
        created_success = "Successfully created a new item with id - "
        url = f"https://graph.microsoft.com/v1.0/sites/{self.site_id}/lists/c2402b9b-a65b-490a-9bca-b0a4ce953c7d/items"

        payload = {
            "fields": {
                "Title": invoice_details.get("Title"),
                "Customer": invoice_details.get("Customer"),
                "Cost": invoice_details.get("Cost"),
                "DueBy": invoice_details.get("DueBy"),
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
