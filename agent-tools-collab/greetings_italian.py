#greetings_....py
from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool( 
    name="greeter_italian", 
    description="Risponde con saluti in lingua italiana."
    )
def greet() -> str:
    """
    Saluti per tutti
    """

    greeting = "Ciao a tutti"
    return greeting