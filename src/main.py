import csv
import json
import hashlib
import rest as r
import mtgDelver

config = {
    'output':'output.html',
    'outputType':'VariantsHTML',
    'input':'decks/Ardenn.txt',
    'inputType':'archideckt'
}
response = mtgDelver.execute(config)
print(response)