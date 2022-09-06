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
    return convertType(str.split('x ',1))

def importSimple(rawArray):
    pass

def importArchideckt(rawArray):
    return formatDeckX(rawArray)

def removeQuotes(array):
    zero = int(array[0][1:])
    one = str(array[1])
    return [zero, one]

def splitCSV(str):
    result = str.split('","')
    return removeQuotes([result[0],result[1]])

def importDelverDeck(rawArray = [], type='default'):
    if 'Quantity,Name,' in rawArray[0]:
        rawArray.pop(0)
        deckArray = list(map(splitCSV, rawArray))
        return deckArray
    else:
        return []
    pass