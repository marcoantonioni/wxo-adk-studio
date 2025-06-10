from ibm_watsonx_orchestrate.agent_builder.tools import tool
import json, random

class CustomerLoyaltyInfos:
    def __init__(self, name: str):
        self.customerName = name
        self.loyaltyPoints = random.randint(100, 1000) 
        self.loyaltyLevel = random.randint(1, 5)


@tool( 
    name="MA42021_tool_customer_loyalty_informations", 
    description="This tool accept in input the the name of a customer, return an json object with the following data: number of loyalty points, loyalty level"
    )
def customerLoyaltyInformations(name:str) -> str:
    """
    The goal of this tool is about produce informations about customer loyalties transactions.
    This tool produce a json object with the customer loyalty informations.

    :param name: The name of the customer.
    :returns: a json object.    
    """
    
    cli = CustomerLoyaltyInfos(name)
    return json.dumps(cli.__dict__)

# TEST
if __name__ == '__main__':     
     print(customerLoyaltyInformations("Marco"))