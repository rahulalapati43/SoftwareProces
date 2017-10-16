def swipeGame(messageDictionary):
    outputDictionary = {}
    if "direction" not in messageDictionary.keys():
        outputDictionary["gameStatus"] = "error: missing direction"

    elif (messageDictionary["direction"] != "up" and messageDictionary["direction"] != "down" and messageDictionary["direction"] != "left" and messageDictionary["direction"] != "right"):
        outputDictionary["gameStatus"] = "error: invalid direction"

    if "columnCount" not in messageDictionary["board"]:
        outputDictionary["gameStatus"] = "error: missing columnCount"

    elif (isinstance(messageDictionary["board"]["columnCount"], int) == False):
        outputDictionary["gameStatus"] = "error: columnCount is not an integer"

    elif (messageDictionary["board"]["columnCount"] <= 1 or messageDictionary["board"]["columnCount"] > 100):
        outputDictionary["gameStatus"] = "error: columnCount is out of bounds"

    if "rowCount" not in messageDictionary["board"]:
        outputDictionary["gameStatus"] = "error: missing rowCount"

    elif (isinstance(messageDictionary["board"]["rowCount"], int) == False):
        outputDictionary["gameStatus"] = "error: rowCount is not an integer"

    elif (messageDictionary["board"]["rowCount"] <= 1 or messageDictionary["board"]["rowCount"] > 100):
        outputDictionary["gameStatus"] = "error: rowCount is out of bounds"

    if ("rowCount" in messageDictionary["board"] and "columnCount" in messageDictionary["board"]):
        if (messageDictionary["board"]["rowCount"] > 1 and messageDictionary["board"]["rowCount"] <= 100):
            if (messageDictionary["board"]["columnCount"] > 1 and messageDictionary["board"]["columnCount"] <= 100):

                i = messageDictionary["board"]["rowCount"] * messageDictionary["board"]["columnCount"]

                j = len(messageDictionary["board"]["grid"])

                if (i != j):
                    outputDictionary["gameStatus"] = "error: invalid board"

    return outputDictionary