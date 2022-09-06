import LinuxHelper as lh
import rest
import copy

class Card:

    _defaults = {
        "name":"",
        "oracleId":"",
        "quantity":0,
        "scryfallObj":{},
        "md5":"",
        "variations":[],
        "cache": lh.getHomeDirectory() + '/' + lh.getCacheDirectory() + 'MTGDelver/'
    }

    def __init__(self, **kwargs):
        self.__dict__.update(self._defaults)
        self.__dict__.update(kwargs)
        self.md5 = lh.encodeMD5(self.name)
        self.oracleId = rest.getOracleId(self.name)
        self.scryfallObj = rest.getScryfallObj(self.name)
        self.getVariations()

    def getVariations(self):
        cache = self.cache + 'cache/images'
        self.variationsObj = rest.getVariations(self.oracleId)['data']
        variations = []
        for item in self.variationsObj:
            variationObj = {
                'border':'',
                'foil':'',
                'location':cache,
            }
            if 'image_uris' not in item:
                variationObj['fileName'] = item['card_faces'][0]['image_uris']['normal'].split('/')[-1]
                variationObj['imageUri'] = item['card_faces'][0]['image_uris']['normal']
                pass
            else:
                variationObj['fileName'] = item['image_uris']['normal'].split('/')[-1]
                variationObj['imageUri'] = item['image_uris']['normal']
                pass
            if 'purchase_uris' in item:
                variationObj['uri'] = item['purchase_uris']['cardmarket']
            else:
                variationObj['uri'] = '404'
            #print(variationObj['location'])
            #print(variationObj['fileName'])
            lh.retrieveFile(variationObj['imageUri'],variationObj['location'],variationObj['fileName'],10000)
            variations.append(variationObj)
        self.variations = copy.deepcopy(variations)
        pass

    def print(self):
        return f'{self.name} - {self.oracleId}'

    def printMKMImport(self):
        return f'{self.quantity} {self.name}'

    def printVariationsHTML(self):
        returnValue = ''
        for e in self.variations:
            returnValue = f'{returnValue}<td><a href="{e["uri"]}"><img src="{"file://" + e["location"]+"/" + e["fileName"].replace("?","%3F")}"></a></td>'
        return returnValue

    def printVariantsHTML(self):
        variants = self.printVariationsHTML()
        returnValue = f'<tr><td>{self.name}</td>{copy.deepcopy(variants)}</tr>'
        return returnValue
    