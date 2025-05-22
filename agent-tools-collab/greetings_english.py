#greetings_....py
from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool( 
    name="MA42021_greeter_english", 
    description="This tool is for english language. Replies with greetings in english."
    )
def greet() -> str:
    """
    Greetings to all
    """

    greeting = "Hi everyone !"
    return greeting