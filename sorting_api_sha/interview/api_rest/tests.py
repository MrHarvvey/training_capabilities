from django.test import TestCase
import requests
import json
data = {
  "data_list": [
    {"first_name": "Artur", "second_name": "Nowak", "birth_date": "1988-06-18"},
    {"first_name": "Stefan", "second_name": "Nowak", "birth_date": "1988-06-18"},
    {"first_name": "Maciek", "second_name": "Nowak", "birth_date": "1988-06-18"},
    {"first_name": "Oskar", "second_name": "Nowak", "birth_date": "1988-06-18"},
    {"first_name": "Jandasas", "second_name": "Kowalski", "birth_date": "1977-11-10"}
  ]
}
headers = {'Content-type': 'application/json'}

#req = requests.post("http://127.0.0.1:8001/zadanie3/", data=json.dumps(data), headers=headers)

# Create your tests here.

data = {
    "buy": "0.1234"
}



#req = requests.get("https://bitbay.net/API/Public/BTCPLN/orderbook.json")

#print(req.text)


def download_bitcoin_costs():
  try:
    req = requests.get("https://bitbay.net/API/Public/BTCPLN/orderbook.json")
  except:
    return "nie udało się pobrac danych"
  return req.text


def recalculate(dane):
  try:
    dane = dane['bids']
    total_btc = 0
    total_btc_price = 0
    for item in dane:
      total_btc += int(item[1])
      total_btc_price += int(item[0])
  except:
    return "nie udalo sie obliczyc"
  return total_btc, total_btc_price

#print(download_bitcoin_costs())

print(recalculate(download_bitcoin_costs()))