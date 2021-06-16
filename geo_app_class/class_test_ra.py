import csv


class CVSRecord:
    def __init__(self, data):
        self._data = data

    def can_add_record(self):
        return True

class CSVDataFile:
    def load_data(self):
        with open(self._file_name, "r") as cvs_file:
            file_data = csv.reader(cvs_file, delimiter=';')
            self._data = dict()
            for row in file_data:
                row_obj = self._record_class(row)
                # import ipdb; ipdb.set_trace()
                if row_obj.can_add_record():
                    self._data[row_obj.record_id()] = row_obj


class Street(CVSRecord):

    def record_id(self):
        return self._data[4] + ";" + self._data[5]

    @property
    def street_type(self):
        return self._data[6]

    @property
    def street_name(self):
        return self._data[7] + " " + self._data[8]

    @property
    def city_symbol(self):
        return self._data[4]

    def to_json(self):
        return {
            "id": self.record_id(),
            "name": self.street_name,
            "type": self.street_type
        }


class Streets(CSVDataFile):
    _file_name = "ULIC.csv"
    _record_class = Street

    def search_streets(self, city_symbol):
        res = []
        for id, street in self._data.items():
            if street.city_symbol == city_symbol:
                res.append(street)
        return res


class City(CVSRecord):

    def record_id(self):
        return self._data[7] + ";" + self._data[8]

    @property
    def city_name(self):
        return self._data[6]

    def is_city(self):
        return self._data[4] == "96"

    @property
    def symbol(self):
        return self._data[8]

    def to_json(self):
        return {
            "id": self.record_id(),
            "name": self.city_name
        }


class Cities(CSVDataFile):
    _record_class = City
    _file_name = "SIMC.csv"

    def search_city(self, city_name):
        for c in self._data.values():
            if c.city_name == city_name:
                return c


street_data = Streets()
street_data.load_data()

city_data = Cities()
city_data.load_data()

print(street_data.search_streets("0090316"))
print(city_data.search_city("Warszawa").to_json())
