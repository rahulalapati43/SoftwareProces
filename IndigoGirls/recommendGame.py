from IndigoGirls.swipeGame import swipeGame
from random import *

def recommendGame(messageDictionary):

    outputDictionary = {}
    outputDictionary["gameStatus"] = "underway"

    if "moves" not in messageDictionary.keys():
        messageDictionary["moves"] = 0

    elif (isinstance(messageDictionary["moves"], int) == False):
        outputDictionary["gameStatus"] = "error: invalid moves"

    elif (messageDictionary["moves"] < 0):
        outputDictionary["gameStatus"] = "error: moves must be GE 0"

    if "board" not in messageDictionary.keys():
        outputDictionary["gameStatus"] = "error: missing board"

    elif "columnCount" not in messageDictionary["board"]:
        outputDictionary["gameStatus"] = "error: missing columnCount"

    elif (isinstance(messageDictionary["board"]["columnCount"], int) == False):
        outputDictionary["gameStatus"] = "error: columnCount is not an integer"

    elif ((messageDictionary["board"]["columnCount"] <= 1) or (messageDictionary["board"]["columnCount"] > 100)):
        outputDictionary["gameStatus"] = "error: columnCount is out of bounds"

    elif "rowCount" not in messageDictionary["board"]:
        outputDictionary["gameStatus"] = "error: missing rowCount"

    elif (isinstance(messageDictionary["board"]["rowCount"], int) == False):
        outputDictionary["gameStatus"] = "error: rowCount is not an integer"

    elif ((messageDictionary["board"]["rowCount"] <= 1) or (messageDictionary["board"]["rowCount"] > 100)):
        outputDictionary["gameStatus"] = "error: rowCount is out of bounds"

    elif "grid" not in messageDictionary["board"]:
        outputDictionary["gameStatus"] = "error: missing grid"

    elif "grid" in messageDictionary["board"]:
        rowcolumnProd = messageDictionary["board"]["rowCount"] * messageDictionary["board"]["columnCount"]
        gridLength = len(messageDictionary["board"]["grid"])

        if (rowcolumnProd != gridLength):
            outputDictionary["gameStatus"] = "error: invalid grid length"

        elif (rowcolumnProd == gridLength):
            for index in range(0,gridLength):
                if(isinstance(messageDictionary["board"]["grid"][index], int) == False):
                    outputDictionary["gameStatus"] = "error: grid elements are not integers"

            if (outputDictionary["gameStatus"] != "error: grid elements are not integers"):
                for index in range(0,gridLength):
                    if(messageDictionary["board"]["grid"][index] < 0):
                        outputDictionary["gameStatus"] = "error: grid elements must be GE 0"

                if (outputDictionary["gameStatus"] != "error: grid elements must be GE 0"):
                    upperBound = 2 ** rowcolumnProd
                    for index in range(0,gridLength):
                        if (messageDictionary["board"]["grid"][index] > upperBound):
                            outputDictionary["gameStatus"] = "error: grid elements must be LE 2 ** grid Length"

                    if (outputDictionary["gameStatus"] != "error: grid elements must be LE 2 ** grid Length"):
                        countGT0 = 0
                        for index in range(0, gridLength):
                            if (messageDictionary["board"]["grid"][index] > 0):
                                countGT0 = countGT0 + 1

                        if countGT0 < 2:
                            outputDictionary["gameStatus"] = "error: No fewer than 2 items can be GT 0"

    if(outputDictionary["gameStatus"] == "underway"):

        inputDictionary = {}
        boardDictionary = {}


        if (messageDictionary["moves"] == 0):
            directionList = ["left", "right", "up", "down"]
            direction = sample(directionList,1)
            inputDictionary["direction"] = direction[0]
            boardDictionary["columnCount"] = messageDictionary["board"]["columnCount"]
            boardDictionary["rowCount"] = messageDictionary["board"]["rowCount"]
            boardDictionary["grid"] = messageDictionary["board"]["grid"]
            inputDictionary["board"] = boardDictionary
            outputDictionary = swipeGame(inputDictionary)



    return outputDictionary