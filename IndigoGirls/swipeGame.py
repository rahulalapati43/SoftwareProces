def swipeGame(messageDictionary):
    outputDictionary = {}
    if "direction" not in messageDictionary.keys():
        outputDictionary["gameStatus"] = "error: missing direction"

    if (messageDictionary["direction"] != "up" or messageDictionary["direction"] != "down" or messageDictionary[
        "direction"] != "left" or messageDictionary["direction"] != "right"):
        outputDictionary["gameStatus"] = "error: invalid direction"

    return outputDictionary