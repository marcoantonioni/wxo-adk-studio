#greetings_....py
from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool( 
    name="MA42021_greeter_italian", 
    description="Questo tool è per la lingua italiana. Risponde con saluti in lingua italiana."
    )
def greet() -> str:
    """
    Saluti per tutti
    """

    greeting = "Ciao a tutti !"
    return greeting