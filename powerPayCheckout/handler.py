import logging
import azure.functions as func
from powerPayCheckout.microsoft_graph_api import GraphClient
from powerPayCheckout.sharepoint_client import SharePointClient

graph_client_obj = GraphClient()
graph_client_obj.get_graph_access_token()
sharepoint_client_obj = SharePointClient(graph_client_obj)


def update_list_item(req: func.HttpRequest) -> str:
    """Update the SharePoint Invoice List

    Args:
        req (HttpRequest): request object

    Returns:
        str: status of the update
    """

    assert req.method == "POST"

    logging.info("Started processing the callback from Rapyd")

    update_result: str = sharepoint_client_obj.update_list_item(req.get_json())

    logging.info("Done processing the callback from Rapyd")

    return update_result


def create_sharepoint_list(req: func.HttpRequest) -> str:
    """Create a new entry into the SharePoint Invoice List

    Args:
        req (HttpRequest): request object

    Returns:
        str: status of the creation
    """

    assert req.method == "POST"

    logging.info("Started processing the invoice creation request")

    creation_status: str = sharepoint_client_obj.create_list_item(req.get_json())

    logging.info("Completed processing the invoice creation request")

    return creation_status
