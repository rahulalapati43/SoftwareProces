from IndigoGirls.swipeGame import swipeGame
from IndigoGirls.callSwipeGame import callSwipeGame
from random import *

def recommendGame(messageDictionary):

    outputDictionary = {}
    outputDictionary["gameStatus"] = "underway"

    outputDictionary = validateRecommend(messageDictionary, outputDictionary)

    if(outputDictionary["gameStatus"] == "underway"):

        inputDictionary = {}
        boardDictionary = {}


        if (messageDictionary["moves"] == 0):
            directionList = ["left", "right", "up", "down"]
            direction = sample(directionList,1)
            inputDictionary["op"] = "swipe"
            inputDictionary["direction"] = direction[0]
            boardDictionary["columnCount"] = messageDictionary["board"]["columnCount"]
            boardDictionary["rowCount"] = messageDictionary["board"]["rowCount"]
            boardDictionary["grid"] = messageDictionary["board"]["grid"]
            inputDictionary["board"] = boardDictionary
            outputDictionary = swipeGame(inputDictionary)

            while ((outputDictionary["gameStatus"] == "error: no tiles can be shifted") and (len(directionList) != 0) ):
                if (len(directionList) > 1):
                    directionList.remove(inputDictionary["direction"])
                    direction = sample(directionList, 1)
                    inputDictionary["direction"] = direction[0]
                    outputDictionary = swipeGame(inputDictionary)
                else:
                    inputDictionary["direction"] = directionList[0]
                    outputDictionary = swipeGame(inputDictionary)
                    directionList.remove(directionList[0])

        elif (messageDictionary["moves"] == 1):

            outputList = []
            boardDictionary["columnCount"] = messageDictionary["board"]["columnCount"]
            boardDictionary["rowCount"] = messageDictionary["board"]["rowCount"]
            boardDictionary["grid"] = messageDictionary["board"]["grid"]
            inputDictionary["board"] = boardDictionary
            inputDictionary["board"] = boardDictionary
            inputDictionary["score"] = 0
            inputDictionary["op"] = "recommend"
            leftDictionary,rightDictionary,upDictionary, downDictionary = callSwipeGame(inputDictionary)

            outputList.append(leftDictionary)
            outputList.append(rightDictionary)
            outputList.append(upDictionary)
            outputList.append(downDictionary)

            scoresList = []
            leftScore = 0
            rightScore = 0
            upScore = 0
            downScore = 0

            inputDictionary = outputList[0]
            if (inputDictionary["gameStatus"] == "underway"):
                scoresList.append(inputDictionary["score"])
                leftScore = inputDictionary["score"]

            inputDictionary = outputList[1]
            if (inputDictionary["gameStatus"] == "underway"):
                scoresList.append(inputDictionary["score"])
                rightScore = inputDictionary["score"]

            inputDictionary = outputList[2]
            if (inputDictionary["gameStatus"] == "underway"):
                scoresList.append(inputDictionary["score"])
                upScore = inputDictionary["score"]

            inputDictionary = outputList[3]
            if (inputDictionary["gameStatus"] == "underway"):
                scoresList.append(inputDictionary["score"])
                downScore = inputDictionary["score"]

            if (len(scoresList) != 0):
                directionList = []
                maxScore = max(scoresList)
                if (maxScore == leftScore):
                    directionList.append("left")

                if (maxScore == rightScore):
                    directionList.append("right")

                if (maxScore == upScore):
                    directionList.append("up")

                if (maxScore == downScore):
                    directionList.append("down")

                if (len(directionList) > 1):
                    direction = sample(directionList, 1)
                    inputDictionary["direction"] = direction[0]
                else:
                    inputDictionary["direction"] = directionList[0]

                boardDictionary["columnCount"] = messageDictionary["board"]["columnCount"]
                boardDictionary["rowCount"] = messageDictionary["board"]["rowCount"]
                boardDictionary["grid"] = messageDictionary["board"]["grid"]
                inputDictionary["board"] = boardDictionary
                inputDictionary["board"] = boardDictionary
                inputDictionary["op"] = "swipe"
                outputDictionary = swipeGame(inputDictionary)
            else:
                outputDictionary["gameStatus"] = "error: no tiles can be shifted on a subsequent swipe"


        elif (messageDictionary["moves"] > 1):

            outputList = []
            boardDictionary["columnCount"] = messageDictionary["board"]["columnCount"]
            boardDictionary["rowCount"] = messageDictionary["board"]["rowCount"]
            boardDictionary["grid"] = messageDictionary["board"]["grid"]
            inputDictionary["board"] = boardDictionary
            inputDictionary["board"] = boardDictionary
            inputDictionary["score"] = 0
            inputDictionary["op"] = "recommend"
            leftDictionary, rightDictionary, upDictionary, downDictionary = callSwipeGame(inputDictionary)

            outputList.append(leftDictionary)
            outputList.append(rightDictionary)
            outputList.append(upDictionary)
            outputList.append(downDictionary)

            start = 0
            noofElements = 0
            for move in range(1,messageDictionary["moves"]):
                noofElements = noofElements + ((2 ** move) ** 2)
                for element in range(start,noofElements):
                    inputDictionary = outputList[element]
                    inputDictionary = dict(inputDictionary)
                    if (inputDictionary["gameStatus"] != "error: no tiles can be shifted"):
                        inputDictionary["op"] = "recommend"
                    leftDictionary, rightDictionary, upDictionary, downDictionary = callSwipeGame(inputDictionary)
                    outputList.append(leftDictionary)
                    outputList.append(rightDictionary)
                    outputList.append(upDictionary)
                    outputList.append(downDictionary)
                start = noofElements

            leftScores = []
            rightScores = []
            upScores = []
            downScores = []

            start = 4
            for move in range(1,messageDictionary["moves"]):
                noofElements = (2 ** move) ** 2
                lower = start
                upper = (lower + noofElements)
                if (move == (messageDictionary["moves"] - 1)):
                    for element in range(lower,upper):
                        inputDictionary = outputList[element]
                        if (inputDictionary["gameStatus"] == "underway"):
                            leftScores.append(inputDictionary["score"])

                lower = upper
                upper = (lower + noofElements)
                if (move == (messageDictionary["moves"] - 1)):
                    for element in range(lower,upper):
                        inputDictionary = outputList[element]
                        if (inputDictionary["gameStatus"] == "underway"):
                            rightScores.append(inputDictionary["score"])

                lower = upper
                upper = (lower + noofElements)
                if (move == (messageDictionary["moves"] - 1)):
                    for element in range(lower,upper):
                        inputDictionary = outputList[element]
                        if (inputDictionary["gameStatus"] == "underway"):
                            upScores.append(inputDictionary["score"])

                lower = upper
                upper = (lower + noofElements)
                if (move == (messageDictionary["moves"] - 1)):
                    for element in range(lower,upper):
                        inputDictionary = outputList[element]
                        if (inputDictionary["gameStatus"] == "underway"):
                            downScores.append(inputDictionary["score"])

                start = upper

            if ((len(leftScores) == 0) and (len(rightScores) == 0) and (len(upScores) == 0) and (len(downScores) == 0) ):
                outputDictionary["gameStatus"] = "error: no tiles can be shifted on a subsequent swipe"
            else:
                scoresList = []
                leftScore = 0
                rightScore = 0
                upScore = 0
                downScore = 0
                if (len(leftScores) != 0):
                    leftScore = max(leftScores)
                    scoresList.append(leftScore)

                if (len(rightScores) != 0):
                    rightScore = max(rightScores)
                    scoresList.append(rightScore)

                if (len(upScores) != 0):
                    upScore = max(upScores)
                    scoresList.append(upScore)

                if (len(downScores) != 0):
                    downScore = max(downScores)
                    scoresList.append(downScore)

                if (len(scoresList) != 0):
                    directionList = []
                    maxScore = max(scoresList)
                    if (maxScore == leftScore):
                        directionList.append("left")

                    if (maxScore == rightScore):
                        directionList.append("right")

                    if (maxScore == upScore):
                        directionList.append("up")

                    if (maxScore == downScore):
                        directionList.append("down")

                    if (len(directionList) > 1):
                        direction = sample(directionList, 1)
                        inputDictionary["direction"] = direction[0]
                    else:
                        inputDictionary["direction"] = directionList[0]

                    boardDictionary["columnCount"] = messageDictionary["board"]["columnCount"]
                    boardDictionary["rowCount"] = messageDictionary["board"]["rowCount"]
                    boardDictionary["grid"] = messageDictionary["board"]["grid"]
                    inputDictionary["board"] = boardDictionary
                    inputDictionary["board"] = boardDictionary
                    inputDictionary["op"] = "swipe"
                    outputDictionary = swipeGame(inputDictionary)

    return outputDictionary


