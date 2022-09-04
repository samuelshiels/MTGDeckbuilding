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

def getDeckOracleIds(deck):
    deckObj= []
    i = 0
    for card in deck:
        response = r.runRest(
            'https://api.scryfall.com/cards/named',
            {
                'exact':card[0]
            },
            card[1],
            'cache/cards'
            )
        cardObj = (card[0],card[1],json.loads(response)['oracle_id'])
        deckObj.append(cardObj)
    return deckObj

def getVariations(deck):
    deckObj= getDeckOracleIds(deck)
    output = ''
    for card in deckObj:
        output = output + '\n'
        response = r.runRest(
            'https://api.scryfall.com/cards/search',
            {
                'q':'oracle_id=' + card[2],
                'unique':'prints'
            },
            card[2],
            'cache/search'
            )
        
        searchObj = json.loads(response)
        output = output + searchObj['data'][0]['name'] + '\n'
        print(searchObj['data'][0]['name'])
        frames = ''
        for data in searchObj['data']:
            if 'paper' in data['games']:
                frames = frames + '\t' + data['frame']
            if 'finishes' in data:
                if 'nonfoil' not in data['finishes']:
                    frames = frames + ' ' + str(data['finishes'])
            if data['border_color'] == 'borderless':
                frames = frames + ' borderless'
            if data['textless'] == True:
                frames = frames + ' textless'
            if data['full_art'] == True:
                frames = frames + ' full_art'
            frames = frames + ' ' + data['set_name']
        output = output + frames
        print(frames)    
    out_file='output'
    with open(out_file, 'x') as f:
        f.write(output)

config = {
    'output':'output_delver',
    'outputType':'MKMImport',
    'input':'decks/decklisttest',
    'inputType':'archideckt'
}
print(mtgDelver.execute(config))