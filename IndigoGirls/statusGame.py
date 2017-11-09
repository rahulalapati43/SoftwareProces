
def statusGame(messageDictionary):

    outputDictionary = {}

    if "tile" not in messageDictionary.keys():
        messageDictionary["tile"] = 2048

    return outputDictionary
