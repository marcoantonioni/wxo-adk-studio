from typing import List
import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError


from ibm_watsonx_orchestrate.agent_builder.tools import tool
from ibm_watsonx_orchestrate.run import connections
from ibm_watsonx_orchestrate.client.connections import ConnectionType


CONN_NAME = 'ITAH2'


@tool(
    expected_credentials=[
        {"app_id": CONN_NAME, "type": ConnectionType.BASIC_AUTH}
        #{"app_id": CONN_NAME, "type": ConnectionType.BEARER_TOKEN}
    ],
)
def get_order_status(
    reference_id: str
) -> List[str]:
    """
    Invoke the ITAH_GetOrderStatus endpoint to retrieve the status of a given order.
    Args:
        reference_id (str): The reference ID of the order
    Returns:
        dict: An order status object, which includes the following keys:
            - 'statusCode' (int): The status code of the order.  
            - 'orderStatus' (str): Status of the order.
            - 'reason' (str, optional): A reason for the current status, if available.
    Raises:
        ITAHException: If the service returns a 4xx or 5xx HTTP error with a JSON error body.
        requests.HTTPError: For non-JSON errors or other unexpected HTTP failures.
    """
    url = f"{connections.basic_auth(CONN_NAME).url}/ITAH_GetOrderStatus"
    username = connections.basic_auth(CONN_NAME).username
    password = connections.basic_auth(CONN_NAME).password
    auth = HTTPBasicAuth(username, password)

    #token = connections.bearer_token(CONN_NAME).token
    #url = connections.bearer_token(CONN_NAME).url
    

    print(reference_id)
    print(username)
    print(password)
    print(url)
    #print(token)

    print("")

    payload = {"referenceID": reference_id}

    try:
        response = requests.post(url, auth=auth, json=payload, verify=False)
        response.raise_for_status()
    except HTTPError as err:
        error_resp = err.response or response
        log_lines = [
            "HTTPError in ITAH_GetOrderStatus",
            f"URL          : {error_resp.url}",
            f"Status code  : {error_resp.status_code}",
            f"Content-Type : {error_resp.headers.get('Content-Type', '—')}",
            "Error text    :",
            (error_resp.text or "")[:2_000],
        ]
        print("\n".join(log_lines))
        raise

    data = response.json()
    return data.get("statusCode")

# TEST
if __name__ == '__main__':     
     print(get_order_status("123"))

"""
export WXO_SECURITY_SCHEMA_ITAH2=basic_auth
export WXO_CONNECTION_ITAH2_username=myUser
export WXO_CONNECTION_ITAH2_password=myPassword
export WXO_CONNECTION_ITAH2_url=http://api.test

export WXO_SECURITY_SCHEMA_ITAH2=bearer
export WXO_CONNECTION_ITAH2_token=tok123
"""
