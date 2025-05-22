#greetings_....py
from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool( 
    name="greeter_spanish", 
    description="Él responde con saludos en español."
    )
def greet() -> str:
    """
    Saludos a todos   
    """

    greeting = "Hola a todos"
    return greeting