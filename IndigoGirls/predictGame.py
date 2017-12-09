from IndigoGirls.swipeGame import swipeGame

def predictGame(messageDictionary):

    outputDictionary = {}
    outputDictionary["gameStatus"] = "underway"

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

    elif ((messageDictionary["board"]["columnCount"] <= 1) or (messageDictionary["board"]["columnCount"] > 100)):
        outputDictionary["gameStatus"] = "error: columnCount is out of bounds"

    elif "rowCount" not in messageDictionary["board"]:
        outputDictionary["gameStatus"] = "error: missing rowCount"

    elif (isinstance(messageDictionary["board"]["rowCount"],int) == False):
        outputDictionary["gameStatus"] = "error: rowCount is not an integer"

    elif ((messageDictionary["board"]["rowCount"] <= 1) or (messageDictionary["board"]["rowCount"] > 100)):
        outputDictionary["gameStatus"] = "error: rowCount is out of bounds"

    elif "grid" not in messageDictionary["board"]:
        outputDictionary["gameStatus"] = "error: missing grid"

    elif (len(messageDictionary["board"]["grid"]) != (messageDictionary["board"]["columnCount"] * messageDictionary["board"]["rowCount"])):
        outputDictionary["gameStatus"] = "error: invalid grid length"

    elif (len(messageDictionary["board"]["grid"]) == (messageDictionary["board"]["columnCount"] * messageDictionary["board"]["rowCount"])):
        for index in range(0, len(messageDictionary["board"]["grid"])):
            if (isinstance(messageDictionary["board"]["grid"][index],int) == False):
                outputDictionary["gameStatus"] = "error: invalid grid elements"

        if (outputDictionary["gameStatus"] != "error: invalid grid elements"):
            for index in range(0, len(messageDictionary["board"]["grid"])):
                if (messageDictionary["board"]["grid"][index] < 0):
                    outputDictionary["gameStatus"] = "error: grid elements must be GE 0"

            if (outputDictionary["gameStatus"] != "error: grid elements must be GE 0"):
                for index in range(0, len(messageDictionary["board"]["grid"])):
                    if (messageDictionary["board"]["grid"][index] > (messageDictionary["board"]["columnCount"] * messageDictionary["board"]["rowCount"])):
                        outputDictionary["gameStatus"] = "error: grid elements must be LE gridLength"

                if (outputDictionary["gameStatus"] != "error: grid elements must be LE gridLength"):
                    countGT0 = 0
                    for index in range(0, len(messageDictionary["board"]["grid"])):
                        if (messageDictionary["board"]["grid"][index] > 0):
                            countGT0 = countGT0 + 1

                    if (countGT0 < 2):
                        outputDictionary["gameStatus"] = "error: No fewer than 2 grid elements must be GT 0"

    if (outputDictionary["gameStatus"] == "underway"):

        inputDictionary = {}
        resultDictionary = {}
        predictDictionary = {}

        if (messageDictionary["moves"] == 1):
            resultDictionary = swipeGame(messageDictionary)
            predictDictionary["highScore"] = resultDictionary["score"]
            predictDictionary["lowScore"] = resultDictionary["score"]
            predictDictionary["averageScore"] = resultDictionary["score"]
            outputDictionary["prediction"] = predictDictionary
            outputDictionary["gameStatus"] = "underway"

    return outputDictionary


