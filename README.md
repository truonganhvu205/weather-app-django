# IMPORTANT
[Current weather data](https://openweathermap.org/current)

# Clone project
```bash
git init
git clone https://github.com/truonganhvu205/weather-app-django.git
cd weather-app-django
```

## Install pipenv
```bash
pip3 install pipenv
```

## Activate virtual environment
```bash
pipenv --python 3.10
pipenv shell
```

## Install Django & frameworks
```bash
# Django
pipenv install django
pip3 install python-dotenv
pip3 install requests
```

# Run server
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## Deactivate virtual environment
```bash
exit
```

# Preview project
<table align='center'>
  <tr align='center'>
    <td>Weather app</td>
  </tr>
  <tr align='center'>
    <td>
      <img src='https://github.com/truonganhvu205/weather-app-django/blob/main/weather-app-django/weather-app-django-pic.png' />
    </td>
  </tr>
</table>
