import math
def swipeGame(messageDictionary):
    outputDictionary = {}
    outputDictionary["gameStatus"] = "underway"
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

        sumElements = 0

        boardDictionary = {}

        outList = []
        for y in range(0, x):
            outList.append(0)

        if (messageDictionary["direction"] == "left"):

            inListIndex = outListIndex = 0
            previousElement = 0

            for row in range(0, messageDictionary["board"]["rowCount"]):
                outListIndex = inListIndex
                previousElement = 0
                for column in range(0, messageDictionary["board"]["columnCount"]):
                    print messageDictionary["board"]["grid"][inListIndex]
                    if (messageDictionary["board"]["grid"][inListIndex] != 0):
                        if (previousElement == 0):
                            previousElement = messageDictionary["board"]["grid"][inListIndex]
                            print previousElement
                        else:
                            if (previousElement == messageDictionary["board"]["grid"][inListIndex]):
                                power = messageDictionary["board"]["grid"][inListIndex]
                                sumElements = 2 * (2 ** power)
                                outList[outListIndex] = int(math.log(sumElements, 2))
                                outListIndex = outListIndex + 1
                                previousElement = 0
                            else:
                                outList[outListIndex] = previousElement
                                print outList[outListIndex]
                                outListIndex = outListIndex + 1
                                previousElement = messageDictionary["board"]["grid"][inListIndex]
                    inListIndex = inListIndex + 1
                if previousElement != 0:
                    print previousElement
                    outList[outListIndex] = previousElement

            compareResult = cmp(messageDictionary["board"]["grid"], outList)

            if (compareResult != 0):
                outputDictionary["score"] = sumElements
                boardDictionary["columnCount"] = messageDictionary["board"]["columnCount"]
                boardDictionary["rowCount"] = messageDictionary["board"]["rowCount"]
                boardDictionary["grid"] = outList
                outputDictionary["board"] = boardDictionary
            elif (compareResult == 0):
                outputDictionary["gameStatus"] = "error: no tiles can be shifted"

    return outputDictionary