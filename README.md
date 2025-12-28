🌦️ Weather Forecasting App

A small Python script that calls WeatherAPI to show current weather for a city.

✨ FEATURES

• Fetches current weather: temperature, feels-like temperature, humidity, wind speed, UV index, visibility, condition
• Loads API key from .env (not committed)
• Uses requests and python-dotenv
• Handles invalid city input and network errors

⚙️ QUICK START

• Clone the repository and open the project folder
• Create and activate a virtual environment (Windows PowerShell):

python -m venv .venv
..venv\Scripts\Activate.ps1

• 📦 Install dependencies:

pip install -r requirements.txt

• 🔑 Create a .env file in the project folder and add your WeatherAPI key:

WEATHER_API_KEY=your_api_key_here

• 🚀 Run the app:

python "Weather Forecasting App.py"

• 🏙️ Type a city name (example: Vadodara) when prompted

🖥️ EXAMPLE OUTPUT

Weather data for Vadodara

Local time is 2025-12-28 14:54
Last updated at 2025-12-28 14:45

Condition is Sunny
Temperature is 28.9 Celsius
Feels like 27.1 Celsius

Humidity is 23 %
Wind is 4.3 kph
UV index is 3.8
Visibility is 10.0 km

🧪 DEVELOPMENT AND TESTING NOTES

• Add pytest tests that mock the WeatherAPI (optional)
• Use black, ruff, or flake8 for formatting/linting
• Pre-commit hooks are optional

🔐 SECURITY NOTES

• Do NOT commit your real API key
• Keep keys in .env or environment variables
• If your key is exposed, rotate it in the WeatherAPI dashboard
• Make sure .env is listed in .gitignore
