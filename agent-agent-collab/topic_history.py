from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool( 
    name="MA42021_topic_history", 
    description="This tool is for topic history."
    )
def history() -> str:
    """
    Knowledge History
    """

    message = "I know all about the topic history !"
    return message

# TEST
if __name__ == '__main__':     
     print(history())