import mtgDelver

config = {
    'output':'./output.txt',
    'outputType':'MKM',
    'input':'decks/DMUNeeded',
    'inputType':''
}
response = mtgDelver.execute(config)
print(response)