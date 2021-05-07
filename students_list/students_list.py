import os

list_of_students = ['Maciek', 'Oskar', 'Franek']


def print_list():
    for student in list_of_students:
        print(student)


def add_student():
    student = input("Wpisz studenta którego chcesz dodac")
    list_of_students.append(student)

def add_at_number():
    number = int(input("Wpisz numer na liście studenta"))
    student = input("Wpisz nazwę studenta ")
    if number > 0:
        list_of_students.insert((number - 1), student)
    else:
        print('Musisz wpisac liczbę większą od 0 ')


while True:
    print("\n1.Wyświetl liste studentów \n2.Dodaj Studenta na końcu listy \n3.Dodaj studenta w odpowiednim miejscu listy ")
    try:
        what_to_do = int(input("Enter choice:"))
    except ValueError:
        print("Sorry, i dont understand use only numbers")
        continue
    if what_to_do == 1:
        print_list()
    if what_to_do == 2:
        add_student()
        print("student dodany")
        print_list()
    if what_to_do == 3:
        add_at_number()
        print("student dodany")
        print_list()
