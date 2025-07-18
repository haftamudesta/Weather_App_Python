from dotenv import load_dotenv
from pprint import pprint
import os
import requests

load_dotenv()


def get_current_weather(city="Addis Ababa"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == "__main__":
    print("\n***Get current weather condition...***\n")
    city = input("\nPlease enter city name: ")
    if not city or not city.strip():
        city = "Addis Ababa"
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)
