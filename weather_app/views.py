from django.shortcuts import render
import requests
import datetime
import os
import WEATHER_API_KEYS

# Create your views here.
def index(request):
    API_KEYS = open('WEATHER_API_KEYS', 'r').read()