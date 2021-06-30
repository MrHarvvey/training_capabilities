import yaml
from django.conf import settings


class Validator(Exception):
    _errors = None
    _error_code = "ERROR-BAD-REQ"
    _language = "PL"
    error_desc = str

    def __init__(self, **params):
        self._errors = settings.YAML_VALIDATION_ERRORS.errors
        self.error_desc = self._errors.get(self._error_code).get(self._language)
        for k, v in params.items():
            if not k.startswith("_"):
                if hasattr(self, k):
                    self.__setattr__(k, v)


class ValidReq(Validator):
    _error_code = "ERROR-BAD-REQ"
    object_city = None

    def __call__(self, value):
        if value.get('city'):
            return value.get('city')
        else:
            raise self


class ValLen(Validator):
    _error_code = "STRING-VALIDATOR"
    max_len = 45
    min_len = 4

    def __call__(self, value):
        if len(value) > ValLen.max_len:
            raise self
        elif len(value) > ValLen.min_len:
            raise self
        return value


class IsCity(ValLen):
    _error_code = "ERROR-NOT-IN-DATABASE"
    object_city = None

    def __call__(self, city):
        assert self.object_city, 'brak zainstancjonowanego objektu'
        if self.object_city.search_city_id(city):
            return city
        else:
            return self






