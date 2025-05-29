from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool( 
    name="MA42021_topic_geography", 
    description="This tool is for topic geography."
    )
def geography() -> str:
    """
    Knowledge Geography
    """

    message = "I know all about the topic geography !"
    return message

# TEST
if __name__ == '__main__':     
     print(geography())