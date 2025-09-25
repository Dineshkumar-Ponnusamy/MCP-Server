import os
import requests
from dotenv import load_dotenv
from fastmcp import FastMCP

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
if not API_KEY:
    raise ValueError("WEATHER_API_KEY environment variable not set")

mcp = FastMCP("Weather Bot", "Get current weather information for a given city.")

@mcp.tool
def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return f"Error: Unable to fetch weather data for {city}."
    
    data = response.json()
    weather_desc = data['weather'][0]['description']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    
    return (f"The current weather in {city} is {weather_desc} with a temperature of "
            f"{temp}°C and humidity of {humidity}%.")

if __name__ == "__main__":
    mcp.run(transport="stdio")