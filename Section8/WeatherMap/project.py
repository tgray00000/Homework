import requests
from dotenv import load_dotenv
import pandas as pd
import json
import os

#Load API Key
load_dotenv()
api_key = os.getenv("API_KEY")
#print(api_key)

# Location: Dublin
#Construst the API request URL: Current weather
Dublin_url = 'https://api.openweathermap.org/data/2.5/weather?q=Dublin&appid=' + api_key
#API request to Openweather
response = requests.get(Dublin_url)
#print(response.json())

weather_data = json.loads(response.text)

#Extract relevant weather information from the API response: temperature, humidity, and weather description.
Location = weather_data['name']
stuff = weather_data['sys']
weather_detail = weather_data['main']
weather_desc = weather_data['weather']

print("The weather in," ,Location, "Which is in,", stuff['country'])
print("The temp is,", weather_detail['temp'])
print("But feels like", weather_detail['feels_like'])

