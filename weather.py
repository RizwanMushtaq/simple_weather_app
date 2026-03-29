import requests
from dotenv import (
    load_dotenv,
)
import os


load_dotenv()


def get_current_weather():
    print("\n*** Get Current Weather Conditions ***\n")
    city = input("\nPlease enter a city anem:\n")
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=metric"
    print(request_url)

    weather_data = requests.get(request_url).json()
    current_city = weather_data["name"]
    current_temp = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    description = weather_data["weather"][0]["description"]

    print(f"Current weather for {current_city}")
    print(f"\nThe temp is {current_temp}")
    print(f"Feels like {feels_like} and {description}\n")


if __name__ == "__main__":
    get_current_weather()
