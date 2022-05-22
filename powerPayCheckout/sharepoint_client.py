import logging
import os
from powerPayCheckout.microsoft_graph_api import GraphClient


class SharePointClient:
    def __init__(self, msft_graph_client: GraphClient) -> None:
        self.site_id = os.getenv("SITE_ID")
        self.msft_graph_client = msft_graph_client

    def get_all_lists(self):
        url = f"https://graph.microsoft.com/v1.0/sites/{self.site_id}/lists"

        graph_result = self.msft_graph_client.send_msft_graph_request(url)

        logging.info(graph_result)
