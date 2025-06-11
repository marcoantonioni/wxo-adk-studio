from ibm_watsonx_orchestrate.agent_builder.tools import tool
import json, random, datetime

class CustomerPersonalTransaction:
    def __init__(self, name: str):
        self.customerName = name
        self.purchaseDate = str(datetime.date.today() - datetime.timedelta(days=random.randint(1, 365)))
        self.purchaseAmount = random.randint(10, 10000)


@tool( 
    name="MA42021_tool_customer_purchase_transactions", 
    description="This tool accept in input the the name of a customer, return an json object with the following list of records: purchase date, purchase amount"
    )
def customerPersonalTransactions(name:str) -> str:
    """
    The goal of this tool is about produce informations about customer purchase transactions.
    The data returned is a list of objects each one with the date of purchase and the amount of purchase.
    This tool produce a json object with the list of all purchase transactions made by the customer.

    :param name: The name of the customer.
    :returns: a json object.    
    """
    
    transactions = [CustomerPersonalTransaction(name), CustomerPersonalTransaction(name), CustomerPersonalTransaction(name)]
    return json.dumps([{"customerName": obj.customerName, "purchaseDate": obj.purchaseDate, "purchaseAmount": obj.purchaseAmount} for obj in transactions])

# TEST
if __name__ == '__main__':     
     print(customerPersonalTransactions("Marco"))