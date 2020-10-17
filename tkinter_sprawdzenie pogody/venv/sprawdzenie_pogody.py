



import json
import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"callback":"test","id":"2172797","units":"%22metric%22 or %22imperial%22","mode":"xml%2C html","q":"Warszawa"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "bf66404f35mshecd7b9b3525744bp1d79a8jsna94048c27ef6"
    }

response = requests.request("GET", url, headers=headers, params=querystring)



odpowiedz = json.loads(response.text[5:-1])

pogoda_w_warszawie = odpowiedz['weather'][0]['main']
temperatura_w_warszawie = int(odpowiedz['main']['temp'] - 273.15)

print(temperatura_w_warszawie)
print(pogoda_w_warszawie)
