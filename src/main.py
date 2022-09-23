import mtgDelver

config = {
    'output':'output.html',
    'outputType':'VariantsHTML',
    'input':'decks/Kestia.txt',
    'inputType':''
}
response = mtgDelver.execute(config)
print(response)