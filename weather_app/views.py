from django.shortcuts import render

import datetime
import requests

import os
from dotenv import load_dotenv

load_dotenv()

# Create your views here.
WEATHER_API_KEY = str(os.getenv('WEATHER_API_KEY'))

def get_weather_data(city, weather_api_key):
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
    
    current_weather_res = requests.get(current_weather_url.format(city, weather_api_key)).json()
    
    current_weather_data = {
        'date': datetime.datetime.fromtimestamp(current_weather_res['dt']).strftime('%a, %b %d'),
        'city': city,
        'temperature': current_weather_res['main']['temp'],
        'min_temp': current_weather_res['main']['temp_min'],
        'max_temp': current_weather_res['main']['temp_max'],
        'humidity': current_weather_res['main']['humidity'],
        'description': current_weather_res['weather'][0]['description'],
        'icon': current_weather_res['weather'][0]['icon'],
    }
    
    return current_weather_data

def weather_view(request):
    if request.method == 'POST':
        city = request.POST['city']
        current_weather = get_weather_data(city, WEATHER_API_KEY)
        
        return render(request, 'weather.html', {'current_weather': current_weather})
    else:
        return render(request, 'weather.html')