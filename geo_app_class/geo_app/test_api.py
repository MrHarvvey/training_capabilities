


def is_value(value):
    return bool(value)




_is_value = False
required = False


def czy_zwracac(string):
    if not _is_value:
        if required:
            return string
    return "to nie jest wartosc"

print(czy_zwracac(""))