def validateRecommend(messageDictionary, outputDictionary):

    if "moves" not in messageDictionary.keys():
        messageDictionary["moves"] = 0

    elif (isinstance(messageDictionary["moves"], int) == False):
        outputDictionary["gameStatus"] = "error: invalid moves"

    elif (messageDictionary["moves"] < 0):
        outputDictionary["gameStatus"] = "error: moves must be GE 0"

    outputDictionary = validateBoard(messageDictionary, outputDictionary)

    return outputDictionary


def validateBoard(messageDictionary, outputDictionary):

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
            for index in range(0, gridLength):
                if (isinstance(messageDictionary["board"]["grid"][index], int) == False):
                    outputDictionary["gameStatus"] = "error: grid elements are not integers"

            if (outputDictionary["gameStatus"] != "error: grid elements are not integers"):
                for index in range(0, gridLength):
                    if (messageDictionary["board"]["grid"][index] < 0):
                        outputDictionary["gameStatus"] = "error: grid elements must be GE 0"

                if (outputDictionary["gameStatus"] != "error: grid elements must be GE 0"):
                    for index in range(0, gridLength):
                        if (messageDictionary["board"]["grid"][index] > rowcolumnProd):
                            outputDictionary["gameStatus"] = "error: grid elements must be LE grid Length"

                    if (outputDictionary["gameStatus"] != "error: grid elements must be LE grid Length"):
                        countGT0 = 0
                        for index in range(0, gridLength):
                            if (messageDictionary["board"]["grid"][index] > 0):
                                countGT0 = countGT0 + 1

                        if countGT0 < 2:
                            outputDictionary["gameStatus"] = "error: No fewer than 2 items can be GT 0"

    return outputDictionary