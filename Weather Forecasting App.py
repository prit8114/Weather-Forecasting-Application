import os
import requests
import json
from dotenv import load_dotenv #to load environment variables from .env file
load_dotenv()

def main():
    API_KEY = os.getenv("WEATHER_API_KEY")

    if not api_key:
        print("API key not found. Please add WEATHER_API_KEY in your .env file.")
        return

city=input("Enter the name of the city:")
url=f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

try:
    r=requests.get(url, timeout=5)
    r.raise_for_status()  # Raise an error for bad status codes
    weather_data=json.loads(r.text)
except requests.exceptions.RequestException as e:
    print("Error fetching weather data:", e)
    exit()

if 'error' in weather_data:
    print("Error from Server:", weather_data['error']['message'])
    exit()

print("\nWeather data for", city)
print("\nLocal time is",weather_data['location']['localtime'])
print("Last updated at", weather_data['current']['last_updated'])
print("\nCondition is",weather_data['current']['condition']['text'])
print("Temperature is", weather_data['current']['temp_c'],"Celcius")
print("Feels like", weather_data['current']['feelslike_c'], "Celcius")
print("\nHumidity is",weather_data['current']['humidity'],"%")
print("Wind is", weather_data['current']['wind_kph'], "kph")
print("UV index is",weather_data['current']['uv'])
print("Visibility is",weather_data['current']['vis_km'], "km")

if __name__ == "__main__":
    main()
