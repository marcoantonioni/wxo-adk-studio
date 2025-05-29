from ibm_watsonx_orchestrate.agent_builder.tools import tool
import json, random

@tool( 
    name="MA42021_tool_weather_forecast", 
    description="This tool accecpt in input the the name of a city and a date, return an json object of type {\"city\": string, \"temperature\": integer}."
    )
def weatherForecast(city:str, date:str) -> str:
    """
    Return a weather forecast for a city and date.

    :param city: The name of a city.
    :param date: A date in format mm/dd/aaaa.
    :returns: a json object.    
    """
    temperature: int = random.randint(-10, 40)

    forecast = {"city": city.upper(), "temperature": temperature}
    return forecast