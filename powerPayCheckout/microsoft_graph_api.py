import msal
import logging
import requests
import os


class GraphClient:
    def __init__(self) -> None:
        self.client_id = os.getenv("MSFT_CLIENT_ID")
        self.client_secret = os.getenv("MSFT_CLIENT_SECRET")
        self.tenant_id = os.getenv("TENANT_ID")
        self.authority = f"https://login.microsoftonline.com/{self.tenant_id}"
        self.access_token = ""

    def get_graph_access_token(self):
        logging.info("Trying to fetch the MSFT Graph API access token")

        # connecting to the client app
        app = msal.ConfidentialClientApplication(
            client_id=self.client_id,
            client_credential=self.client_secret,
            authority=self.authority,
        )

        scopes = ["https://graph.microsoft.com/.default"]

        result = None

        # checking the cache for tokens
        result = app.acquire_token_silent(scopes, account=None)

        if not result:
            logging.info(
                "No suitable token exists in cache. Let's get a new one from Azure Active Directory."
            )
            # getting a new token if it's not available in cache
            result = app.acquire_token_for_client(scopes=scopes)

        if "access_token" in result:
            self.access_token = result["access_token"]
            logging.info("Successfully retrieved the token")
        else:
            logging.info(f"Token can't be fetched, {result['error']}")

    def send_msft_graph_request(self, url: str, method="GET", payload=None):

        # if we don't have an access token then get a new one
        if not self.access_token:
            self.get_graph_access_token()

        if method == "GET":
            logging.info(f"Sending in Graph API GET request to - {url}")
            try:
                graph_result_data = requests.get(
                    url,
                    headers={"Authorization": "Bearer " + self.access_token},
                ).json()
            except:
                logging.error(f"Error while trying to fetch details for URL - {url}")
                raise

            logging.info(f"Successfully retrieved details on URL - {url}")
            return graph_result_data

        elif method == "PATCH":
            assert payload

            logging.info(f"Sending a patch request to - {url}")

            try:

                graph_result_data = requests.patch(
                    url,
                    headers={
                        "Authorization": "Bearer " + self.access_token,
                        "Content-Type": "application/json",
                    },
                    data=payload,
                ).json()

            except:
                logging.error(f"Error while trying to patch details for URL - {url}")
                raise

            logging.info(f"Successfully patched details on URL - {url}")
            return graph_result_data

        elif method == "POST":
            assert payload

            logging.info(f"Sending a post request to - {url}")

            try:

                graph_result_data = requests.post(
                    url,
                    headers={
                        "Authorization": "Bearer " + self.access_token,
                        "Content-Type": "application/json",
                    },
                    data=payload,
                ).json()

            except:
                logging.error(f"Error while trying to post details for URL - {url}")
                raise

            logging.info(f"Successfully posted details on URL - {url}")
            return graph_result_data
