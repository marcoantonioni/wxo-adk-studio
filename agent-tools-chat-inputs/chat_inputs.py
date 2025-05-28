from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool( 
    name="MA42021_tool_input_params", 
    description="This tool accecpt in input the first name and last name of type string."
    )
def fullName(firstName:str, lastName:str) -> str:
    """
    Join firstName and lastName

    :param firstName: The first name.
    :param lastName: The last name.
    :returns: The full name.    
    """

    fullName = "Your fullname is "+firstName+" "+lastName #+" and tool used is MA42021_tool_input_params"
    return fullName