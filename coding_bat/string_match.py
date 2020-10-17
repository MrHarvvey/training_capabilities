

def string_match(a, b):
    count = 0
    for i in range(len(a)):
        zmienna1 = a[i:(i+2)]
        print(zmienna1)
        zmienna2 = b[i:(i+2)]
        print(zmienna2)
        if len(zmienna1) <= 1:
            count = count
        elif zmienna1 == zmienna2:
            count += 1
            print(count)
    return count

string_match('abc', 'axc')






