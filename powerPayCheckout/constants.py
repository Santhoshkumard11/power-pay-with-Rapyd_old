import os

COMPANY_AUTH_KEY_MAPPING = ["Microsoft", os.getenv("MICROSOFT_ACCESS_KEY")]

# TODO: try to capture all the urls here

SHAREPOINT_URLS = {"update_url": "https://graph.microsoft.com/v1.0/sites/{site_id}/lists/c2402b9b-a65b-490a-9bca-b0a4ce953c7d/items/{item_id}/fields",
                   "create_rul": "https://graph.microsoft.com/v1.0/sites/{site_id}/lists/c2402b9b-a65b-490a-9bca-b0a4ce953c7d/items"}