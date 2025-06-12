
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission
from ibm_watsonx_orchestrate.run import connections
from ibm_watsonx_orchestrate.client.connections import ConnectionType #, ExpectedCredentials

import json

CONN_BASIC_AUTH = 'app_id_tool_connection'

#type = ConnectionType.BASIC_AUTH
#type = ConnectionType.API_KEY_AUTH
#type = ConnectionType.BEARER_TOKEN
#type = ConnectionType.KEY_VALUE
#type = ConnectionType.OAUTH_ON_BEHALF_OF_FLOW

@tool( 
    name="MA42021_tool_connection", 
    description="This tool answer with connection informations.",
    permission=ToolPermission.READ_ONLY,
    expected_credentials=[
        {"app_id": CONN_BASIC_AUTH, "type": ConnectionType.BASIC_AUTH}
    ],
)
def connections() -> str:
    """
    Show connection informations
    """

    #print(connections)    

    connectionInfos= "n/a"
    otherInfos=""
    try:
        #url="http://test"
        #username="n/a"
        #password="n/a"
        url = f"{connections.basic_auth(CONN_BASIC_AUTH).url}"
        username = connections.basic_auth(CONN_BASIC_AUTH).username
        password = connections.basic_auth(CONN_BASIC_AUTH).password

        connectionInfos = "Connection configuration: "+username+" / "+password + " / " + url  
        otherInfos=str(connections)
    except:
        print("===>> EXCEPTION during execution of TOOL")
        connectionInfos = "execution of Connection informations insufficient, "+otherInfos
    
    print("===>> MA42021_tool_connection: "+connectionInfos)
    return connectionInfos

# TEST
if __name__ == '__main__':     
     print(connections())