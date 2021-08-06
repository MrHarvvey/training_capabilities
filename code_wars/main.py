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
    return int(str("".join(sorted([number for number in str(num)])))[::-1])


def open_or_senior(data):
    """To be a senior, a member must be at least 55 years old and have a handicap greater
     than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.
     print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])) """
    return ["Senior" if word[0] >= 55 and word[1] > 7 else "Open" for word in data]


def dna_strand(dna):
    """In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
     You have function with one side of the DNA (string, except for Haskell); you need to
      get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except
      for Haskell)."""
    dnas = ""
    for letter in dna:
        if letter == "T":
            dnas += "A"
        elif letter == "A":
            dnas += "T"
        elif letter == "C":
            dnas += "G"
        elif letter == "G":
            dnas += "C"
        else:
            dnas += letter
    return dnas


def dna_strand_trans(dna):
    """In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
     You have function with one side of the DNA (string, except for Haskell); you need to
      get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except
      for Haskell)."""
    return dna.translate(dna.maketrans("ATCG", "TAGC"))


def row_sum_odd_numbers(n):
    liczby = [liczba for liczba in range(n + 1)]
    suma_liczb = sum(liczby)
    list_number = [number for number in range(int(suma_liczb + 1)*2) if number % 2 == 1][:-1]
    return sum(list_number[-n:])


def row_sum_odd_numbers2(n):
    #your code here
    return n ** 3

