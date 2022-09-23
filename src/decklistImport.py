from turtle import position
from deck import Deck as d
from card import Card
import re
#read file

#parse entry

###
# Specialised Functions
###
def formatDeckX(deckArray):
    return list(map(formatX, deckArray))

def formatX(str):
    return convertType(str.split('x ',1))

def importArchideckt(rawArray):
    return combineDuplicates(formatDeckX(rawArray))

def importDelverDeck(rawArray = [], type='default'):
    if 'Quantity' in rawArray[0] and 'Name' in rawArray[0]:
        positions = rawArray[0].split(',')
        nameLoc = positions.index('Name')
        quantityLoc = positions.index('Quantity')
        rawArray.pop(0)
        deckArray = [splitCSV(p, nameLoc, quantityLoc) for p in rawArray]
        return combineDuplicates(deckArray)
    else:
        return []
    pass

def removeQuotes(array):
    return [int(array[0]), str(array[1])]

def splitCSV(str, n, q):
    if str[0] == '"':
        result = str[1:-1].split('","')
        return removeQuotes([result[q],result[n]])
    else:
        result = str.split(',')
        return [result[q], result[n]]
###

###
# General Functions
###
def createDeck(name, cards):
    return d(name=name, cards=cards)

def createCards(cards):
    returnArray = []
    for card in cards:
        returnArray.append(Card(name = card[1], quantity = card[0]))
    return returnArray

def importSimple(rawArray):
    return combineDuplicates(formatArray(rawArray))

def convertType(array):
    return [int(array[0]), str(array[1])]

def formatArray(rawArray):
    returnArray = list(map(formatLine, rawArray))
    #print(returnArray)
    return returnArray

def formatLine(line):
    #1 or more digits
    #followed by an optional 'x' character
    #a single mandatory space
    '''
    card name featuring, 
    capitals
    lowercase
    numbers
    forward slash
    question mark
    exclamation mark
    dash
    period
    comma
    '''
    # capture both number and card name
    regex = "([0-9]+)x?\s{1}([A-Za-z0-9\'.,/\-\!\?\s]+)"
    x = re.findall(regex, line)
    #print(x)
    if len(x[0]) == 2:
        return convertType(list(x[0]))
    return False

def combineDuplicates(deckArray):
    result = []
    for x in deckArray:
        found = False  
        for y in result:
            if x[1] == y[1]:
                found = True
                y[0] += x[0]
        if not found:
            result.append(x)
    #print(result)
    return result
###