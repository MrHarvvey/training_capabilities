import csv


class StreetRecord:

    """Single street object parameters """
    def __init__(self, data):
        self._data = data

    def record_id(self):
        return self._data[4] + self._data[5]

    def city_id(self):
        return self._data[4]

    def street_name(self):
        return self._data[7]

    def to_json(self):
        return {
            'street': self.street_name()
        }


class CityRecord:

    """Single City object parameters """
    def __init__(self, data):
        self._data = data

    def record_id(self):
        return self._data[7]

    def city_name(self):
        return self._data[6]

    def to_json(self):
        return {
            'city': self.city_name()
        }


class CSVFile:

    """Importing csv file into dictionary _data object, where primary key is record_id"""
    _data = None
    _file_name = None
    _class_object: type
    def load_file(self):
        with open(self._file_name, "r") as csv_file:
            file_data = csv.reader(csv_file, delimiter=';')
            self._data = dict()
            for row in file_data:
                row_obj = self._class_object(row)
                self._data[row_obj.record_id()] = row_obj


class StreetFile(CSVFile):

    """searching and operating on Street object file"""

    _file_name = "ULIC.csv"
    _class_object = StreetRecord

    def search_street(self, city_id):
        street_list = []
        for item in self._data.items():
            object = item[1]
            if object.city_id() == city_id:
                street_list.append(object.street_name())
        return street_list


class CityFile(CSVFile):

    """searching and operating on City object file"""

    _file_name = "SIMC.csv"
    _class_object = CityRecord

    def search_city_id(self, city_named):
        for item in self._data.items():
            city = item[1]
            if city.city_name() == city_named:
                return city.record_id()





