from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from .models import *
from django.http import JsonResponse
import datetime
from rest_framework.response import Response

my_dick = {
  "data_list": [
    {"first_name": "Stefan", "second_name": "Nowak", "birth_date": "1988-06-18"},
    {"first_name": "Jan", "second_name": "Kowalski", "birth_date": "1977-11-10"}
  ]
}

@csrf_exempt
def zadanie1(request):
#    data = request.data
    return Response(my_dick)
@csrf_exempt
def zadanie2(request):
#    data = request.data
    return my_dick