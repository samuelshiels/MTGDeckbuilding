import copy
from card import Card as c
class Deck:

    _defaults = {
        "name":"",
        "cards":[]
    }

    def __init__(self, **kwargs):
        self.__dict__.update(self._defaults)
        self.__dict__.update(kwargs)
    
    '''
    
    
    '''
    def performAddRemove(self, addRemoveList):
        #
        for i in addRemoveList['remove']:
            #
            for card in self.cards:
                if card.name == i:
                    self.cards.remove(card)
                pass
            pass
        for i in addRemoveList['add']:
            self.cards.append(c(name = i, quantity = 1))
            pass
        return

    def print(self):
        returnValue = []
        returnValue.append(self.name)
        for c in self.cards:
            returnValue.append(c.print())
        return '\n'.join(returnValue)
    
    def printMKMImport(self):
        returnValue = []
        for c in self.cards:
            returnValue.append(c.printMKMImport())
        return '\n'.join(returnValue)
    
    def printVariantsHTML(self):
        header = "<head></head>"
        cards = []
        for c in self.cards:
            cards.append(copy.deepcopy(c.printVariantsHTML()))
        cardHTML = ''.join(cards)
        content = f'<table><caption>{self.name}</caption><tr><th>Name</th><th>Pics</th></tr>{cardHTML}</table>'
        body = f"<body>{content}</body>"
        returnValue = f"<html>{header}{body}</html>"
        return returnValue
    