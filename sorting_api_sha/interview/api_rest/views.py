from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PeopleSerializers
from rest_framework.views import APIView

my_dick = {
  "data_list": [
    {"first_name": "Stefan", "second_name": "Nowak", "birth_date": "1988-06-18"},
    {"first_name": "Jan", "second_name": "Kowalski", "birth_date": "1977-11-10"}
  ]
}

class PeopleAPIView(APIView):
    serializers = PeopleSerializers
_dick)