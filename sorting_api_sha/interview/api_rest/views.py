from .serializers import PeopleSerializers
from rest_framework import generics
from .models import People
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import hashlib
import requests



class PeopleAPIView(generics.ListAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializers

#@csrf_exempt
@api_view(['POST'])
def safe_people(request):
    print(request.data)
    if request.method == 'POST':
        try:
            list_elements = request.data['data_list']
            print(list_elements)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if any(list_elements):
            for item in list_elements:
                saveserialize = PeopleSerializers(data=item)
                if saveserialize.is_valid():
                    saveserialize.save()

            return Response(saveserialize.data, status=status.HTTP_201_CREATED)
            return Response(saveserialize.data, status=status.HTTP_400_BAD_REQUEST)


class Postac:
    def __init__(self, first_name, second_name, birth_date):
        self.first_name = first_name
        self.second_name = second_name
        self.birth_date = birth_date
        string_ob = self.first_name + self.second_name + self.birth_date
        hash_object = hashlib.sha256(string_ob.encode())
        hex_dig = hash_object.hexdigest()
        self.hash = hex_dig

def sorting(persons):
    sorteda = sorted(persons, key=lambda e: e.first_name)
    return sorteda

@api_view(['POST'])
def safe_people2(request):
    if request.method == 'POST':
        my_dick = request.data
        list_of_person = []
        try:
            data1 = my_dick['data_list']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        for person in data1:
            person = Postac(person['first_name'], person['second_name'], person['birth_date'])
            list_of_person.append(person)

        new_list = sorting(list_of_person)

        sorted_list = []
        for e in new_list:
            dick = {"first_name": e.first_name, "second_name": e.second_name, 'birth_date': e.birth_date,
                    'hash': e.hash}
            sorted_list.append(dick)
        new_dick = {'result': sorted_list}
        return Response(new_dick, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

def download_bitcoin_costs():
  try:
    req = requests.get("https://bitbay.net/API/Public/BTCPLN/orderbook.json")
  except:
    return "nie udało się pobrac danych"
  return req.json()


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




@api_view(['POST'])
def bitcoin_cost(request):
    if request.method == 'POST':
        my_data = request.data
        try:
            value_bitcoin = my_data['buy']
            price = float(value_bitcoin) * float(recalculate(download_bitcoin_costs()))
            nowy_slownik = {'price': "%.2f" % price}
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(nowy_slownik, status=status.HTTP_201_CREATED)

