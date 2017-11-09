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

        elif (messageDictionary["moves"] > 0):

            boardDictionary["columnCount"] = messageDictionary["board"]["columnCount"]
            boardDictionary["rowCount"] = messageDictionary["board"]["rowCount"]
            boardDictionary["grid"] = messageDictionary["board"]["grid"]
            inputDictionary["board"] = boardDictionary
            inputDictionary["board"] = boardDictionary
            outputDictionary["score"] = 0

            for move in range(0, messageDictionary["moves"]):
                scoreList = []
                directionList = []
                inputDictionary["direction"] = "left"
                leftDictionary = swipeGame(inputDictionary)
                print leftDictionary
                if (leftDictionary["gameStatus"] == "underway"):
                    scoreList.append(leftDictionary["score"] + outputDictionary["score"])

                inputDictionary["direction"] = "right"
                rightDictionary = swipeGame(inputDictionary)
                print rightDictionary
                if (rightDictionary["gameStatus"] == "underway"):
                    scoreList.append(rightDictionary["score"] + outputDictionary["score"])

                inputDictionary["direction"] = "up"
                upDictionary = swipeGame(inputDictionary)
                print upDictionary
                if (upDictionary["gameStatus"] == "underway"):
                    scoreList.append(upDictionary["score"] + outputDictionary["score"])

                inputDictionary["direction"] = "down"
                downDictionary = swipeGame(inputDictionary)
                print downDictionary
                if (downDictionary["gameStatus"] == "underway"):
                    scoreList.append(downDictionary["score"] + outputDictionary["score"])

                print scoreList
                if (len(scoreList) != 0):
                    maxScore = max(scoreList)
                    print maxScore

                if (leftDictionary["gameStatus"] == "underway"):
                    if (maxScore == leftDictionary["score"] + outputDictionary["score"]):
                        directionList.append("left")

                if (rightDictionary["gameStatus"] == "underway"):
                    if (maxScore == rightDictionary["score"] + outputDictionary["score"]):
                        directionList.append("right")
                if (upDictionary["gameStatus"] == "underway"):
                    if (maxScore == upDictionary["score"] + outputDictionary["score"]):
                        directionList.append("up")

                if (downDictionary["gameStatus"] == "underway"):
                    if (maxScore == downDictionary["score"] + outputDictionary["score"]):
                        directionList.append("down")

                print directionList
                if (len(directionList) != 0):
                    direction = sample(directionList, 1)
                    inputDictionary["direction"] = direction[0]
                    outputDictionary = swipeGame(inputDictionary)
                    outputDictionary["score"] = maxScore
                    inputDictionary["board"] = outputDictionary["board"]
                else:
                    outputDictionary = swipeGame(inputDictionary)
                    if (outputDictionary["gameStatus"] == "error: no tiles can be shifted"):
                        outputDictionary["gameStatus"] = outputDictionary["gameStatus"] + ' ' + "in" + ' ' + str(move + 1) + ' ' + "move"

                print inputDictionary
                print outputDictionary

    return outputDictionary