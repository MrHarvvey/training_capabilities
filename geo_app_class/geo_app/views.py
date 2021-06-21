from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import CityFile, StreetFile
from .libs.validators import IsCity

object_city = CityFile()
object_city.load_file()

object_street = StreetFile()
object_street.load_file()

@api_view(['POST'])
def street_search(request):
    #curl -X POST -H "Content-Type: application/json" -d @towns.json 127.0.0.1:8000/street/
    error_bad_req = 4
    if request.method == 'POST':
        try:
            searched_city = request.data['city']
            city_validator = IsCity()
            valued_city = city_validator(searched_city)
        except IsCity as ex:
            error_bad_req = {'error': ex.error_desc}
            return Response(error_bad_req, status=status.HTTP_200_OK)
        try:
            searched_city = object_city.search_city_id(searched_city)
            if searched_city == None:
                return Response(error_bad_req, status=status.HTTP_200_OK)
            elif not object_street.search_street(searched_city):
                error_req_streets = {'error': "City does not have any streets"}
                return Response(error_req_streets, status=status.HTTP_200_OK)
            else:
                dict_1 = {'result': object_street.search_street(searched_city)}
            return Response(dict_1, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            error_bad_req = {'error': "Something went wrong "}
            return Response(error_bad_req, status=status.HTTP_400_BAD_REQUEST)