import csv
import json
import hashlib
import rest as r
import mtgDelver

config = {
    'output':'output.txt',
    'outputType':'MKMImport',
    'input':'decks/Prossh.txt',
    'inputType':'delverDefault'
}
response = mtgDelver.execute(config)
print(response)