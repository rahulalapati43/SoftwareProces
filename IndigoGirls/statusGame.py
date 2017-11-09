
def statusGame(messageDictionary):

    outputDictionary = {}

    if "board" not in messageDictionary.keys():
        outputDictionary["gameStatus"] = "error: missing board"

    elif "columnCount" not in messageDictionary["board"].keys():
        outputDictionary["gameStatus"] = "error: missing columnCount"

    elif (isinstance(messageDictionary["board"]["columnCount"],int) == False):
        outputDictionary["gameStatus"] = "error: columnCount is not an integer"

    elif (messageDictionary["board"]["columnCount"] <= 1 or messageDictionary["board"]["columnCount"] > 100):
        outputDictionary["gameStatus"] = "error: columnCount is out of bounds"

    elif "rowCount" not in messageDictionary["board"].keys():
        outputDictionary["gameStatus"] = "error: missing rowCount"

    elif (isinstance(messageDictionary["board"]["rowCount"],int) == False):
        outputDictionary["gameStatus"] ="error: rowCount is not an integer"

    elif (messageDictionary["board"]["rowCount"] <= 1 or messageDictionary["board"]["rowCount"] > 100):
        outputDictionary["gameStatus"] = "error: rowCount is out of bounds"

    elif ("tile" not in messageDictionary.keys()):
        messageDictionary["tile"] = 2 ** round(messageDictionary["board"]["rowCount"] * messageDictionary["board"]["columnCount"] * 0.6875)

    elif (isinstance(messageDictionary["tile"],int) == False):
        outputDictionary["gameStatus"] = "error: tile is not an integer"

    elif (messageDictionary["tile"] < 2):
        outputDictionary["gameStatus"] = "error: invalid tile value"

    elif (messageDictionary["tile"] > 2 ** (messageDictionary["board"]["rowCount"] * messageDictionary["board"]["columnCount"])):
        outputDictionary["gameStatus"] = "error: invalid tile value"


    return outputDictionary
