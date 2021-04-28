

oskar = lambda x: x if x <34 else 0

print(oskar(1500))

n = [2,3,3]
w = (2,3,3)

print(iter(n))

def square(*rozbierajsie):
    for arg in rozbierajsie:
        for arg2 in arg:
            print(arg2)
    return sum(*rozbierajsie)

print(square((1,2,3,4)))


# wygeneruj liczby parzyste od 2 do 10
lista = [2, 11, 2]

print(range(*lista))

def rodzina(*args, **kwargs):
    for arg in args:
        print("naziwska to:" + arg)
    for args, item in kwargs.items():
        print(args ,item)


rodzina("kowalscy", a=2, b=2 )

items = [{'product': {'id': 3, 'name': 'Karton szary 200x30x20 cm', 'price': '43.00', 'imageURL': '/images/Screenshot_2021-04-24_Rower_Magnetyczny_Stacjonarny_z_pulsem_fitness.png'}, 'quantity': 4, 'get_total': '172.00'}]

for item in items:
    print(item.product.name)

