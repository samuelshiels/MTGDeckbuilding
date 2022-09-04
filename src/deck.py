class Deck:

    _defaults = {
        "name":"",
        "cards":[]
    }

    def __init__(self, **kwargs):
        self.__dict__.update(self._defaults)
        self.__dict__.update(kwargs)
    
    def print(self):
        returnValue = []
        returnValue.append(self.name)
        for c in self.cards:
            returnValue.append(c.print())
        return '\n'.join(returnValue)
    
    def printMKMImport(self):
        returnValue = []
        for c in self.cards:
            returnValue.append(c.printMKMImport())
        return '\n'.join(returnValue)
    