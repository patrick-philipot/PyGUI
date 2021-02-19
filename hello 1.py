import sys

print (sys.version)
print( sys.executable)

print ("hello")

class affichable:
  pass

  def __init__(self, term, definition):
    self.term = term
    self.definition = definition

  def print_term(self):
    print(self.term)
  def print_definition(self):
    print(self.definition)


# card1 = affichable("A", "1ère lettre de l'alphabet")
# card1.print_term()
# card1.print_definition()
# print(chr(65))

deck = []

for i in range(65, 91):
  # print(chr(i))
  deck.append( affichable(chr(i), "{} ème lettre de l'alphabet".format(i-64)))

deck[12].print_term()
deck[12].print_definition()

print(chr(0x30ab))

d = deck[25]
d.print_term()
d.print_definition()
print(type(d))








