from random import *
def initializeGame(messageDictionary):
    outputDictionary = {}
    boardDictionary = {}
    x = 0
    y = 0
    i = 0
    if "rowCount" not in messageDictionary.keys():
        messageDictionary["rowCount"] = 4
    if "columnCount" not in messageDictionary.keys():
        messageDictionary["columnCount"] = 4
    if (messageDictionary["rowCount"] <= 1 or messageDictionary["rowCount"] > 100):
        outputDictionary["gameStatus"] = "error: rowCount is out of bounds"
    if (messageDictionary["columnCount"] <= 1 or messageDictionary["columnCount"] > 100):
        outputDictionary["gameStatus"] = "error: columnCount is out of bounds"
    if (isinstance(messageDictionary["rowCount"], int) == False):
        outputDictionary["gameStatus"] = "error: rowCount is not an integer"
    if (isinstance(messageDictionary["columnCount"], int) == False):
        outputDictionary["gameStatus"] = "error: columnCount is not an integer"
    if (messageDictionary["rowCount"] > 1 and messageDictionary["rowCount"] <= 100):
        if (messageDictionary["columnCount"] > 1 and messageDictionary["columnCount"] <= 100):
            i = messageDictionary["rowCount"] * messageDictionary["columnCount"]
            gridList = []
            for index in range(0, i):
                gridList.append(0)
            randomList = [1, 1, 1, 2]
            a = sample(randomList, 2)
            x = randint(0, i - 1)
            y = randint(0, i - 1)
            while (x == y):
                x = randint(0, i - 1)
                y = randint(0, i - 1)
            gridList[x] = a[0]
            gridList[y] = a[1]
            outputDictionary["score"] = 0
            boardDictionary["rowCount"] = messageDictionary["rowCount"]
            boardDictionary["columnCount"] = messageDictionary["columnCount"]
            boardDictionary["grid"] = gridList
            outputDictionary["board"] = boardDictionary
            outputDictionary["gameStatus"] = "underway"

    return outputDictionary