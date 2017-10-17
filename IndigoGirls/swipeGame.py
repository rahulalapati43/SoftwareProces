import math
from random import *

def swipeGame(messageDictionary):
    outputDictionary = {}
    outputDictionary["gameStatus"] = "underway"

    if "direction" not in messageDictionary.keys():
        outputDictionary["gameStatus"] = "error: missing direction"

    elif (messageDictionary["direction"].lower() != "up" and messageDictionary["direction"].lower() != "down" and messageDictionary["direction"].lower() != "left" and messageDictionary["direction"].lower() != "right"):
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

                elif (i == j):
                    for index in range(0,i):
                        if (isinstance(messageDictionary["board"]["grid"][index], int) == False):
                            outputDictionary["gameStatus"] = "error: invalid grid elements"

                    if (outputDictionary["gameStatus"] != "error: invalid grid elements"):
                        for index in range(0, i):
                            if (messageDictionary["board"]["grid"][index] < 0):
                                outputDictionary["gameStatus"] = "error: Each item in the grid must be GE 0"

                    if (outputDictionary["gameStatus"] != "error: Each item in the grid must be GE 0"):
                        count = 0
                        for index in range(0, i):
                            if (messageDictionary["board"]["grid"][index] > 0):
                                count = count + 1
                        if count < 2:
                            outputDictionary["gameStatus"] = "error: No fewer than two items can be GT 0"

    if (outputDictionary["gameStatus"] == "underway"):

        x = len(messageDictionary["board"]["grid"])

        randomList = [1, 1, 1, 2]
        a = sample(randomList, 1)

        position = randint(0, x - 1)

        sumElements = 0

        score = 0

        boardDictionary = {}

        outList = []
        for y in range(0, x):
            outList.append(0)

        if (messageDictionary["direction"].lower() == "left"):

            inListIndex = 0

            for row in range(0, messageDictionary["board"]["rowCount"]):
                outListIndex = inListIndex
                previousElement = 0
                for column in range(0, messageDictionary["board"]["columnCount"]):
                    if (messageDictionary["board"]["grid"][inListIndex] != 0):
                        if (previousElement == 0):
                            previousElement = messageDictionary["board"]["grid"][inListIndex]
                        else:
                            if (previousElement == messageDictionary["board"]["grid"][inListIndex]):
                                power = messageDictionary["board"]["grid"][inListIndex]
                                sumElements = 2 * (2 ** power)
                                score = score + sumElements
                                outList[outListIndex] = int(math.log(sumElements, 2))
                                outListIndex = outListIndex + 1
                                previousElement = 0
                            else:
                                outList[outListIndex] = previousElement
                                outListIndex = outListIndex + 1
                                previousElement = messageDictionary["board"]["grid"][inListIndex]
                    inListIndex = inListIndex + 1
                if previousElement != 0:
                    outList[outListIndex] = previousElement

            compareResult = cmp(messageDictionary["board"]["grid"], outList)

            if (compareResult != 0):

                while (outList[position] != 0):
                    position = randint(0, x - 1)

                outList[position] = a[0]

                outputDictionary["score"] = score
                boardDictionary["columnCount"] = messageDictionary["board"]["columnCount"]
                boardDictionary["rowCount"] = messageDictionary["board"]["rowCount"]
                boardDictionary["grid"] = outList
                outputDictionary["board"] = boardDictionary
            elif (compareResult == 0):
                outputDictionary["gameStatus"] = "error: no tiles can be shifted"


        elif (messageDictionary["direction"].lower() == "right"):

            for row in range(1, messageDictionary["board"]["rowCount"] + 1):

                columnCount = messageDictionary["board"]["columnCount"]

                outListIndex = inListIndex = ((row * columnCount) - 1)

                previousElement = 0

                for column in range(0, messageDictionary["board"]["columnCount"]):

                    if (messageDictionary["board"]["grid"][inListIndex] != 0):

                        if (previousElement == 0):

                            previousElement = messageDictionary["board"]["grid"][inListIndex]

                        else:

                            if (previousElement == messageDictionary["board"]["grid"][inListIndex]):

                                power = messageDictionary["board"]["grid"][inListIndex]

                                sumElements = 2 * (2 ** power)

                                score = score + sumElements

                                outList[outListIndex] = int(math.log(sumElements, 2))

                                outListIndex = outListIndex - 1

                                previousElement = 0

                            else:

                                outList[outListIndex] = previousElement

                                outListIndex = outListIndex - 1

                                previousElement = messageDictionary["board"]["grid"][inListIndex]

                    inListIndex = inListIndex - 1

                if previousElement != 0:
                    outList[outListIndex] = previousElement

            compareResult = cmp(messageDictionary["board"]["grid"], outList)

            if (compareResult != 0):

                while (outList[position] != 0):
                    position = randint(0, x - 1)

                outList[position] = a[0]

                outputDictionary["score"] = score

                boardDictionary["columnCount"] = messageDictionary["board"]["columnCount"]

                boardDictionary["rowCount"] = messageDictionary["board"]["rowCount"]

                boardDictionary["grid"] = outList

                outputDictionary["board"] = boardDictionary

            elif (compareResult == 0):

                outputDictionary["gameStatus"] = "error: no tiles can be shifted"

        elif (messageDictionary["direction"].lower() == "up"):

            columnCount = messageDictionary["board"]["columnCount"]

            for column in range(1, columnCount + 1):

                outListIndex = inListIndex = column - 1
                previousElement = 0

                for row in range(0, messageDictionary["board"]["rowCount"]):
                    if (messageDictionary["board"]["grid"][inListIndex] != 0):
                        if (previousElement == 0):
                            previousElement = messageDictionary["board"]["grid"][inListIndex]
                        else:
                            if (previousElement == messageDictionary["board"]["grid"][inListIndex]):
                                power = messageDictionary["board"]["grid"][inListIndex]
                                sumElements = 2 * (2 ** power)
                                score = score + sumElements
                                outList[outListIndex] = int(math.log(sumElements, 2))
                                outListIndex = outListIndex + columnCount
                                previousElement = 0
                            else:
                                outList[outListIndex] = previousElement
                                outListIndex = outListIndex + columnCount
                                previousElement = messageDictionary["board"]["grid"][inListIndex]
                    inListIndex = inListIndex + columnCount
                if previousElement != 0:
                    outList[outListIndex] = previousElement

            compareResult = cmp(messageDictionary["board"]["grid"], outList)

            if (compareResult != 0):

                while (outList[position] != 0):
                    position = randint(0, x - 1)

                outList[position] = a[0]

                outputDictionary["score"] = score
                boardDictionary["columnCount"] = messageDictionary["board"]["columnCount"]
                boardDictionary["rowCount"] = messageDictionary["board"]["rowCount"]
                boardDictionary["grid"] = outList
                outputDictionary["board"] = boardDictionary
            elif (compareResult == 0):
                outputDictionary["gameStatus"] = "error: no tiles can be shifted"

        elif (messageDictionary["direction"].lower() == "down"):

            columnCount = messageDictionary["board"]["columnCount"]
            rowCount = messageDictionary["board"]["rowCount"]

            length = (len(messageDictionary["board"]["grid"]) - 1)

            for column in range(0, columnCount):

                outListIndex = inListIndex = length
                previousElement = 0

                for row in range(0, rowCount):
                    if (messageDictionary["board"]["grid"][inListIndex] != 0):
                        if (previousElement == 0):
                            previousElement = messageDictionary["board"]["grid"][inListIndex]
                        else:
                            if (previousElement == messageDictionary["board"]["grid"][inListIndex]):
                                power = messageDictionary["board"]["grid"][inListIndex]
                                sumElements = 2 * (2 ** power)
                                score = score + sumElements
                                outList[outListIndex] = int(math.log(sumElements, 2))
                                outListIndex = outListIndex - columnCount
                                previousElement = 0
                            else:
                                outList[outListIndex] = previousElement
                                outListIndex = outListIndex - columnCount
                                previousElement = messageDictionary["board"]["grid"][inListIndex]
                    inListIndex = inListIndex - columnCount
                if previousElement != 0:
                    outList[outListIndex] = previousElement
                length = length - 1

            compareResult = cmp(messageDictionary["board"]["grid"], outList)

            if (compareResult != 0):

                while (outList[position] != 0):
                    position = randint(0, x - 1)

                outList[position] = a[0]

                outputDictionary["score"] = score
                boardDictionary["columnCount"] = messageDictionary["board"]["columnCount"]
                boardDictionary["rowCount"] = messageDictionary["board"]["rowCount"]
                boardDictionary["grid"] = outList
                outputDictionary["board"] = boardDictionary
            elif (compareResult == 0):
                outputDictionary["gameStatus"] = "error: no tiles can be shifted"

    return outputDictionary