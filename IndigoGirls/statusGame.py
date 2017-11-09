
def statusGame(messageDictionary):

    outputDictionary = {}

    if "tile" not in messageDictionary.keys():
        messageDictionary["tile"] = 2048

    elif (messageDictionary["tile"] < 2):
        outputDictionary["gameStatus"] = "error: invalid tile value"

    return outputDictionary
