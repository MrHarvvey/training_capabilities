




def moja_lista(str, n):
    wynik = str[:n-1].__add__(str[n:])
    return wynik
print(moja_lista("kitten", 3))