import hashlib

class Postac:
    def __init__(self, first_name, second_name, birth_date):
        self.first_name = first_name
        self.second_name = second_name
        self.birth_date = birth_date
        string_ob = self.first_name + self.second_name + self.birth_date
        hash_object = hashlib.sha256(string_ob.encode())
        hex_dig = hash_object.hexdigest()
        self.hash = hex_dig

    def __repr__(self):
        return '({}, {}, {}, {})'.format(self.first_name, self.second_name, self.birth_date, self.hash)


def sorting(persons):
    # sorting claas object by first_name
    sorteda = sorted(persons, key=lambda e: e.first_name)
    return sorteda

my_dick = {
  "data_list": [
    {"first_name": "Stefan", "second_name": "Nowak", "birth_date": "1988-06-18"},
    {"first_name": "Jan", "second_name": "Kowalski", "birth_date": "1977-11-10"}
  ]
}

list_of_person = []
data1 = my_dick['data_list']
for person in data1:
    person = Postac(person['first_name'], person['second_name'], person['birth_date'])
    list_of_person.append(person)

new_list = sorting(list_of_person)

sorted_list = []
for e in new_list:
    dick = {"first_name": e.first_name, "second_name": e.second_name, 'birth_date': e.birth_date, 'hash': e.hash}
    sorted_list.append(dick)
new_dick = {'result': sorted_list}
