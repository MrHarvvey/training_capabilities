


class SoftwareEnginer:
    #atrybut klasy
    alias = "Keyboard Magician"
    #atrybuty instancji
    def __init__(self):
        self._salary = None
    # getter
    def salary(self):
        return self._salary
    #setter
    def set_salary(self, value):
        self._salary =value


se = SoftwareEnginer()

se.set_salary(6000)

print(se.salary())

print(SoftwareEnginer.__name__)