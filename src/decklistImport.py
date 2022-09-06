from deck import Deck as d
from card import Card

#read file

#parse entry
def createDeck(name, cards):
    return d(name=name, cards=cards)

def createCards(cards):
    returnArray = []
    for card in cards:
        returnArray.append(Card(name = card[1], quantity = card[0]))
    return returnArray

def formatDeckX(deckArray):
    return list(map(formatX, deckArray))

def convertType(array):
    return [int(array[0]), str(array[1])]

def formatX(str):
    return convertType(str.split('x ',2))

def importSimple():
    pass

def importArchideckt():
    #split 'x\s'
    pass

def importDelverDeck():
    pass