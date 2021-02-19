from random import shuffle
import PySimpleGUI as sg

class Card:
    """ flash card rceto/verso values """

    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def get_term(self):
        return self.term

    def get_definition(self):
        return self.definition

    def __str__(self):
        return "Class Card, with term = '{}' and definition = '{}'".format(self.term, self.definition)


class Deck:
    """ set of flash cards """

    def __init__(self, interest, title):
        self.data = []
        self.interest = interest
        self.title = title

    def add(self, card):
        """ add an Card to the deck array """
        self.data.append(card)

    def valueAtIndex(self, index):
        """ base 1 access to data elements """
        i = index - 1
        return self.data[i]
    
    def __str__(self):
        message = "Class Deck (of Flash Cards)\n"
        message += "{} elements\n".format(len(self.data))
        message += "Premier élément :{} \n".format(self.data[0].__str__())
        return message
    
    def cardsCount(self):
        return len( self.data)
    

# Testing Deck
# Create a Deck with 26 Cards
Deck1 = Deck("Alphabet", "Les 26 lettres de l'alphabet.")

for i in range(65, 91):
    Deck1.add(Card(chr(i), "{} ème lettre de l'alphabet".format(i-64)))
    
# Préparation du test
# index des cards connues
known = []
# index des cards non encore connues
# filling notKnown with all card indexes
notKnown = list( range(1, Deck1.cardsCount() +1 ))
# shuffle
shuffle(notKnown)

notFinished = True
index = 0

# liste des cards non connues après test
newUnknown = []

def readCard(index):
    cardIndex = notKnown[index]
    card = Deck1.valueAtIndex(cardIndex)
    # affiche term puis definition
    term = card.get_term()
    definition = card.get_definition()
    return (term, definition)

# pySimpleGUI
# theme
sg.theme('LightGrey2') 

# style
sty: dict = {'size':(40,1), 'font':('Franklin Gothic Book', 24)}
styb: dict = {'size':(20,2), 'font':('Franklin Gothic Book', 18)}

term, definition = readCard(index)

# window layout
layout = [
            [sg.Text("Flashcards : les lettres de l'alphabet", **sty)],
            [sg.Text(term, key='_TERM_', **sty) ],
            [sg.Text(definition, key='_DEFINITION_', **sty)],
            [sg.Sizer(0,50)],      
            [sg.Button('Je sais', key="OK", **styb), sg.Button('Je ne sais pas', key="NOTOK", **styb)],
            [sg.Button('STOP'), sg.CalendarButton('date')]
]

# The window
window = sg.Window('FlashCards with pySimpleGUI', layout, size=(600,300))

# STEP3 - the event loop
while True:
    event, values = window.read()   # Read the event that happened and the values dictionary
    print(event, values)
    if event in (None, 'Exit'):     # If user closeddow with X or if user clicked "Exit" button then exit
        break
    if event == 'OK':
      #print('Button OK')
      known.append(notKnown[index])

    if event == 'NOTOK':
      #print('Button NOTOK')
      newUnknown.append(notKnown[index])
      
    if event in ('OK', 'NOTOK'):
      index += 1
      term, definition = readCard(index)
      window['_TERM_'].update(term)
      window['_DEFINITION_'].update(definition)  
      
    if event == 'STOP':
      print('Button STOP')
      print("notKnown = {}".format(notKnown))
      print("known = {}".format(known))
      print("newUnknown = {}".format(newUnknown))


window.close()














def playWithDeck( D ):
    # index des cards connues
    known = []
    # index des cards non encore connues
    # filling notKnown with all card indexes
    notKnown = list( range(1, D.cardsCount() +1 ))
    # shuffle
    shuffle(notKnown)
    
    notFinished = True
    index = 0
    
    # liste des cards non connues après test
    newUnknown = []
    
    while notFinished:
        cardIndex = notKnown[index]
        card = D.valueAtIndex(cardIndex)
        # affiche term puis definition
        print(card.get_term())
        print(card.get_definition())
                
        answer = input("Espace pour connu, Q pour quitter, Toutes autres lettre pour pas connu, puis touche Entrée\n")
        if answer == 'q':
            notFinished = False
        elif answer == ' ':
            # card connue
            known.append(cardIndex)
        else:
            # card non connue
            newUnknown.append(cardIndex)
            
        index += 1
        print("index ? {}".format(index))
        
        if index == D.cardsCount():
            print("Toutes les cards ont été affichées.")
            notFinished = False
    
    print("notKnown = {}".format(notKnown))
    print("known = {}".format(known))
    print("newUnknown = {}".format(newUnknown))
    



