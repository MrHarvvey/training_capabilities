from rest_framework import serializers
from .models import People

class PeopleSerializers(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['first_name', 'second_name', 'birth_date']