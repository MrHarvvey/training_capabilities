import adding_database

name_database = "database_1.db"

emails_adresses = adding_database.connect(database_name=name_database).search_data(table='szkola', what_to_search='liam_ro')


print(emails_adresses)




