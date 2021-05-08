

class Employee:
    def __init__(self, name, surname, salary):
        self.imie = name
        self.nazwisko = surname
        self.pensja = salary
    def work(self):
        print(f"imie naszego pracownika to {self.imie} oraz nazwisko {self.nazwisko} zarabia {self.pensja}")

class SoftwareEnginer(Employee):
    def __init__(self, name, surname, salary, poziom):
        super().__init__(name, surname, salary)
        self.poziom = poziom
    @staticmethod
    def currency(currency):
        if currency == "PLN":
            return "to polska waluta"
        return "nie znam takiej waluty"
    def __str__(self):
        return f"{self.imie} to jest nazwa instancji"

class Designer(SoftwareEnginer):
    def workat(self):
        print(f"imie naszego pracownika to {self.imie} oraz nazwisko {self.nazwisko} zarabia {self.pensja} na poziomie {self.poziom}")

class Kid(SoftwareEnginer):
    def __init__(self, name, surname, salary):
        self.imie = name
        self.nazwisko = surname
        self.pensja = salary





# emplo1 = Employee("MAciek", "Brzeczyszczykiewicz", 7900)
#
# softwareenginer1 = SoftwareEnginer("Wladek", "Brzeczyszczykiewicz", 79002, "sredniozaawansowany")
#
# designer1 = Designer("Dziukciarz", "Brzeczyszczykiewicz", 79002, "sredniozaawansowany")
#
# softwareenginer1.work()
# emplo1.work()
# designer1.workat()
#
# print(designer1.currency("PLN"))
# print(designer1)


#polimorfizm co to jest ?

employees = [
    Employee("MAciek", "Brzeczyszczykiewicz", 7900),
    SoftwareEnginer("Wladek", "Brzeczyszczykiewicz", 79002, "sredniozaawansowany"),
    Designer("Dziukciarz", "Brzeczyszczykiewicz", 79002, "sredniozaawansowany"),
    Kid("wer", "chuk", 23)
]

def motivate_employess(employess):
    for employee in employess:
        employee.work()

motivate_employess(employees)