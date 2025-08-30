import requests
from datetime import datetime
from colorama import Fore, Style, init
import time

init(autoreset=True)

# ----------- Helper Functions -----------
def weather_icon(description):
    description = description.lower()
    if "cloud" in description:
        return "☁️"
    elif "rain" in description or "drizzle" in description:
        return "🌧️"
    elif "snow" in description:
        return "❄️"
    elif "clear" in description or "sun" in description:
        return "☀️"
    elif "storm" in description or "thunder" in description:
        return "⛈️"
    elif "mist" in description or "fog" in description:
        return "🌫️"
    else:
        return "🌡️"

def color_temp(temp_c):
    if temp_c >= 30:
        return Fore.RED + str(temp_c) + "°C"
    elif temp_c <= 15:
        return Fore.BLUE + str(temp_c) + "°C"
    else:
        return Fore.GREEN + str(temp_c) + "°C"

# ----------- OpenWeatherMap Functions -----------
def get_openweathermap_current(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()
        return {
            "City": data['name'],
            "Temperature": color_temp(data['main']['temp']),
            "Weather": f"{weather_icon(data['weather'][0]['description'])} {data['weather'][0]['description']}",
            "Humidity": f"{data['main']['humidity']}%",
            "Wind": f"{data['wind']['speed']} m/s",
            "Cloudiness": f"{data['clouds']['all']}%"
        }
    except requests.exceptions.RequestException:
        return {"error": "OpenWeatherMap: City not found or API error."}

def get_openweathermap_forecast(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric&cnt=4"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()
        forecast_list = []
        for item in data['list']:
            time_str = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d %H:%M')
            forecast_list.append({
                "Time": time_str,
                "Temp": color_temp(item['main']['temp']),
                "Weather": f"{weather_icon(item['weather'][0]['description'])} {item['weather'][0]['description']}"
            })
        return forecast_list
    except requests.exceptions.RequestException:
        return [{"error": "OpenWeatherMap forecast not available."}]

# ----------- WeatherAPI Functions -----------
def get_weatherapi_current(city, api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()
        return {
            "City": data['location']['name'],
            "Temperature": color_temp(data['current']['temp_c']),
            "Condition": f"{weather_icon(data['current']['condition']['text'])} {data['current']['condition']['text']}",
            "Humidity": f"{data['current']['humidity']}%",
            "Wind": f"{data['current']['wind_kph']} kph",
            "Cloudiness": f"{data['current']['cloud']}%"
        }
    except requests.exceptions.RequestException:
        return {"error": "WeatherAPI.com: City not found or API error."}

def get_weatherapi_forecast(city, api_key):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=3"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()
        forecast_list = []
        for day in data['forecast']['forecastday']:
            forecast_list.append({
                "Date": day['date'],
                "Max Temp": color_temp(day['day']['maxtemp_c']),
                "Min Temp": color_temp(day['day']['mintemp_c']),
                "Condition": f"{weather_icon(day['day']['condition']['text'])} {day['day']['condition']['text']}"
            })
        return forecast_list
    except requests.exceptions.RequestException:
        return [{"error": "WeatherAPI.com forecast not available."}]

# ----------- Display Functions -----------
def display_weather(title, data):
    print(Fore.CYAN + f"\n{title} Current Weather")
    print(Fore.CYAN + "-"*50)
    if "error" in data:
        print(Fore.RED + data["error"])
    else:
        for k, v in data.items():
            print(Fore.YELLOW + f"{k}: {Fore.GREEN}{v}")
    print(Fore.CYAN + "-"*50)

def display_forecast(title, forecast_list):
    print(Fore.MAGENTA + f"\n{title} Forecast")
    print(Fore.MAGENTA + "-"*50)
    for item in forecast_list:
        if "error" in item:
            print(Fore.RED + item["error"])
        else:
            print(", ".join([f"{k}: {v}" for k,v in item.items()]))
    print(Fore.MAGENTA + "-"*50)

# ----------- Main Interactive Loop -----------
def main():
    owm_api_key = "8a77d3b7d42acb7be6c28dafc361b872"
    weatherapi_key = "a3a6f141e40543608b6101205252408"

    city = input(Fore.CYAN + "Enter city name: ").strip().title()

    print(Fore.CYAN + "\nChoose API to display:")
    print("1 - OpenWeatherMap")
    print("2 - WeatherAPI.com")
    print("3 - Both")
    choice = input("Enter choice (1/2/3): ").strip()

    try:
        refresh_interval = int(input("Enter auto-refresh interval in minutes (0 to disable): ").strip())
    except ValueError:
        refresh_interval = 0

    while True:
        print(Fore.CYAN + f"\n--- Weather Update for {city} ---\n")

        if choice in ["1","3"]:
            display_weather("OpenWeatherMap", get_openweathermap_current(city, owm_api_key))
            display_forecast("OpenWeatherMap (Next 12 hours)", get_openweathermap_forecast(city, owm_api_key))

        if choice in ["2","3"]:
            display_weather("WeatherAPI.com", get_weatherapi_current(city, weatherapi_key))
            display_forecast("WeatherAPI.com (Next 3 Days)", get_weatherapi_forecast(city, weatherapi_key))

        if refresh_interval <= 0:
            break
        else:
            print(Fore.CYAN + f"\nNext update in {refresh_interval} minute(s)...")
            time.sleep(refresh_interval * 60)

if __name__ == "__main__":
    main()


