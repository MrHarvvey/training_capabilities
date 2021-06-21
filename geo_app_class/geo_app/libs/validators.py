import re
import yaml


class UploadErrors(Exception):
    _file = None
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
    _file = 'Validation_Errors.yaml'
    _error_code = 'ERROR-BAD-REQ'
    _category = 'errors'
    def __call__(self, *args, **kwargs):
        return UploadErrors.error_desc


class IsCity(Validator):
    _error_code = "ERROR-STREET-DOES-NOT-FOUND"

    def __call__(self, value):
        if len(value) > 20:
            raise IsCity
        return value



class IsStreet(Validator):
    _error_code = "ERROR-STREET-DOES-NOT-FOUND"
    def __call__(self, value):
        if len(value) < 20:
            raise IsStreet
        return value



validacja = IsCity()



try:
    validacja("kasdkjasdkskljdasddassssssssssssssss")
except Validator as ex:
    print(ex.error_desc)









