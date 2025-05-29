from ibm_watsonx_orchestrate.agent_builder.tools import tool
import json, random, datetime

class WeatherForecast:
    def __init__(self, city: str, date: str):
        self.city = city
        self.date = date
        self.temperature = random.randint(-10, 40)
        self.dateOfRequest = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")


@tool( 
    name="MA42021_tool_weather_forecast", 
    description="This tool accecpt in input the the name of a city and a date, return an json object with the following data city, forecast date, temperature, date of the request."
    )
def weatherForecast(city:str, date:str) -> str:
    """
    Return a weather forecast for a city and date.

    :param city: The name of a city.
    :param date: A date in format mm/dd/aaaa.
    :returns: a json object.    
    """
    
    wf = WeatherForecast(city.upper(), date)
    return json.dumps(wf.__dict__)