from django.db import models
import hashlib
# Create your models here.


class People(models.Model):
    first_name = models.CharField(max_length=300)
    second_name = models.CharField(max_length=300)
    birth_date = models.CharField(max_length=300)
    hash = models.CharField(max_length=300)
    def __str__(self):
        return self.first_name



class Postac:
    def __init__(self, first_name, second_name, birth_date):
        self.first_name = first_name
        self.second_name = second_name
        self.birth_date = birth_date
        string_ob = self.first_name + self.second_name + self.birth_date
        hash_object = hashlib.sha256(string_ob.encode())
        hex_dig = hash_object.hexdigest()
        self.hash = hex_dig



