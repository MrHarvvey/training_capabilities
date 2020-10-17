
import json
import requests


class Person:
  def __init__(self, miasto):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    querystring = {"callback": "test", "id": "2172797", "units": "%22metric%22 or %22imperial%22",
                     "mode": "xml%2C html", "q": miasto}
    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "bf66404f35mshecd7b9b3525744bp1d79a8jsna94048c27ef6"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    self.odpowiedz = json.loads(response.text[5:-1])
    self.zachmurzenie = json.loads(response.text[5:-1])['weather'][0]['main']
    self.temp = int((json.loads(response.text[5:-1])['main']['temp']) - 273.15)
    self.odczuwalna = int((json.loads(response.text[5:-1])['main']['feels_like']) - 273.15)
    self.temp_min = int((json.loads(response.text[5:-1])['main']['temp_min']) - 273.15)
    self.temp_max = int((json.loads(response.text[5:-1])['main']['temp_max']) - 273.15)

print(Person("Warszawa").temp_max)


def create_winget(self):
    jaka_pogoda.insert(tk.INSERT, "Zachmurzenie: " + Pogoda(miasto.get()).zachmurzenie + "\n")
    jaka_pogoda.insert(tk.INSERT, "Temperatura: " + str(Pogoda(miasto.get()).temp) + " C\n")
    jaka_pogoda.insert(tk.INSERT, "Odczuwalna Temperatura: " + str(Pogoda(miasto.get()).odczuwalna) + " C\n")
    jaka_pogoda.insert(tk.INSERT, "Minimalna Temperatura: " + str(Pogoda(miasto.get()).temp_min) + " C\n")
    jaka_pogoda.insert(tk.INSERT, "Maksymalna Temperatura: " + str(Pogoda(miasto.get()).temp_max) + " C\n")
