def swipeGame(messageDictionary):
    outputDictionary = {}
    if "direction" not in messageDictionary.keys():
        outputDictionary["gameStatus"] = "error: missing direction"

    elif (messageDictionary["direction"] != "up" and messageDictionary["direction"] != "down" and messageDictionary["direction"] != "left" and messageDictionary["direction"] != "right"):
        outputDictionary["gameStatus"] = "error: invalid direction"

    return outputDictionary