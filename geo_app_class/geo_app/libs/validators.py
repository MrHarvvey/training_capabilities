import re
import yaml


class Validators(Exception):
    pass


class UploadYaml:
    _file = None
    _what_download = None
    def load_file(self):
        with open(self._file, 'r') as yaml_file:
            try:
                yaml_file = yaml.safe_load(yaml_file)
                self._data = yaml_file.get(self._what_download)
            except yaml.YAMLError as exc:
                return exc


class Validation(UploadYaml, Exception):
    _file = 'Validation_Errors.yaml'
    _what_download = 'errors'
    def search_error(self, error_code):
        error = self._data.get(error_code).get('PL')
        return error
    def city_check(self, city_name):
        if re.match("^[a-zA-Z]+$", city_name):
            return city_name
        else:
            return self.search_error("ERROR-BAD-CITY")



pliki = Validation()

pliki.load_file()

print(pliki.city_check("Skierniewice"))

