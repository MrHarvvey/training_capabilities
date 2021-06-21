import re
import yaml
from ..views import object_city

class UploadErrors(Exception):
    _file = 'Validation_Errors.yaml'
    _category = None
    _errors = None
    _error_code = 'ERROR-BAD-REQ'
    error_desc = str
    _language = 'PL'

    def __init__(self):
        with open(self._file, 'r') as yaml_file:
            yaml_file = yaml.safe_load(yaml_file)
            self._errors = yaml_file.get(self._category)
            UploadErrors.error_desc = self._errors.get(self._error_code).get(self._language)

#jak dodac tutaj
class Validator(UploadErrors):
    _error_code = 'ERROR-BAD-REQ'
    _category = 'errors'
    def __call__(self, *args, **kwargs):
        return UploadErrors.error_desc


class ValCityLen(Validator):
    _error_code = "ERROR-STREET-DOES-NOT-FOUND"
    max_len = 45
    min_len = 4
    def __call__(self, value):
        if len(value) > ValCityLen.max_len:
            raise ValCityLen
        elif len(value) > ValCityLen.min_len:
            raise ValCityLen
        return value



class ValStreetLen(Validator):
    _error_code = "ERROR-STREET-DOES-NOT-FOUND"
    def __call__(self, value):
        if len(value) < 20:
            raise ValStreetLen
        return value

class IsCity(Validator):
    _error_code = "ERROR-NOT-IN-DATABASE"
    def __call__(self, city):
        if object_city.search_city_id(city):
            return city
        else:
            raise IsCity








validacja = IsCity()



try:
    validacja("kasdkjasdkskljdasddassssssssssssssss")
except Validator as ex:
    print(ex.error_desc)









