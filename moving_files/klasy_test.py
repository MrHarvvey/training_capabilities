#######test i nauka klas, najlepszy portal ever https://pl.python.org/docs/tut/node11.html#SECTION0011310000000000000000

x = "przykład"
class MojaKlasa:
   "Prosta, przykładowa klasa"
   i = 12345
   def f(x):
      return 'witaj świecie'
print(MojaKlasa.f(x))
print(MojaKlasa._+3_doc__)
def kurde_instrukcja(jak_uzyc):
   "musiisz podac 3 paramerty"
   return False
    h = g

print(__name__)
print(kurde_instrukcja.__doc__)


class Zespolona:
   def __init__(self, rzeczywista, urojona):
      self.r = rzeczywista
      self.i = urojona


x = Zespolona(12, 45)

x.licznik = 1

while x.licznik < 10:
    x.licznik = x.licznik * 2
print(x.f())



#Funkcja zdefiniowana poza obrębem klasy
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    def g(self):
        return 'witaj świecie'