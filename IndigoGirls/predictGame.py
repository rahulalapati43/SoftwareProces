def predictGame(messageDictionary):
    outputDictionary = {}

    if "direction" not in messageDictionary.keys():
        outputDictionary["gameStatus"] = "error: missing direction"

    elif (messageDictionary["direction"].lower() != "up" and messageDictionary["direction"].lower() != "down" and
                  messageDictionary["direction"].lower() != "left" and messageDictionary["direction"].lower() != "right"):
        outputDictionary["gameStatus"] = "error: invalid direction"

    return outputDictionary


