import requests

#donloading bitcoin cost form webside
def download_bitcoin_costs():
  try:
    req = requests.get("https://bitbay.net/API/Public/BTCPLN/orderbook.json")
  except:
    return "nie udało się pobrac danych"
  return req.json()

#recalculating bitcoin price
def recalculate(dane):
  try:
    dane = dane['bids']
    total_btc = 0
    total_btc_price = 0
    for item in dane:
      total_btc += int(item[1])
      total_btc_price += int(item[0])
    btc_price = total_btc_price/total_btc
  except Exception as e:
    return e
  return float(btc_price)



def sorting(persons):
    sorteda = sorted(persons, key=lambda e: e.first_name)
    return sorteda