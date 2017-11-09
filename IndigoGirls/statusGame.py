
def statusGame(messageDictionary):

    outputDictionary = {}

    if "tile" not in messageDictionary.keys():
        messageDictionary["tile"] = 2048

    elif (messageDictionary["tile"] < 2):
        outputDictionary["gameStatus"] = "error: invalid tile value"

    if "board" not in messageDictionary.keys():
        outputDictionary["gameStatus"] = "error: missing board"

    return outputDictionary
