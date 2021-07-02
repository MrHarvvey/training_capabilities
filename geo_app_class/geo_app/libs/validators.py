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

class IsCityExc(ValidationException):
    _error_code = "ERROR-NOT-IN-DATABASE"

class BadReq(ValidationException):
    _error_code = "ERROR-BAD-REQ"

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
    object_city = None
    object_exception = ValidationException

    def __call__(self, value):
        if value.get('city'):
            return value.get('city')
        else:
            raise self.object_exception


class ValLen(Validator):
    max_len = 20
    min_len = 3
    object_exception = StringValidator

    def __call__(self, value):
        if len(value) > self.max_len:
            raise self.object_exception
        elif len(value) < self.min_len:
            raise self.object_exception
        return value


class IsCity(ValLen):

    object_city = None
    object_exception = IsCityExc

    def __call__(self, city):
        try:
            val = ValLen.__call__(self, city)
        except Exception:
            raise StringValidator
        assert self.object_city, 'brak zainstancjonowanego objektu'
        if self.object_city.search_city_id(val):
            return city
        else:
            raise self.object_exception


