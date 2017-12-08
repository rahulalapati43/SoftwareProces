def predictGame(messageDictionary):
    outputDictionary = {}

    if "direction" not in messageDictionary.keys():
        outputDictionary["gameStatus"] = "error: missing direction"

    elif (messageDictionary["direction"].lower() != "up" and messageDictionary["direction"].lower() != "down" and
                  messageDictionary["direction"].lower() != "left" and messageDictionary["direction"].lower() != "right"):
        outputDictionary["gameStatus"] = "error: invalid direction"

    elif "moves" not in messageDictionary.keys():
        messageDictionary["moves"] = 1

    elif (isinstance(messageDictionary["moves"],int) == False):
        outputDictionary["gameStatus"] = "error: invalid moves"

    elif (messageDictionary["moves"] < 1):
        outputDictionary["gameStatus"] = "error: moves must be GE 1"

    elif "board" not in messageDictionary.keys():
        outputDictionary["gameStatus"] = "error: missing board"

    elif "columnCount" not in messageDictionary["board"]:
        outputDictionary["gameStatus"] = "error: missing columnCount"

    elif (isinstance(messageDictionary["board"]["columnCount"],int) == False):
        outputDictionary["gameStatus"] = "error: columnCount is not an integer"

    elif (messageDictionary["board"]["columnCount"] <= 1):
        outputDictionary["gameStatus"] = "error: columnCount is out of bounds"

    return outputDictionary


