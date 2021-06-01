# This is a sample Python script.
import hashlib

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Postac:
    def __init__(self, first_name, second_name, birth_date):
        self.first_name = first_name
        self.second_name = second_name
        self.birth_date = birth_date
        string_ob = self.first_name + self.second_name + self.birth_date
        hash_object = hashlib.sha256(string_ob.encode())
        hex_dig = hash_object.hexdigest()
        self.hash = hex_dig
    def __iter__(self):
        return self
    def __next__(self):
        return self.first_name
    def __str__(self):
        return "huk"
    def __del__(self):
        pass


postac1 = Postac("oskar", "maciejewski", "12344")
postac2 = Postac("oskarek", "maciejewski", "12344")
postac3 = Postac("wladek", "maciejewski", "1234dd4")



numbers = [2, 2, 5]

#print(dir(numbers))
#numbers.__add__()
#print(numbers)
iterator1 = iter(numbers)
iterator2 = numbers.__iter__()

#print(next(iterator1), next(iterator2), next(iterator1), next(iterator2), next(iterator1), next(iterator2), next(iterator1), next(iterator2))

class Day():
    def __init__(self, visits, contacts):
        self.visits = visits
        self.contacts = contacts
    def __str__(self):
        return 'Visits: %i, Contacts: %i' % (self.visits, self.contacts)
    def __add__(self, other):
        total_visits = self.visits + other.visits
        total_contacts = self.contacts + other.contacts
        return Day(total_visits, total_contacts)
day1 = Day(10, 1)
day2 = Day(20, 2)

day3 = day2 + day1

print(day3)