
import settings_mine
import requests


print('Starting')

api_key = settings_mine.api_key
# city = 'Seattle'
state = 'CA'

city = input('Enter city: ') 
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_key

request = requests.get(url)
json = request.json()

description = json.get('weather')[0].get('description')
print("Today's forecase:", description)

print('Done.')

