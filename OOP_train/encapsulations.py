

class SoftwareEnginer:
    #atrybut klasy
    alias = "Keyboard Magician"
    #atrybuty instancji
    def __init__(self, name, age):
        self.imie = name
        self.wiek = age
        #variables which has one underscore are protected and should not by taken outside class
        self._salary = 30000
        # variables which has two underscores are private and can not be accessed from outside
        self._num_bugs_solved = 0
    def code(self):
        self._num_bugs_solved += 1
    #getter
    def get_salary(self):
        return self._salary
    #setter
    def set_salary(self, value):
        if value < 1000:
            self._salary = 1000
        else:
            self._salary = 50000
        return self._salary


se1 = SoftwareEnginer("oskar", 23)

se1.set_salary(7000)

print(se1.get_salary())

