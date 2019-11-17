import requests
import json
import pandas as pd



# Downloads weather data from Toronto City station from GOC db

for month in range(13):
    url = f"""https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=31688&Year=2018&Month={month}&Day=14&timeframe=1&submit=Download+Data"""
    request = requests.get(url)

    with open(f'weather_data/toronto_weather_data_{month}.csv', 'w') as file:
        file.write(request.text)




        