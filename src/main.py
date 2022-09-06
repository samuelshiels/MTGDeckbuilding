import csv
import json
import hashlib
import rest as r
import mtgDelver
def loadDelverDeck(deckName):
    line_array = []
    deck_file= f'./decks/{deckName}.csv'
    with open(deck_file, newline='') as f:
        reader = csv.reader(f)
        for line in reader:
            line_array.append(line)
    basics = ['plains','island','swamp','mountain','forest','wastes']
    # construct deck array
    deck = []
    for line in line_array:
        if line[0].lower() not in basics and line[0] != 'Name':
            result = hashlib.md5(line[0].encode())
            deck.append((line[0],result.hexdigest()))
    return deck
    pass

config = {
    'output':'output.txt',
    'outputType':'MKMImport',
    'input':'decks/Prossh.txt',
    'inputType':'delverDefault'
}
response = mtgDelver.execute(config)
print(response)