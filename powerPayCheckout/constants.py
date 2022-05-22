import os

# TODO: try to authenticate the invoice coming through

COMPANY_AUTH_KEY_MAPPING = ["Microsoft", os.getenv("MICROSOFT_ACCESS_KEY")]

SHAREPOINT_URLS = {
    "update_url": "https://graph.microsoft.com/v1.0/sites/{site_id}/lists/c2402b9b-a65b-490a-9bca-b0a4ce953c7d/items/{item_id}/fields",
    "create_url": "https://graph.microsoft.com/v1.0/sites/{site_id}/lists/c2402b9b-a65b-490a-9bca-b0a4ce953c7d/items",
}
