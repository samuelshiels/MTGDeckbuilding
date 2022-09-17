from turtle import position
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
    return makeUnique(formatDeckX(rawArray))

def importArchideckt(rawArray):
    return makeUnique(formatDeckX(rawArray))

def removeQuotes(array):
    zero = int(array[0])
    one = str(array[1])
    return [zero, one]

def splitCSV(str, n, q):
    result = str[1:-1].split('","')
    return removeQuotes([result[q],result[n]])

def makeUnique(deckArray):
    result = []
    done = set()
    for x in deckArray:
        if x[1] not in done:
            result.append(x)
            done.add(x[1])
    return result

def importDelverDeck(rawArray = [], type='default'):
    if 'Quantity' in rawArray[0] and 'Name' in rawArray[0]:
        positions = rawArray[0].split(',')
        nameLoc = positions.index('Name')
        quantityLoc = positions.index('Quantity')
        rawArray.pop(0)
        deckArray = [splitCSV(p, nameLoc, quantityLoc) for p in rawArray]
        return makeUnique(deckArray)
    else:
        return []
    pass