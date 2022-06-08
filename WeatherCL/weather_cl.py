
import settings_mine
import requests


KELVIN_TEMP = 273.15
print('Starting')

api_key = settings_mine.api_key
# city = 'Seattle'
state = 'CA'

city = input('Enter city: ') 
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key

request = requests.get(url)
json = request.json()

# parse data from json
description = json.get('weather')[0].get('description')
current_temp_celsius = json.get('main').get('temp') - KELVIN_TEMP
min_temp_celsius = json.get('main').get('temp_min') - KELVIN_TEMP
max_temp_celsius = json.get('main').get('temp_max') - KELVIN_TEMP

# print("min_temp tyep: ", type(min_temp))

print("Today's forecast: ", description)
print("Current temperature: ", round(current_temp_celsius, 2), "C")
print("Low: ", round(min_temp_celsius, 2), "C")
print("High: ", round(max_temp_celsius, 2), "C")

print('\nDone.')

