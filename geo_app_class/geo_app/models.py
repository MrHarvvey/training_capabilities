from django.db import models
import csv


class CityCsv:

    _data = None
    _file_name = "SIMC_Adresowy_2021-06-09.csv"

    def __init__(self, data):
        self._data = data


    def load_data(self, csv_file):
        with open(self._file_name) as csv_data:
            data_file = csv.reader(csv_data)
            return data_file



