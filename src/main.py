import mtgDelver

config = {
    'output':'output.html',
    'outputType':'VariantsHTML',
    'input':'decks/kykar',
    'inputType':'start.txt',
    'addRemove':'decks/AddRemove.txt'
}
response = mtgDelver.execute(config)
print(response)