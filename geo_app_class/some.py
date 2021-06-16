import csv

class StreetRecord:
    def __init__(self, data):
        self._data = data
    def city_id(self):
        return self._data[5]
    def street_name(self):
        return self._data[7]

class CityRecord:
    def __init__(self, data):
        self._data = data
    def city_id(self):
        return self._data[7]
    def city_name(self):
        return self._data[6]




class CSVFile:
    _data = None
    _file_name = None
    _class_object: type
    def load_file(self):
        with open(self._file_name, "r") as csv_file:
            file_data = csv.reader(csv_file, delimiter=';')
            for row in file_data:
                row_obj = self._class_object(row)
                self._data[row_obj.city_id()] = row_obj


# class StreetFile(CSVFile):
#     _file_name = "ULIC.csv"
#     _class_object = StreetRecord
#     def search_street(self, city_id):
#         street_list = []
#         for item in self._data.keys():
#             print(item)
#             if item == city_id:
#                 street_list.append(self.)

class CityFile(CSVFile):
    _file_name = "SIMC.csv"
    _class_object = CityRecord
    def search_city_id(self, city_name):
        for item in self._data.items():
            if item.city_name() == city_name:
                return item.city_id()


dane_ulicy = CityFile()

CSVFile.load_file()

searched_city = CityFile.search_city_id("Skierniewice")

print(searched_city)