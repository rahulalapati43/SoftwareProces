def predictGame(messageDictionary):
    outputDictionary = {}

    if "direction" not in messageDictionary.keys():
        outputDictionary["gameStatus"] = "error: missing direction"

    return outputDictionary


