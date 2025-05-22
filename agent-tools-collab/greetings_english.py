#greetings_....py
from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool( 
    name="greeter_english", 
    description="Replies with greetings in english."
    )
def greet() -> str:
    """
    Greetings to all
    """

    greeting = "Hi everyone"
    return greeting