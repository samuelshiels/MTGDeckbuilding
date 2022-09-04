import LinuxHelper as lh
import argparse
import decklistImport as dli

def init_argparse() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [FILE]...",
        description="<program_description"
    )

    parser.add_argument(
        "-v", "--version", action="version",
        version = f"{parser.prog} version 0.01"
    )

    parser.add_argument('-o','--output',nargs=1,default=False,
                    help='file to store result in - defaults to none and returns in std out')
    parser.add_argument('-i','--input',nargs=1,default=False,
                    help='file to input')
    parser.add_argument('-ot','--output_type',nargs=1,default=False,
                    help='Type of output data to format')
    parser.add_argument('-it','--input_type',nargs=1,default=False,
                    help='type of input you want to parse')
    args = parser.parse_args()
    return args

'''
004

'''
def output(config):
    returnValue = ''
    match config['outputType']:
        case 'VariantsHTML':
            returnValue = config['deck'].printVariantsHTML()
        case 'MKMImport':
            returnValue = config['deck'].printMKMImport()
        case _:
            returnValue = config['deck'].print()
    if config['output']:
        lh.overwriteFile(config['output'], returnValue)
    return returnValue
'''
003

'''
def createDeck(config):
    match config['inputType']:
        case 'archideckt':
            config['formattedDeck'] = dli.formatDeckX(config['fileData'])
            config['cards'] = dli.createCards(config['formattedDeck'])
            config['deck'] = dli.createDeck('test', config['cards'])
        case _:
            config['formattedDeck'] = dli.formatDeckX(config['fileData'])
            config['cards'] = dli.createCards(config['formattedDeck'])
            config['deck'] = dli.createDeck('test', config['cards'])
    return config

'''
002

'''
def loadDeck(config):
    config['fileData'] = lh.readFile(config['input'])
    return config

'''
001

'''
def __validateConfig(config):
    
    return config

'''


'''
def execute(config):
    config = __validateConfig(config)
    if not config:
        return False
    returnValue = False
    config = loadDeck(config)
    config = createDeck(config)
    returnValue = output(config)
    return returnValue

'''


'''
def main():
    args = vars(init_argparse())
    config = {
        'input':args['input'][0],
        'inputType':args['input_type'][0],
        'output':args['output'][0],
        'outputType':args['output_type'][0]
    }
    return execute(config)

if __name__ == "__main__":
    main()