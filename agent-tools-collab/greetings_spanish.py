#greetings_....py
from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool( 
    name="MA42021_greeter_spanish", 
    description="Esta tool es para el idioma español. Él responde con saludos en español."
    )
def greet() -> str:
    """
    Saludos a todos   
    """

    greeting = "Hola a todos !"
    return greeting