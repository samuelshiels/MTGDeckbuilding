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
                    help='File name to store result in - if not provided will return the value as part of the command')
    parser.add_argument('-i','--input',nargs=1,default=False,
                    help='File name to input - can be a relative or absolute file path')
    parser.add_argument('-ot','--output_type',nargs=1,default=False,
                    help='Type of output data to format')
    parser.add_argument('-it','--input_type',nargs=1,default=False,
                    help='Type of input you want to parse')
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
        case 'delverDefault':
            config['formattedDeck'] = dli.importDelverDeck(config['fileData'], 'default')
            config['cards'] = dli.createCards(config['formattedDeck'])
            config['deck'] = dli.createDeck('test', config['cards'])
        case 'archideckt':
            config['formattedDeck'] = dli.importArchideckt(config['fileData'])
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
    config['fileData'] = [x for x in config['fileData'] if x]
    return config

'''
001

'''
def __validateConfig(config):
    if 'input' not in config or 'input' == '':
        return False
    if 'inputType' not in config:
        config['inputType'] = ''
    if 'outputType' not in config:
        config['outputType'] = ''
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