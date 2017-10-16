def swipeGame(messageDictionary):
    outputDictionary = {}
    if "direction" not in messageDictionary.keys():
        outputDictionary["gameStatus"] = "error: missing direction"

    elif (messageDictionary["direction"] != "up" and messageDictionary["direction"] != "down" and messageDictionary["direction"] != "left" and messageDictionary["direction"] != "right"):
        outputDictionary["gameStatus"] = "error: invalid direction"

    if (isinstance(messageDictionary["board"]["rowCount"], int) == False):
        outputDictionary["gameStatus"] = "error: rowCount is not an integer"

    if (messageDictionary["board"]["rowCount"] <= 1 or messageDictionary["board"]["rowCount"] > 100):
        outputDictionary["gameStatus"] = "error: rowCount is out of bounds"

    return outputDictionary