import math
from IndigoGirls.swipeGame import swipeGame

def statusGame(messageDictionary):
    """
                     statusGame is a function and is invoked in dispatch when the operation to be performed is status of
                     the grid based on the winning tile.
                :param messageDictionary: Is a dictionary which consists the following name value pairs: operation (op), tile,
                                         board dictionary which consists of row count (rowCount), column count (columnCount) and grid.
                                         All the params are mandatory.
                :return:                 A dictionary which consists of the following name value pairs: game status.
                """

    #output dictionary is returned to dispatch after the gameStatus is determined
    outputDictionary = {}
    outputDictionary["gameStatus"] = "underway"

    #call to validateStatus method to validate the status input dictionary
    outputDictionary = validateStatus(messageDictionary, outputDictionary)

    #if all the elements of the status input dictionary are validated
    if (outputDictionary["gameStatus"] == "underway"):
        #to check if any of the grid element matches the winning tile
        rowcolCountprod = messageDictionary["board"]["rowCount"] * messageDictionary["board"]["columnCount"]
        winningTile = int(math.log(messageDictionary["tile"], 2))
        for index in range(0,rowcolCountprod):
            if (messageDictionary["board"]["grid"][index]  >= winningTile):
                outputDictionary["gameStatus"] = "win"

        #if any of the grid element's value doesn't meet the winning tile's value
        if (outputDictionary["gameStatus"] != "win"):
            inputDictionary = {}
            boardDictionary = {}

            #logic to swipe the grid in all the possible directions
            boardDictionary["columnCount"] = messageDictionary["board"]["columnCount"]
            boardDictionary["rowCount"] = messageDictionary["board"]["rowCount"]
            boardDictionary["grid"] = messageDictionary["board"]["grid"]
            inputDictionary["board"] = boardDictionary
            inputDictionary["op"] = "status"

            inputDictionary["direction"] = "left"
            leftDictionary = swipeGame(inputDictionary)

            inputDictionary["direction"] = "right"
            rightDictionary = swipeGame(inputDictionary)

            inputDictionary["direction"] = "up"
            upDictionary = swipeGame(inputDictionary)

            inputDictionary["direction"] = "down"
            downDictionary = swipeGame(inputDictionary)

            #if the grid element doesn't match winning tile and the grid cannot be swiped in any possible direction
            if ((leftDictionary["gameStatus"] == "error: no tiles can be shifted") and (rightDictionary["gameStatus"] == "error: no tiles can be shifted") and
                    (upDictionary["gameStatus"] == "error: no tiles can be shifted") and (downDictionary["gameStatus"] == "error: no tiles can be shifted")):
                outputDictionary["gameStatus"] = "lose"

            else:
                outputDictionary["gameStatus"] = "underway"


    return outputDictionary


#method to validate status input dictionary
def validateStatus(messageDictionary, outputDictionary):

    outputDictionary = validateBoard(messageDictionary, outputDictionary)

    if (outputDictionary["gameStatus"] == "underway"):
        if ("tile" not in messageDictionary.keys()):
            messageDictionary["tile"] = 2 ** round(
            messageDictionary["board"]["rowCount"] * messageDictionary["board"]["columnCount"] * 0.6875)

        elif (isinstance(messageDictionary["tile"], int) == False):
            outputDictionary["gameStatus"] = "error: tile is not an integer"

        elif (messageDictionary["tile"] < 2):
            outputDictionary["gameStatus"] = "error: invalid tile value"

        elif (messageDictionary["tile"] > 2 ** (
                messageDictionary["board"]["rowCount"] * messageDictionary["board"]["columnCount"])):
            outputDictionary["gameStatus"] = "error: invalid tile value"

    return outputDictionary

#method to validate board in status input dictionary
def validateBoard(messageDictionary, outputDictionary):

    if "board" not in messageDictionary.keys():
        outputDictionary["gameStatus"] = "error: missing board"

    elif "columnCount" not in messageDictionary["board"].keys():
        outputDictionary["gameStatus"] = "error: missing columnCount"

    elif (isinstance(messageDictionary["board"]["columnCount"], int) == False):
        outputDictionary["gameStatus"] = "error: columnCount is not an integer"

    elif (messageDictionary["board"]["columnCount"] <= 1 or messageDictionary["board"]["columnCount"] > 100):
        outputDictionary["gameStatus"] = "error: columnCount is out of bounds"

    elif "rowCount" not in messageDictionary["board"].keys():
        outputDictionary["gameStatus"] = "error: missing rowCount"

    elif (isinstance(messageDictionary["board"]["rowCount"], int) == False):
        outputDictionary["gameStatus"] = "error: rowCount is not an integer"

    elif (messageDictionary["board"]["rowCount"] <= 1 or messageDictionary["board"]["rowCount"] > 100):
        outputDictionary["gameStatus"] = "error: rowCount is out of bounds"

    elif ("grid" not in messageDictionary["board"].keys()):
        outputDictionary["gameStatus"] = "error: missing grid"

    elif ("grid" in messageDictionary["board"].keys()):
        rowcolCountprod = (messageDictionary["board"]["rowCount"] * messageDictionary["board"]["columnCount"])
        gridLength = len(messageDictionary["board"]["grid"])
        if (rowcolCountprod != gridLength):
            outputDictionary["gameStatus"] = "error: invalid grid length"

        elif (rowcolCountprod == gridLength):
            for index in range(0, rowcolCountprod):
                if (isinstance(messageDictionary["board"]["grid"][index], int) == False):
                    outputDictionary["gameStatus"] = "error: invalid grid Elements"

            if (outputDictionary["gameStatus"] != "error: invalid grid elements"):
                for index in range(0, rowcolCountprod):
                    if (messageDictionary["board"]["grid"][index] < 0):
                        outputDictionary["gameStatus"] = "error: grid Elements must be GE 0"

            if (outputDictionary["gameStatus"] != "error: grid Elements must be GE 0"):
                countGT0 = 0
                for index in range(0, rowcolCountprod):
                    if (messageDictionary["board"]["grid"][index] > 0):
                        countGT0 = countGT0 + 1

                if countGT0 < 2:
                    outputDictionary["gameStatus"] = "error: No fewer than two items can be GT 0"

    return outputDictionary