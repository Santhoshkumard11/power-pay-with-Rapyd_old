import logging

from powerPayCheckout.microsoft_graph_api import GraphClient
from powerPayCheckout.sharepoint_client import SharePointClient

graph_client_obj = GraphClient()
graph_client_obj.get_graph_access_token()
sharepoint_client_obj = SharePointClient(graph_client_obj)


def update_list_item(req):
    assert req.method == "POST"
    logging.info("Started processing the callback from Rapyd")

    update_result = sharepoint_client_obj.update_list_item(req.get_json())

    logging.info("Done processing the callback from Rapyd")

    return update_result


def create_sharepoint_list(req):
    assert req.method == "POST"

    logging.info("Started processing the invoice creation request")

    creation_status = sharepoint_client_obj.create_list_item(req.get_json())

    logging.info("Completed processing the invoice creation request")

    return creation_status
