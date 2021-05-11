from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import json
from .models import *
from django.http import JsonResponse
import datetime


my_dick = {
  "data_list": [
    {"first_name": "Stefan", "second_name": "Nowak", "birth_date": "1988-06-18"},
    {"first_name": "Jan", "second_name": "Kowalski", "birth_date": "1977-11-10"}
  ]
}


def zadanie1(request):
    data = request.data
    return request.data

def zadanie2(request):
    data = request.data
    return request.data