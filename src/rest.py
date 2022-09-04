import getRestData
import json
import LinuxHelper as lh
from RESTObject import RESTObject as ro

cache = lh.getHomeDirectory() + '/' + lh.getCacheDirectory() + 'MTGDelver/'

def runRest(e, p, o, c):
    global cache
    restObj = ro(operation='get', endpoint=e, params=p, headers={}, payload={})
    config = {}

    '''
    restObj['operation'] = 'get'
    restObj['endpoint'] = endpoint
    restObj['params'] = params
    restObj['headers'] = {}
    restObj['payload'] = {}
    '''

    config['output'] = o + '.json'
    config['cache'] = cache + c
    config['time'] = 21600
    config['sleep'] = 200
    config['rest'] = restObj
    return getRestData.execute(config)


def getOracleId(cardName):
    response = runRest(
        'https://api.scryfall.com/cards/named',
        {
            'exact': cardName
        },
        lh.encodeMD5(cardName),
        'cache/cards'
    )
    return json.loads(response)['oracle_id']

def getScryfallObj(cardName):
    response = runRest(
        'https://api.scryfall.com/cards/named',
        {
            'exact': cardName
        },
        lh.encodeMD5(cardName),
        'cache/cards'
    )
    lh.getCacheDirectory()
    return json.loads(response)