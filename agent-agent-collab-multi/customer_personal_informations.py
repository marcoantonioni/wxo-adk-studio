from ibm_watsonx_orchestrate.agent_builder.tools import tool
import json, random, datetime

class CustomerPersonalInfos:
    def __init__(self, name: str):
        self.customerName = name
        self.customerFromDate = str(datetime.date.today() - datetime.timedelta(days=random.randint(1, 365*200)))
        self.age = random.randint(18, 80)
        self.customerAddress = "Any street, number "+str(random.randint(1, 100))


@tool( 
    name="MA42021_tool_customer_personal_informations", 
    description="This tool accept in input the the name of a customer, return an json object with the following data: customer name, customer from date, customer address, customer age"
    )
def customerPersonalInformations(name:str) -> str:
    """
    Return customer personal informations.
    The goal of this tool is about produce the personal informations about of a customer.
    The personal informations are first name, last name, age and home address.
    This tool produce a json object with the customer personal informations.

    :param name: The name of the customer.
    :returns: a json object.    
    """
    
    cpi = CustomerPersonalInfos(name)
    return json.dumps(cpi.__dict__)

# TEST
if __name__ == '__main__':     
     print(customerPersonalInformations("Marco"))