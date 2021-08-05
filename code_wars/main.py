# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def to_jaden_case(all_sentence):
    """function which capitalize every word in sentence"""
    my_new = all_sentence.split()
    new_list = [word.capitalize() for word in my_new]
    new_str = ' '.join(new_list)
    return new_str


def maskify(cc):
    """function which masks all letter except last 4"""
    if len(cc) < 3:
        return cc
    else:
        string_val = ""
        last_4 = cc[-4:]
        size_hash = len(cc[:-4])
        for number in range(size_hash):
            string_val += "#"
        string_val += last_4
    return string_val


def is_triangle(a, b, c):
    """Implement a method that accepts 3 integer values a, b, c.
     The method should return true if a triangle can be built
     with the sides of given length and false in any other case."""
    if all([a + b > c, b + c > a, c + a > b]):
        return False
    else:
        return True

def descending_order(num):
    # Bust a move right here
    return str(num)[::-1]