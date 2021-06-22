import yaml

class UploadErrors(Exception):
    _file = 'Validation_Errors.yaml'
    _category = None
    _errors = None
    _error_code = 'ERROR-BAD-REQ'
    error_desc = str
    _language = 'PL'
    required = bool

    def __init__(self, **params):
        with open(self._file, 'r') as yaml_file:
            yaml_file = yaml.safe_load(yaml_file)
            self._errors = yaml_file.get(self._category)
            UploadErrors.error_desc = self._errors.get(self._error_code).get(self._language)
        for k, v in params.items():
            if not k.startswith("_"):
                if hasattr(self, k):
                    self.__setattr__(k, v)

#jak dodac tutaj
class Validator(UploadErrors):
    _error_code = 'VALUE-IS-REQUIRED'
    _category = 'errors'
    default_value = ""
    def _is_value(self, value):
        return bool(value)

    def __call__(self, value):
        if not self._is_value(value):
            if self.required:
                raise Validator
            else:
                return self.default_value
        return value



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
    max_len = 5
    min_len = 4
    _error_code = "ERROR-STREETLEN"

    def __call__(self, value):
        var = super(ValStreetLen, self).__call__(value)
        if len(value) > ValStreetLen.max_len:
            raise ValStreetLen
        elif len(value) < ValStreetLen.min_len:
            raise ValStreetLen
        else:
            return value

# class IsCity(Validator):
#     _error_code = "ERROR-NOT-IN-DATABASE"
#     def __call__(self, city):
#         object_city = CityFile()
#         object_city.load_file()
#         if object_city.search_city_id(city):
#             return city
#         else:
#             raise IsCity










