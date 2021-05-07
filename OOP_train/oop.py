
#position, name, age, level, salary
se1 = ["Senior Software", "Max", 20, "Junior", 5000]
se1 = ["Junior Software", "Mariusz", 23, "Junior", 5000]


# class

class SoftwareEnginer:
    #atrybut klasy
    alias = "Keyboard Magician"
    #atrybuty instancji
    def __init__(self, name, age, level, salary):
        self.imie = name
        self.wiek = age
        self.level = level
        self.pensja = salary
    def code(self):
        print(f"{self.imie} programuje w pythonie")

    def what_language(self, *arg):

        print(f"{self.imie} programuje w pythonie i w innym jezyku na poziomie {arg[0]} {arg[1]}")

    def intruduction(self):
        print(f"{self.imie} {self.wiek} {self.level} {self.pensja}")
    #metody specjalne uzywane np do printowania instancji klasy
    def __str__(self):
        information = (f"{self.imie} {self.wiek} {self.level} {self.pensja}")
        return information
    def __eq__(self, other):
        compared = self.imie == other.imie and self.wiek == other.wiek
        return compared

    @staticmethod
    # print(se1.age_salary(24)) - dziala dzięki uzyciu dekoratora
    # print(SoftwareEnginer.age_salary(34)
    def age_salary(age):
        if age > 25:
            return 5000
        if age >30:
            return 7000
        return 10000

#instancje klasy

se1 = SoftwareEnginer("Max", 20, "Junior", 5000)
se2 = SoftwareEnginer("Max", 22, "Senior", 10000)
# print(se1.imie, se1.wiek)
# print(SoftwareEnginer.alias)


se2.what_language("srednio", "zaawansowanym")
se2.intruduction()
print(se2 == se1)

print(se1.age_salary(24))
print(SoftwareEnginer.age_salary(34))


#metoda specjalna
