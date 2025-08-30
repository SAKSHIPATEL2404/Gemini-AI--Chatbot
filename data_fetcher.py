# data_fetcher.py
import requests
from settings import WEATHER_API_KEY

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    data = requests.get(url).json()
    if data.get("main"):
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"The temperature in {city} is {temp}°C with {desc}."
    return "Sorry, I couldn't fetch the weather."

def get_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    data = requests.get(url).json()
    price = data['bpi']['USD']['rate']
    return f"Bitcoin price is ${price}."

