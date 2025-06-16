import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError
from typing import List

from ibm_watsonx_orchestrate.agent_builder.tools import tool
from ibm_watsonx_orchestrate.run import connections
from ibm_watsonx_orchestrate.client.connections import ConnectionType


CONN_BASIC_AUTH = 'ITAH'


@tool(
    expected_credentials=[
        {"app_id": CONN_BASIC_AUTH, "type": ConnectionType.BASIC_AUTH}
    ],
)
def get_orders_by_user(
    user_email: str
) -> List[str]:
    """
    Invoke the ITAH_GetOrdersByUser endpoint to retrieve order reference IDs for a given user.

    Args:
        user_email: The email address of the user.

    Returns:
        A list of order reference IDs.

    Raises:
        ITAHException: If the service returns a 4xx/5xx with a JSON error body.
        requests.HTTPError: For non-JSON errors or unexpected HTTP failures.
    """
    url = f"{connections.basic_auth(CONN_BASIC_AUTH).url}/ITAH_GetOrdersByUser"
    username = connections.basic_auth(CONN_BASIC_AUTH).username
    password = connections.basic_auth(CONN_BASIC_AUTH).password
    auth = HTTPBasicAuth(username, password)

    print(user_email)
    print(username)
    print(password)
    print(url)

    payload = {"userEmail": user_email}

    
    try:
        response = requests.post(url, auth=auth, json=payload, verify=False)
        response.raise_for_status()
    except HTTPError as err:
        error_resp = err.response or response
        log_lines = [
            "HTTPError in ITAH_GetOrdersByUser",
            f"URL          : {error_resp.url}",
            f"Status code  : {error_resp.status_code}",
            f"Content-Type : {error_resp.headers.get('Content-Type', '—')}",
            "Error text    :",
            (error_resp.text or "")[:2_000],
        ]
        print("\n".join(log_lines))
        raise

    data = response.json()
    return data.get("referenceIDs", [])

