#zalozenia
#monkey_trouble(True, True) → True
#monkey_trouble(False, False) → True
#monkey_trouble(True, False) → False

def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False

print(monkey_trouble(False, False))