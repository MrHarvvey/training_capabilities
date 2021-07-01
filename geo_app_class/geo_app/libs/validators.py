import yaml
from django.conf import settings



class ValidationException(Exception):
    _errors = None
    _error_code = "ERROR-BAD-REQ"
    _language = "PL"
    error_desc = str
    object_exception = None

    def __init__(self):
        self._errors = settings.YAML_VALIDATION_ERRORS.errors
        self.error_desc = self._errors.get(self._error_code).get(self._language)

class StringValidator(ValidationException):
    _error_code = "STRING-VALIDATOR"
    max_len = 20
    min_len = 10


class Validator:
    _errors = None
    _error_code = "ERROR-BAD-REQ"
    _language = "PL"
    error_desc = str

    def __init__(self, **params):
        for k, v in params.items():
            if not k.startswith("_"):
                if hasattr(self, k):
                    self.__setattr__(k, v)


class ValidReq(Validator):
    _error_code = "ERROR-BAD-REQ"
    object_city = None
    object_exception = StringValidator

    def __call__(self, value):
        if value.get('city'):
            return value.get('city')
        else:
            raise self.object_exception


class ValLen(Validator):

    _error_code = "STRING-VALIDATOR"
    max_len = 20
    min_len = 10

    def __call__(self, value):
        if len(value) > self.max_len:
            raise self
        elif len(value) < self.min_len:
            raise self
        return value

class IsCity(ValLen):
    _error_code = "ERROR-NOT-IN-DATABASE"
    object_city = None

    def __call__(self, city):

        "zapytac czy tutaj wywołanie super może być z błędem z ValLen"
        val = ValLen.__call__(self, city)
        import ipdb
        ipdb.set_trace()
        assert self.object_city, 'brak zainstancjonowanego objektu'
        if self.object_city.search_city_id(val):
            return city
        else:
            raise self




#old version

# class Validator(Exception):
#     _errors = None
#     _error_code = "ERROR-BAD-REQ"
#     _language = "PL"
#     error_desc = str
#
#     def __init__(self, **params):
#         self._errors = settings.YAML_VALIDATION_ERRORS.errors
#         self.error_desc = self._errors.get(self._error_code).get(self._language)
#         for k, v in params.items():
#             if not k.startswith("_"):
#                 if hasattr(self, k):
#                     self.__setattr__(k, v)
#
#
# class ValidReq(Validator):
#     _error_code = "ERROR-BAD-REQ"
#     object_city = None
#
#     def __call__(self, value):
#         if value.get('city'):
#             return value.get('city')
#         else:
#             raise self
#
#
# class ValLen(Validator):
#     _error_code = "STRING-VALIDATOR"
#     max_len = 20
#     min_len = 10
#
#     def __call__(self, value):
#         if len(value) > self.max_len:
#             raise self
#         elif len(value) < self.min_len:
#             raise self
#         return value
#
#
# class IsCity(ValLen):
#     _error_code = "ERROR-NOT-IN-DATABASE"
#     object_city = None
#
#     def __call__(self, city):
#
#         "zapytac czy tutaj wywołanie super może być z błędem z ValLen"
#         val = ValLen.__call__(self, city)
#         import ipdb
#         ipdb.set_trace()
#         assert self.object_city, 'brak zainstancjonowanego objektu'
#         if self.object_city.search_city_id(val):
#             return city
#         else:
#             raise self



