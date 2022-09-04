import LinuxHelper as lh
import rest

class Card:

    _defaults = {
        "name":"",
        "oracleId":"",
        "quantity":0,
        "scryfallObj":{},
        "md5":""
    }

    def __init__(self, **kwargs):
        self.__dict__.update(self._defaults)
        self.__dict__.update(kwargs)
        self.md5 = lh.encodeMD5(self.name)
        self.oracleId = rest.getOracleId(self.name)
        self.scryfallObj = rest.getScryfallObj(self.name)

    def print(self):
        return f'{self.name} - {self.oracleId}'

    def printMKMImport(self):
        return f'{self.quantity} {self.name}'
    