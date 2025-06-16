
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission
from ibm_watsonx_orchestrate.run import connections
from ibm_watsonx_orchestrate.client.connections import ConnectionType #, ExpectedCredentials

import json

CONN_BASIC_AUTH = 'CONN_TC'

#type = ConnectionType.BASIC_AUTH
#type = ConnectionType.API_KEY_AUTH
#type = ConnectionType.BEARER_TOKEN
#type = ConnectionType.KEY_VALUE
#type = ConnectionType.OAUTH_ON_BEHALF_OF_FLOW

class ConnectionInfos:
    def __init__(self, u: str, p: str, ur):
        self.un : str = u
        self.pa : str = p
        self.ur : str = ur


@tool( 
    name="MA42021_tool_connection", 
    description="This tool answer with connection informations.",
    #permission=ToolPermission.READ_ONLY,
    expected_credentials=[
        {"app_id": CONN_BASIC_AUTH, "type": ConnectionType.BASIC_AUTH}
    ],
)
def getConnInfos() -> str:
    """
    Show connection informations

    Returns a JSON object with connection informations.
    """

    connectionInfos= "n/a"
    ci: ConnectionInfos;
    try:
        #url="http://test"
        #username="n/a"
        #password="n/a"
        url = f"{connections.basic_auth(CONN_BASIC_AUTH).url}"
        username = connections.basic_auth(CONN_BASIC_AUTH).username
        password = connections.basic_auth(CONN_BASIC_AUTH).password
        connectionInfos = f"Connection configuration: {username}/{password}/{url}"  
        ci = ConnectionInfos(username, password, url)
    except:
        print("===>> EXCEPTION during execution of TOOL")
        connectionInfos = "execution of Connection informations insufficient."
        ci = ConnectionInfos(u="n/a", p="n/a", ur="n/a")
    
    print("===>> MA42021_tool_connection: "+connectionInfos)
    return json.dumps( ci.__dict__ )

# TEST
if __name__ == '__main__':     
     print(getConnInfos())

"""
export WXO_SECURITY_SCHEMA_CONN_TC=basic_auth
export WXO_CONNECTION_CONN_TC_username=username
export WXO_CONNECTION_CONN_TC_password=password
export WXO_CONNECTION_CONN_TC_url=http://localhost:9876
"""
