import requests
from bs4 import BeautifulSoup as soup
import re

def list_of_names():

   #downloading website text with names
   names_page = soup(requests.get(("https://family.disney.com/articles/1000-most-popular-boy-names/")).text, "html.parser")

   # finding all names on text
   temporary_names = [imie.contents[0].string for imie in names_page.body.findAll('li')]

   # cuting list from first name 'Liam' to last name 'Jaxx'
   list_of_names = temporary_names[temporary_names.index('Liam'):(temporary_names.index('Jaxx') + 1)]

   return list_of_names, len(list_of_names)



def list_of_surnames():
   #downloading website text with surnames
   surnames_page = soup(requests.get(("https://namecensus.com/most_common_surnames.html")).text, "html.parser")

   # finding all surnames on text
   temporary_surnames = [imie.contents[0].string for imie in surnames_page.findAll('tr')]

   #limiter returning only first 1000 surnames and list starts from 'Surname"

   list_of_surnames = temporary_surnames[temporary_surnames.index('Surname') + 1:]
   return list_of_surnames[:1000]

def list_levels():
   list_levels = ['Beginner', 'Elementary', 'Intermediate', 'Upper Intermediate', 'Advanced', 'Proficient']
   return list_levels

print(list_of_surnames())
print(list_of_names())

