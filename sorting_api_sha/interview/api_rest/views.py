from .serializers import PeopleSerializers, People1Serializers
from rest_framework import generics
from .models import People, Postac
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .utils import download_bitcoin_costs as download_bitcoin_costs
from .utils import recalculate as recalculate
from .utils import sorting as sorting
import hashlib

class PeopleAPIView(generics.ListAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializers

@api_view(['POST'])
def safe_people_db(request):
    #print(request.data)
    if request.method == 'POST':
        try:
            list_elements = request.data['data_list']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if any(list_elements):
            for item in list_elements:
                saveserialize = PeopleSerializers(data=item)
                if saveserialize.is_valid():
                    string_hash = item['first_name'] + item['second_name'] + item['birth_date']
                    hash_object = hashlib.sha256(string_hash.encode())
                    hex_dig = hash_object.hexdigest()
                    new_ob = People(first_name=item['first_name'], second_name=item['second_name'], birth_date=item['birth_date'], hash=hex_dig)
                    new_ob.save()
            all_items = People.objects.all()
            serializer = People1Serializers(all_items, many=True)
            dict_1 = {'result': serializer.data}
            return Response(dict_1, status=status.HTTP_201_CREATED)
            return Response(saveserialize.data, status=status.HTTP_400_BAD_REQUEST)


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

#returning bitcoin price
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

@api_view(['POST'])
def hash_search(request):
    # retuning sets with persons from database with specific hash value, example of usage curl -X POST -H "Content-Type: application/json" -d @hash.json 127.0.0.1:8000/hash_search/
    # @hash.json body includes json:
    # {
    #     "hash": "02b1e82bb99249f3e32e86d219763dc62d103cb047c6c887e0e5d9b80557c637" - what hash value you want to delete (if multiple objects has the same hash botj will be deleted)
    # }
    if request.method == 'POST':
        my_data = request.data
        try:
            hash_value = my_data['hash']
            person = People.objects.filter(hash=hash_value)
            serializer = People1Serializers(person, many=True)
        except People.DoesNotExist:
            dic = {'error': 'This person does not exist'}
            return Response(dic, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def hash_del(request):
    # deleting person from database with specific hash value, example of usage curl -X POST -H "Content-Type: application/json" -d @hash.json 127.0.0.1:8000/hash_del/
    # @hash.json body includes json:
    # {
    #     "hash": "02b1e82bb99249f3e32e86d219763dc62d103cb047c6c887e0e5d9b80557c637" - what hash value you want to delete (if mutliple objects has the same hash botj will be deleted)
    # }
    if request.method == 'POST':
        my_data = request.data
        try:
            hash_value = my_data['hash']
            person = People.objects.filter(hash=hash_value).delete()
            if person[0] == 0:
                dic2 = {'error': 'Person Was not found'}
                return Response(dic2, status=status.HTTP_400_BAD_REQUEST)
        except:
            dic = {'error': "something went wrong "}
            return Response(dic, status=status.HTTP_400_BAD_REQUEST)
        dic = {'error': f'Object with hash deleted  {hash_value} where was {person[0]} with this hash number'}
        return Response(dic, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def list_persons(request):
    # returning list of persons from database object Person, example curl -X POST -H "Content-Type: application/json" -d @all.json 127.0.0.1:8000/list_persons/
    # @all.json body must includes json with one parameter count:
    # {
    #     "count": "10" - how many objects you want to return
    # }
    if request.method == 'POST':
        my_data = request.data
        try:
            query_number = int(my_data['count'])
            person = People.objects.all()[:query_number]
            serializer = People1Serializers(person, many=True)
        except People.DoesNotExist:
            dic = {'error': 'This person does not exist'}
            return Response(dic, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)