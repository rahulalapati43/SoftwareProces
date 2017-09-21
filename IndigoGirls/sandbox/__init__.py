from random import *
def initializeGame(messageDictionary):
    outputDictionary = {}
    boardDictionary = {}
    if "rowCount" not in messageDictionary.keys():
        messageDictionary["rowCount"] = 4
    if "colCount" not in messageDictionary.keys():
        messageDictionary["colCount"] = 4
    if(messageDictionary["rowCount"] <= 1 or messageDictionary["rowCount"] > 100):
        outputDictionary["gameStatus"] = "error: rowCount is out of bounds"
    if(messageDictionary["colCount"] <= 1 or messageDictionary["colCount"] > 100):
        outputDictionary["gameStatus"] = "error: colCount is out of bounds"
    if(isinstance(messageDictionary["rowCount"],int) == False):
        outputDictionary["gameStatus"] = "error: rowCount is not an integer"
    if(isinstance(messageDictionary["colCount"],int) == False):
        outputDictionary["gameStatus"] = "error: colCount is not an integer"
    if(messageDictionary["rowCount"] > 1 and messageDictionary["rowCount"] <= 100):
        if(messageDictionary["colCount"] > 1 and messageDictionary["colCount"] <= 100):
            i = messageDictionary["rowCount"] * messageDictionary["colCount"]
            gridList = []
            for index in range (0,i):
                gridList[index] = 0
            x = randint(1,i)
            y = randint(1,i)
            randomList = [1,1,1,2]
            a = sample(randomList,2)
            gridList[x] = a[0]
            gridList[y] = a[1]
            outputDictionary["score"] = 0
            boardDictionary["rowCount"] = messageDictionary["rowCount"]
            boardDictionary["colCount"] = messageDictionary["colCount"]
            boardDictionary["grid"] = gridList
            outputDictionary["board"] = boardDictionary
            outputDictionary["gameStatus"] = "underway"

    return outputDictionary


