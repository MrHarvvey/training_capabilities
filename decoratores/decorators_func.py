


def tajne_oblicznenia():
    obliczenia = 2+2
    print(obliczenia)

def decorator_func(func):
    print(tajne_oblicznenia())
    def wrapper():
        print("start")
        print(type(func()))
        print("koniec")
    return wrapper

wykonaj_funkcje = decorator_func(tajne_oblicznenia())

print(wykonaj_funkcje)

#@mydecorator
def do_something():
    pass

print(type.__name__)

