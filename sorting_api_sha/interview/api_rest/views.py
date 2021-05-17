from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.response import api_view

my_dick = {
  "data_list": [
    {"first_name": "Stefan", "second_name": "Nowak", "birth_date": "1988-06-18"},
    {"first_name": "Jan", "second_name": "Kowalski", "birth_date": "1977-11-10"}
  ]
}


@api_view
@csrf_exempt
def zadanie1(request):
#    data = request.data
    return JsonResponse(my_dick)


@api_view
@csrf_exempt
def zadanie2(request):
#    data = request.data
    return JsonResponse(my_dick)