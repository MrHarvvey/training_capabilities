import csv



class CSVDataFile:
    _data = None

    _record_class: type
    _file_name = 'SIMC_Adresowy_2021-06-09.csv'
    def load_data(self):
        with open(self._file_name, "r") as cvs_file:
            file_data = csv.reader(cvs_file, delimiter=';')

            self._data = dict()
            for row in file_data:
                self._data = row



objekt = CSVDataFile()

objekt.load_data()





