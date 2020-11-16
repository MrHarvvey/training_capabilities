import requests
from bs4 import BeautifulSoup as soup
import re
import random

def list_of_names():

   #downloading website text with names
   names_page = soup(requests.get(("https://family.disney.com/articles/1000-most-popular-boy-names/")).text, "html.parser")

   # finding all names on text
   temporary_names = [imie.contents[0].string for imie in names_page.body.findAll('li')]

   # cuting list from first name 'Liam' to last name 'Jaxx'
   list_of_names = temporary_names[temporary_names.index('Liam'):(temporary_names.index('Jaxx') + 1)]

   return list_of_names



def list_of_surnames():
   #downloading website text with surnames
   surnames_page = soup(requests.get(("https://namecensus.com/most_common_surnames.html")).text, "html.parser")

   # finding all surnames on text
   temporary_surnames = [imie.contents[0].string for imie in surnames_page.findAll('tr')]

   #limiter returning only first 1000 surnames and list starts from 'Surname"

   list_of_surnames = temporary_surnames[temporary_surnames.index('Surname') + 1:1000]
   return list_of_surnames

def list_levels():
   list_levels = ['Beginner', 'Elementary', 'Intermediate', 'Upper Intermediate', 'Advanced', 'Proficient']
   return list_levels

def list_of_emails():
   nazwisko = list_of_surnames()
   imie = list_of_names()
   list_emails = [(x.lower() +"_"+ y.lower() + "@gmail.com") for x in imie for y in nazwisko]
   return list_emails


# it takes to much memory

# def list_of_students():
#    emaile = list_of_emails()
#    names = list_of_names()
#    surnames = list_of_surnames()
#    levels = list_levels()
#    list_students = [(a,b,random.choice(levels),random.randint(18,65),e) for a in names for b in surnames for e in emaile]
#    return list_students
#
#
# print(list_of_students())
