from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import CityFile, StreetFile
from .libs.validators import ValidReq, IsCity, ValidationException

object_city = CityFile()
object_city.load_file()

object_street = StreetFile()
object_street.load_file()

def validation_handling(fun):
    def new_fun(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except ValidationException as ex:
            #import ipdb;ipdb.set_trace()
            return Response({'error': ex.error_desc}, status=status.HTTP_200_OK)
    return new_fun

@api_view(['POST'])
@validation_handling
def street_search(request):
    if request.method == 'POST':
        req_validator = ValidReq()
        searched_city = req_validator(request.data)
        city_validator = IsCity(object_city=object_city)
        valued_city = city_validator(searched_city)
        city_id = object_city.search_city_id(valued_city)
        streets = object_street.search_street(city_id)
        data_response = {
            "streets": streets
        }
    return Response(data_response, status=status.HTTP_200_OK)
